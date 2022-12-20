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
#######################JUSTIN#######################2

# conn = connection.cursor(dictionary=True, buffered=True)
conn = pymysql.cursors.DictCursor(connection=connection)

class Patients(Resource):
    """It contain all the api carrying the activity with and specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        # patients = conn.execute("SELECT * FROM patient  ORDER BY pat_date DESC").fetchall()
        conn.execute("SELECT patient.*, CONCAT(patient.Fname, ' ', patient.Lname) AS patientFullName FROM patient")
        patients = conn.fetchall()
        return patients

    def post(self):
        """api to add the patient in the database"""

        patientInput = request.get_json(force=True)
        pat_FN = patientInput['Fname']
        pat_LN = patientInput['Lname']
        pat_Gender = patientInput['Gender']
        pat_Phone = patientInput['Phone']
        pat_Email = patientInput['Email']
        CovidPos=patientInput['CovidPositive']
        pat_Med_Rec = patientInput['MedRecID']
        pat_District = patientInput['DistID']

        patientInput['ID'] = conn.execute("INSERT INTO patient(Fname,Lname,Gender,Phone,Email,CovidPositive,MedRecID,DistID) "
                                              "VALUES('%s','%s', '%s', %s, '%s',%s,%s,%s)"
                                              %(pat_FN, pat_LN, pat_Gender, pat_Phone, pat_Email,CovidPos, pat_Med_Rec,pat_District))

        connection.commit()
        # pat_ID = patientInput['']
        return patientInput


class Patient(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self, id):
        """api to retrive details of the patient by it id"""

        # conn.execute("SELECT * FROM patient WHERE pat_id='%s'"%(id))
        conn.execute("SELECT * FROM patient WHERE ID='%s'"%(id))
        patient=conn.fetchall()
        return patient

    def delete(self, id):
        """api to delete the patiend by its id"""

        # conn.execute("DELETE FROM patient WHERE pat_id='%s'"%(id))
        conn.execute("DELETE FROM patient WHERE ID='%s'"%(id))
        connection.commit()
        return {'msg': 'successfully deleted'}

    def put(self, id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        pat_FN = patientInput['Fname']
        pat_LN = patientInput['Lname']
        pat_Gender = patientInput['Gender']
        pat_Phone = patientInput['Phone']
        pat_Email = patientInput['Email']
        CovidPos=patientInput['CovidPositive']
        pat_Med_Rec = patientInput['MedRecID']
        pat_District = patientInput['DistID']
        conn.execute(
            "UPDATE patient SET Fname='%s',Lname='%s',Gender='%s',Phone=%s,Email='%s',CovidPositive=%s,MedRecID='%s',DistID=%s WHERE id = %s"
            %(pat_FN, pat_LN, pat_Gender, pat_Phone, pat_Email,CovidPos,pat_Med_Rec, pat_District,id))
        connection.commit()
        return patientInput
