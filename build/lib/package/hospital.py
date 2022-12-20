#Python 2.7

from flask_restful import Resource, Api, request
# from package.model import conn, connection

import pymysql

import json
with open('dbconn.json') as data_file:
    config = json.load(data_file)

connection = pymysql.connect(
    host=config["host"],
    port=config["port"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)
print("Connected to '" + config["host"] + "' at port: " + str(config["port"]))
# except:
#     print("Error connecting to server.")

# conn = connection.cursor(dictionary=True, buffered=True)
conn3 = pymysql.cursors.DictCursor(connection=connection)

class Hospitals(Resource):
    """This contain api is to carry out activity with all hospitals"""

    def get(self):
        """Retrieve list of all the hospitals"""

        conn3.execute("""SELECT hospital.*, district.Name AS districtName FROM hospital LEFT JOIN district ON hospital.DistrictID = district.ID""")
        hospitals = conn3.fetchall()
        return hospitals



    def post(self):
        """Add the new Hospital"""

        hospitalInput = request.get_json(force=True)
        hosp_Name = hospitalInput['Name']
        hosp_Phone = hospitalInput['Phone']
        hosp_Capacity = hospitalInput['Capacity']
        hosp_DistID = hospitalInput['DistrictID']

        hospitalInput['ID'] = conn3.execute("INSERT INTO hospital(`Name`,`Phone`,`Capacity`,`DistrictID`) "
                                          "VALUES('%s','%s', '%s', '%s')"
                                            % (str(hosp_Name), str(hosp_Phone), str(hosp_Capacity), str(hosp_DistID)))

        connection.commit()
        return hospitalInput

class Hospital(Resource):
    """It includes all the apis carrying out the activity with the single hospital"""


    def get(self,id):
        """get the details of the hospital by the hospital id"""

        conn3.execute("SELECT * FROM hospital WHERE ID='%s'" % (id))
        hospital = conn3.fetchall()
        return hospital

    def delete(self, id):
        """api to delete the hospital by its id"""

        # conn.execute("DELETE FROM patient WHERE pat_id='%s'"%(id))
        conn3.execute("DELETE FROM hospital WHERE ID='%s'" % (id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):
        """api to update the hospital by it id"""

        hospitalInput = request.get_json(force=True)
        hosp_Name = hospitalInput['Name']
        hosp_Phone = hospitalInput['Phone']
        hosp_Capacity = hospitalInput['Capacity']
        hosp_DistID = hospitalInput['DistrictID']
        conn3.execute(
            "UPDATE hospital SET Name='%s',Phone='%s',Capacity='%s',DistrictID='%s' WHERE ID = '%s'"
            %(hosp_Name, str(hosp_Phone), str(hosp_Capacity), str(hosp_DistID), id))
        connection.commit()
        return hospitalInput