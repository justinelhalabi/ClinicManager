from flask_restful import Resource, request
# from package.model import conn, connection

import mysql.connector
import datetime
# import pymysql

import json
with open('dbconn.json') as data_file:
    config = json.load(data_file)

connection = mysql.connector.connect(
# connection = pymysql.connect(
    host=config["host"],
    port=config["port"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)
print("Connected to '" + config["host"] + "' at port: " + str(config["port"]))

conn5 = connection.cursor(dictionary=True, buffered=True)
# conn = pymysql.cursors.DictCursor(connection=connection)


class Vaccines(Resource):

    def get(self):

        # conn.execute("""SELECT d.ID AS ID,d.Name AS Name,g.Name AS GovernateName FROM governate AS g RIGHT JOIN district AS d ON g.ID = d.GovID""")
        # print("HERE1")
        conn5.execute("""SELECT vaccine.*, hospital.Name AS hospitalName, CONCAT(patient.Fname,' ', patient.Lname) AS patientName FROM vaccine LEFT JOIN hospital ON vaccine.HospID = hospital.ID LEFT JOIN patient 
                        ON vaccine.PatientID = patient.ID""")
        vaccines = conn5.fetchall()
        for i in vaccines:
            i['DateTaken'] = str(i['DateTaken'])
        return vaccines

    def post(self):

        vaccineInput = request.get_json(force=True)
        DateTaken = vaccineInput['DateTaken']
        HospID=vaccineInput["HospID"]
        PatientID = vaccineInput["PatientID"]

        vaccineInput['ID'] = conn5.execute("""INSERT INTO vaccine (`DateTaken`,`HospID`,`PatientID`) VALUES ('%s',%s,%s)"""%((datetime.datetime.strptime(str(DateTaken), '%Y-%m-%d').date()),HospID,PatientID))
        connection.commit()
        return vaccineInput


class Vaccine(Resource):

    def get(self, id):

        conn5.execute("SELECT * FROM vaccine WHERE ID=%s" % (id))
        vaccine = conn5.fetchall()
        return vaccine

    def delete(self, id):

        conn5.execute("DELETE FROM vaccine WHERE ID=%s" % (id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):
        """api to update the district by it id"""

        vaccineInput = request.get_json(force=True)
        DateTaken = vaccineInput['DateTaken']
        HospID = vaccineInput["HospID"]
        PatientID = vaccineInput["PatientID"]

        conn5.execute(
            """UPDATE vaccine SET `DateTaken`='%s', `HospID`=%s, `PatientID`=%s WHERE ID = %s"""
            % ((datetime.datetime.strptime(str(DateTaken), '%Y-%m-%d').date()), HospID, PatientID, id))
        connection.commit()
        return vaccineInput
