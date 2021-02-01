from datetime import datetime
from flask import Flask, request
from flask_restx import Resource, Api
import psycopg2.errors as db_errors

from churn_api.infrastructure.config.config import config
from churn_api.domain.customer import CustomerPredict, CUSTOMER_MODEL
from churn_api.infrastructure.customer_dao import CustomerDAO

app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]

api = Api(app, version='1.0', title='Churn Predictor API',
    description='This API provides a range of services enabling you to get, post, edit and delete a Customer and to perform a churn prediction for the given customer.')

ns_customer = api.namespace('customers', description='Customers saved in the database')
ns_pred = api.namespace('predictions', description='Perform a churn prediction')
ns_creation = api.namespace('create_customer', description="enter a new customer")
customer_model = api.model('Customers', CUSTOMER_MODEL)


DAO = CustomerDAO()

@ns_customer.route('/<int:id>')
@ns_customer.response(404, 'customer not found')
@ns_customer.param('id', 'The customer identifier')
class Customer(Resource):
    '''API ressource related to the namespace '/customers/id' exposing get,delete and put methods'''

    @ns_customer.doc('get_customer')
    @ns_customer.marshal_with(customer_model)
    def get(self, id):
        '''Fetch a given customer'''
        customer = DAO.get(id)
        if customer is not None:
            return customer
        else:
            api.abort(404, "The customer {} doesn't exist".format(id))

    @ns_customer.doc('delete_customer')
    @ns_customer.response(204, 'customer deleted')
    def delete(self, id):
        '''Delete a customer given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns_customer.expect(customer_model)
    @ns_customer.marshal_with(customer_model)
    def put(self, id):
        '''Update a customer given its identifier'''
        customer = DAO.update(id, api.payload)
        if customer is not None:
            return customer
        else:
            api.abort(404, "The customer {} doesn't exist".format(id)) 

  
@ns_customer.route('/')
class new_customer(Resource):
    """ API Ressource related the namespace '/customers/' exposing post method to add new customers in the database"""

    @ns_customer.doc("Create customer")
    @ns_customer.expect(customer_model)
    @ns_customer.marshal_with(customer_model, code=201)
    @ns_customer.response(201, 'customer created')
    @ns_customer.response(409, 'customer already exists')
    def post(self):
        '''Create customer'''
        try :
            customer = DAO.create(api.payload)
            return customer, 201
        except db_errors.UniqueViolation:
            api.abort(409, "The customer already exist") 



@ns_pred.route("")
class churn_predictor(Resource):
    """ API Ressource related the namespace '/predictions/' exposing post method to get churn predictions"""

    @ns_pred.doc("get churn prediction from customer features")
    @ns_pred.expect(customer_model, validate=True)
    def post(self):
        input_json = request.get_json(force=True)
        try:
            customer = CustomerPredict(input_json)
            churn_prob = customer.predict_churn()
        except KeyError:
            return "Attention, veillez à renseigner dans le json d'entrée tous les champs, tel que montré dans l'exemple !"
        except TypeError:
            return "Attention, un ou plusieurs champs n'ont pas ete renseignes avec le bon type. Vérifiez dans l'exemple le type des valeurs à renseigner pour chaque champ !"
        except ValueError:
            return "Attention à ce que les valeurs de chaque champ remplissent bien les conditions spécifiées. En particulier, veillez à ce que la date soit bien au format '%d/%m/%Y'"
        return {"churn probability": round(churn_prob,3)}



if __name__ == "__main__":
    print("starting API at", datetime.now())
    app.run(debug=False, host=HOST, port=PORT)

