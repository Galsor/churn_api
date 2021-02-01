import os
import requests
import subprocess
from churn_api.infrastructure.config.config import *
from churn_api.settings import URL_MASTER, URL_STAGING
import pytest
import json

BRANCH_NAME = os.getenv("BRANCH_NAME")
this_dir = os.path.dirname(os.path.realpath(__file__))

if BRANCH_NAME == 'staging':
    url_base = URL_STAGING
elif BRANCH_NAME == 'master':
    url_base = URL_MASTER


url_prediction = url_base+"/predictions"
url_customer = url_base+"/customers/"
print(url_prediction)


client1 = { 'FEATURES' : {"ID_CLIENT":15688172, 
    "NOM":"Tai", 
    "DATE_ENTREE":"2015-01-01", 
    "PAYS":"Espagne", 
    "SEXE":"H", 
    "MEMBRE_ACTIF":"No", 
    "NB_PRODUITS":2, 
    "CARTE_CREDIT":"Yes", 
    "AGE":50, 
    "BALANCE":0, 
    "SCORE_CREDIT":677, 
    "SALAIRE": 88947.56},
    'CHURN_PROB': 0.539}

client2 = { 'FEATURES' : {"ID_CLIENT":15791700, 
    "NOM":"Ugochukwutubelum", 
    "DATE_ENTREE":"2018-01-01", 
    "PAYS":"Allemagne", 
    "SEXE":"H", 
    "MEMBRE_ACTIF":"No", 
    "NB_PRODUITS":4, 
    "CARTE_CREDIT":"Yes", 
    "AGE":47, 
    "BALANCE":118079.47, 
    "SCORE_CREDIT":773, 
    "SALAIRE": 143007.49},
    'CHURN_PROB': 0.726}

false_client = { 'FEATURES' : {"ID_CLIENT":15791700, 
    "NOM":"Ugochukwutubelum", 
    "DATE_ENTREE":"2018-01-01", 
    "PAYS":"Allemagne", 
    "SEXE":"H", 
    "MEMBRE_ACTIF":"Oui", 
    "NB_PRODUITS":4, 
    "CARTE_CREDIT":"Yes", 
    "AGE":47, 
    "BALANCE":118079.47, 
    "SCORE_CREDIT":773, 
    "SALAIRE": 143007.49},
    'CHURN_PROB': 0.726}


@pytest.mark.parametrize("customer_data, expected_churn", [(client1['FEATURES'], client1['CHURN_PROB']), (client2['FEATURES'], client2['CHURN_PROB'])])
def test_expected_churn(customer_data, expected_churn):
    response = requests.post(url_prediction, json=customer_data)
    results = response.json()
    assert results["churn probability"] == expected_churn

@pytest.mark.parametrize("customer_data", [client1['FEATURES'], client2['FEATURES']])
def test_expected_status(customer_data):
    response = requests.post(url_prediction, json=customer_data)
    results = response.status_code
    assert results == 200

@pytest.mark.parametrize("customer_data", [false_client['FEATURES'], false_client['CHURN_PROB']])
def test_expected_status(customer_data):
    response = requests.post(url_prediction, json=customer_data)
    results = response.status_code
    assert results == 400


def test_customer_get_status_fail():
    response = requests.get(url_customer+f"{client2['FEATURES']['ID_CLIENT']}")
    result = response.status_code
    assert result == 500

def test_customer_get_data():
    response = requests.get(url_customer+"3456")
    assert response.status_code == 200

def test_customer_delete():
    response = requests.delete(url_customer+f"{client2['FEATURES']['ID_CLIENT']}")
    assert response.status_code == 204
