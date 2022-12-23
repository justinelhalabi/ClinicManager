#Python 2.7

from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.hospital import Hospitals, Hospital
from package.governate import Governates, Governate
from package.district import Districts, District
from package.medicalRec import MedicalRecs, MedicalRec
from package.vaccine import Vaccines, Vaccine


from package.common import Common
import json


with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')

api.add_resource(Hospitals, '/hospital')
api.add_resource(Hospital, '/hospital/<int:id>')

api.add_resource(Governates, '/governate')
api.add_resource(Governate, '/governate/<int:id>')

api.add_resource(Districts, '/district')
api.add_resource(District, '/district/<int:id>')

api.add_resource(MedicalRecs, '/medicalRec')
api.add_resource(MedicalRec, '/medicalRec/<int:id>')

api.add_resource(Vaccines, '/vaccine')
api.add_resource(Vaccine, '/vaccine/<int:id>')

api.add_resource(Common, '/common')

# Routes

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=False, host=config['host'], port=config['port'])
    # app.run(debug=False, host=config['host'])