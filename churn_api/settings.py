from flask_restx import fields

FEATURES = ['DATE_ENTREE', 'ID_CLIENT', 'NOM', 'PAYS', 'SEXE','MEMBRE_ACTIF',
            'NB_PRODUITS', 'CARTE_CREDIT', 'AGE', 'BALANCE', 'SCORE_CREDIT', 'SALAIRE']

CUSTOMER_MODEL = {
    'ID_CLIENT': fields.Integer(example=3456, default = 123456789, readonly=True, description='The customer unique identifier'),
    'NOM': fields.String(example= 'Garcia', default= 'Anonymous', readonly = True,description='The customer name'),
    'DATE_ENTREE': fields.DateTime(example='2019-05-23',required=True, description='The date when the customer joined the bank formatted as yyyy-mm-dd'),
    'PAYS': fields.String(example='Espagne', enum= ['France', 'Espagne', 'Allemagne'],required=True, description='The country of customer'),
    'SEXE' : fields.String(example='H', enum=['H', 'F'],required=True, description='The customer gender'),
    'MEMBRE_ACTIF': fields.String(example='Yes', enum=['Yes', 'No'], required=True, description='Whether the customer is active or not'),
    'NB_PRODUITS': fields.Integer(example= 1, min=1, max=4,required=True, description='The amount of product subscribed by the customer'),
    'CARTE_CREDIT': fields.String(example= 'No', enum=['Yes', 'No'],required=True, description='Whether the customer has a credit card or not'),
    'AGE': fields.Integer(example= 58, min = 18, max = 130,required=True, description='The age of the customer'),
    'BALANCE': fields.Float(example= 500.89, min=0, max = 10**6, required=True, description='The customer balance'),
    'SCORE_CREDIT': fields.Integer(example= 456, min = 350, max= 850, required=True, description='The credit score of the customer'),
    'SALAIRE' : fields.Float(example= 60789.2, min=0, max = 10**6, required=True, description='The income of the customer'),
}

BUCKET_NAME = "chaos-2"

MODEL_NAME = "churn_classifier.joblib"

URL_MASTER = "http://35.233.44.81:5000"
URL_STAGING = "http://104.155.30.83:5000"