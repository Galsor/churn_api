
import pandas as pd
from flask_restx import fields
from datetime import datetime
from churn_api.infrastructure.model import load_model

MODEL=load_model()

FEATURES = ['DATE_ENTREE', 'ID_CLIENT', 'NOM', 'PAYS', 'SEXE','MEMBRE_ACTIF',
            'NB_PRODUITS', 'CARTE_CREDIT', 'AGE', 'BALANCE', 'SCORE_CREDIT', 'SALAIRE']

CUSTOMERS_TABLE_COLUMNS = ['ID_CLIENT','DATE_ENTREE', 'NOM', 'PAYS', 'SEXE','MEMBRE_ACTIF',
            'NB_PRODUITS', 'CARTE_CREDIT', 'AGE', 'BALANCE', 'SCORE_CREDIT', 'SALAIRE']


CUSTOMER_MODEL = {
    'ID_CLIENT': fields.Integer(example=3456, default = 123456789, required=True, description='The customer unique identifier'),
    'NOM': fields.String(example= 'Garcia', default= 'Anonymous',required=True, description='The customer name'),
    'DATE_ENTREE': fields.DateTime(example="2018-06-01",required=True, description='The date when the customer joined the bank formatted as yyyy-mm-dd'),
    'PAYS': fields.String(example='Espagne', enum= ['France', 'Espagne', 'Allemagne'],required=True, description='The country of customer'),
    'SEXE' : fields.String(example='H', enum=['H', 'F'],required=True, description='The customer gender'),
    'MEMBRE_ACTIF': fields.String(example='Yes', enum=['Yes', 'No'], required=True, description='Whether the customer is active or not'),
    'NB_PRODUITS': fields.Integer(example= 3, min=1, max=4,required=True, description='The amount of product subscribed by the customer'),
    'CARTE_CREDIT': fields.String(example= 'No', enum=['Yes', 'No'],required=True, description='Whether the customer has a credit card or not'),
    'AGE': fields.Integer(example= 50, min = 18, max = 130,required=True, description='The age of the customer'),
    'BALANCE': fields.Float(example= 500.89, min=0, max = 10**6, required=True, description='The customer balance'),
    'SCORE_CREDIT': fields.Integer(example= 650, min = 350, max= 850, required=True, description='The credit score of the customer'),
    'SALAIRE' : fields.Float(example= 60789.2, min=0, max = 10**6, required=True, description='The income of the customer'),
}

class CustomerPredict:

    def __init__(self, data: dict):
        """
        Parameters
        ----------
        data: dict
            customer data, used for prediction:
            'DATE_ENTREE', 'ID_CLIENT', 'NOM', 'PAYS', 'SEXE','MEMBRE_ACTIF',
            'NB_PRODUITS', 'CARTE_CREDIT', 'AGE', 'BALANCE', 'SCORE_CREDIT', 'SALAIRE'
        """
        self.data = data
        self.model = MODEL


    def predict_churn(self) -> float:
        """Returns churn probability of the customer predicted by the model
        
        Returns
        -------
        churn_prob: float
            appetence of the customer to churn (0: not appetent, 1: very appetent)

        Explanation
        -----------
        We construct the features from the caracteristics and the socio economic data.
        At the moment, we use arbitrary features. This should be changed.
        """
        customer_data = self.data.copy()
        customer_data["DATE_ENTREE"]=datetime.strptime(customer_data["DATE_ENTREE"], "%Y-%m-%d")
        X = pd.DataFrame({feature: [customer_data[feature]] for feature in FEATURES})
        churn_prob = self.model.predict_proba(X)[0][1]
        return churn_prob


