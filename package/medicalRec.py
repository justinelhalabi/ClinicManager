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
conn2 = pymysql.cursors.DictCursor(connection=connection)

class MedicalRecs(Resource):

    def get(self):

        conn2.execute("""SELECT medicalrecord.*, patient.Fname, patient.Lname FROM medicalrecord LEFT JOIN patient ON patient.ID = medicalrecord.PatientID""")
        medicalRecs = conn2.fetchall()
        return medicalRecs



    def post(self):

        medicalRecInput = request.get_json(force=True)
        Is_Pregnant = medicalRecInput['Is_Pregnant']
        Has_BloodPressure = medicalRecInput['Has_BloodPressure']
        Has_Diabetes = medicalRecInput['Has_Diabetes']
        Has_Cancer = medicalRecInput['Has_Cancer']
        Has_RespiratoryD = medicalRecInput['Has_RespiratoryD']
        Has_HeartD = medicalRecInput['Has_HeartD']
        PatientID = medicalRecInput['PatientID']

        medicalRecInput['ID'] = conn2.execute("INSERT INTO hospital(`Is_Pregnant`,`Has_BloodPressure`,`Has_Diabetes`,`Has_Cancer`,`Has_RespiratoryD`,`Has_HeartD`,`PatientID`) "
                                          "VALUES('%s','%s','%s','%s','%s','%s','%s')"
                                              % (str(Is_Pregnant), str(Has_BloodPressure), str(Has_Diabetes), str(Has_Cancer), str(Has_RespiratoryD), str(Has_HeartD), str(PatientID)))

        connection.commit()
        return medicalRecInput

class MedicalRec(Resource):


    def get(self,id):

        conn2.execute("SELECT * FROM medicalrecord WHERE ID='%s'" % (id))
        medicalRec = conn2.fetchall()
        return medicalRec

    def delete(self, id):

        # conn.execute("DELETE FROM patient WHERE pat_id='%s'"%(id))
        conn2.execute("DELETE FROM medicalrecord WHERE ID='%s'" % (id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):

        medicalRecInput = request.get_json(force=True)
        Is_Pregnant = medicalRecInput['Is_Pregnant']
        Has_BloodPressure = medicalRecInput['Has_BloodPressure']
        Has_Diabetes = medicalRecInput['Has_Diabetes']
        Has_Cancer = medicalRecInput['Has_Cancer']
        Has_RespiratoryD = medicalRecInput['Has_RespiratoryD']
        Has_HeartD = medicalRecInput['Has_HeartD']
        PatientID = medicalRecInput['PatientID']

        conn2.execute(
            "UPDATE hospital SET `Is_Pregnant`='%s',`Has_BloodPressure`='%s',`Has_Diabetes`='%s',`Has_Cancer`='%s',`Has_RespiratoryD`='%s',`Has_HeartD`='%s',`PatientID`='%s' WHERE ID = '%s'"
            %(str(Is_Pregnant), str(Has_BloodPressure), str(Has_Diabetes), str(Has_Cancer), str(Has_RespiratoryD), str(Has_HeartD), str(PatientID), id))
        connection.commit()
        return medicalRecInput