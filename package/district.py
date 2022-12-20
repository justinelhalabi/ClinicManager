from flask_restful import Resource, request
# from package.model import conn, connection
import mysql.connector
# import pymysql

import json
with open('dbconn.json') as data_file:
    config = json.load(data_file)

connection = mysql.connector.connect(
    host=config["host"],
    port=config["port"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)
print("Connected to '" + config["host"] + "' at port: " + str(config["port"]))

conn4 = connection.cursor(dictionary=True, buffered=True)
# conn = pymysql.cursors.DictCursor(connection=connection)


class Districts(Resource):
    """This contain apis to carry out activity with all districts"""

    def get(self):
        """Retrieve all the districts and return in form of json"""

        # conn.execute("""SELECT d.ID AS ID,d.Name AS Name,g.Name AS GovernateName FROM governate AS g RIGHT JOIN district AS d ON g.ID = d.GovID""")
        # print("HERE1")
        conn4.execute("""SELECT * FROM district""")
        # print('HERE2')
        districts = conn4.fetchall()
        for i in range(len(districts)):
            GovID = districts[i]['GovID']
            conn4.execute("SELECT governate.Name FROM governate WHERE ID=%s" % (GovID))
            govName = conn4.fetchall()
            # print(govName)
            districts[i]['GovernateName'] = govName[0]['Name']
        # print(districts)
        return districts

    def post(self):
        """api to add the district in the database"""

        districtInput = request.get_json(force=True)
        Name = districtInput['Name']
        GovID=districtInput["GovID"]
        districtInput['ID'] = conn4.execute("""SELECT @id := id FROM governate WHERE governate.ID ='%s';
                                            INSERT INTO district (`Name`,`GovID`) VALUES ('%s',@id)"""
                                            % (GovID,Name), multi=True)
        connection.commit()
        return districtInput


class District(Resource):
    """It contains all apis doing activity with the single districts entity"""

    def get(self, id):
        """api to retrieve details of the district by it id"""

        conn4.execute("SELECT * FROM district WHERE ID=%s" % (id))
        district = conn4.fetchall()
        return district

    def delete(self, id):
        """api to delete the district by its id"""

        # conn.execute("DELETE FROM hospital WHERE DisrtictID=%s"%(id))
        # conn.execute("DELETE FROM patient WHERE DistID=%s"%(id))
        conn4.execute("""DELETE district, patient, hospital, civilian, medical,nationalpersonnel, vaccine FROM """)

        conn4.execute("DELETE FROM district WHERE ID=%s" % (id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):
        """api to update the district by it id"""

        districtInput = request.get_json(force=True)
        Name = districtInput['Name']
        print(districtInput)
        conn4.execute(
            """UPDATE district SET Name='%s' WHERE ID = %s"""
            % (Name, id))
        connection.commit()
        return districtInput
