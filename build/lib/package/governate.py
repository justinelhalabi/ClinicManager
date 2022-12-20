from flask_restful import Resource, Api, request
# from package.model import conn, connection
import mysql.connector

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
# except:
#     print("Error connecting to server.")

conn1 = connection.cursor(dictionary=True, buffered=True)

class Governates(Resource):
    """It contain all the api carrying the activity with and specific governates"""

    def get(self):
        """Api to retive all the governates from the database"""

        conn1.execute("""SELECT * FROM governate""")
        governate = conn1.fetchall()
        print(governate)
        return governate

    def post(self):
        """api to add the governate in the database"""

        governateInput = request.get_json(force=True)
        Name = governateInput['Name']
        governateInput['ID'] = conn1.execute("""INSERT INTO governate (`Name`)
                  VALUES ('%s')""" % (Name))
        connection.commit()
        print("DONEEEEEEEEEEEEEEEEEEEEEEE")
        return governateInput


class Governate(Resource):
    """It contains all apis doing activity with the single governates entity"""

    def get(self, id):
        """api to retrieve details of the governate by it id"""

        conn1.execute("SELECT * FROM governate WHERE ID=%s" % (id))
        governate=conn1.fetchall()
        # print(governate)
        return governate

    def delete(self, id):
        """api to delete the governate by its id"""

        conn1.execute("DELETE FROM district WHERE GovID=%s" % (id))
        conn1.execute("DELETE FROM governate WHERE ID=%s" % (id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):
        """api to update the governate by it id"""

        governateInput = request.get_json(force=True)
        Name = governateInput['Name']
        conn1.execute(
            """UPDATE governate SET Name='%s' WHERE ID = %s"""
            %(Name, id))
        connection.commit()
        return governateInput
