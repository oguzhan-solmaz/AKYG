from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Ucus(Resource):
    def get(self):
        data = pd.read_csv('ucak.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        havaalani = request.args['havaalani']
        kalkis = request.args['kalkis']
        inis = request.args['inis']
        saat= request.args['saat']
        req_data = pd.DataFrame({'havaalani': [havaalani],
                                  'kalkis': [kalkis],
                                  'inis': [inis],
                                  'saat':[saat]})
        data = pd.read_csv('ucak.csv')
        data = data.append(req_data, ignore_index=True)
        data.to_csv('ucak.csv', index=False)
        return ({'message': 'Record successfully added.'}, 200)

     def delete(self):
        name = request.args['havaalani']
        data = pd.read_csv('ucak.csv')

        if name in data['havaalani'].values:
            data = data[data['havaalani'] != name]
            data.to_csv('ucak.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

class Name(Resource):
    def get(self):
        data = pd.read_csv('ucak.csv',usecols=[0])
        data = data.to_dict('records')
        return {'data' : data}, 200

api.add_resource(Ucus, '/ucus')
api.add_resource(Name, '/havaalani')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)