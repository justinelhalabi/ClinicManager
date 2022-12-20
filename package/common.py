from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrive the patient, hospital and appointment count for the dashboard page"""

        conn.execute("SELECT COUNT(*) AS patient FROM patient")
        getPatientCount=conn.fetchone()

        conn.execute("SELECT COUNT(*) AS hospital FROM hospital")
        getHospitalCount=conn.fetchone()

        conn.execute("SELECT COUNT(*) AS governate FROM governate")
        getGovernateCount=conn.fetchone()

        conn.execute("SELECT COUNT(*) AS district FROM district")
        getDistrictCount=conn.fetchone()

        conn.execute("SELECT COUNT(*) AS medicalrecord FROM medicalrecord")
        getMedicalRecCount=conn.fetchone()

        conn.execute("SELECT COUNT(*) AS vaccine FROM vaccine")
        getVaccineCount=conn.fetchone()

        getPatientCount.update(getHospitalCount)
        getPatientCount.update(getGovernateCount)
        getPatientCount.update(getDistrictCount)
        getPatientCount.update(getMedicalRecCount)
        getPatientCount.update(getVaccineCount)

        return getPatientCount