constraint_scheme = {
    "DATE_ENTREE": {'type': str, 'format': "%d/%m/%Y"}, 
    "ID_CLIENT": {'type': int},  
    "NOM": {'type': str}, 
    "PAYS": {'type': str, 'values'=['France', 'Espagne', 'Allemagne']}, 
    "SEXE": {'type': str, 'values'=['H', 'F']}, 
    "MEMBRE_ACTIF": {'type': str, 'values': ['Yes', 'No']}, 
    "NB_PRODUITS": {'type': int, 'range': [1,4]},  
    "CARTE_CREDIT": {'type': str, 'values': ['Yes', 'No']}, 
    "AGE": {'type': int, 'range': [18, 130]},  
    "BALANCE": {'type': float, 'range': [0, 10**6]},  
    "SCORE_CREDIT": {'type': float, 'range': [350, 850]},  
    "SALAIRE": {'type': float, 'range': [0, 10**6]},  
    }

client = {"DATE_ENTREE": "01/06/2018", 
    "ID_CLIENT": 3456, 
    "NOM": "Garcia", 
    "PAYS": "Espagne", 
    "SEXE": "H",
    "MEMBRE_ACTIF": "Yes",
    "NB_PRODUITS":24, 
    "CARTE_CREDIT": "Yes", 
    "AGE": 50, 
    "BALANCE": 0, 
    "SCORE_CREDIT": 500, 
    "SALAIRE": 50000}



def check_json(client, contraint_scheme)
    features = list(constraint_scheme.keys())
    for feature in features:
        constraint = constraint_scheme[feature]
        if not isinstance(client[feature], constraint['type']):
            return "Champ {}: type fourni non acceptable. Type attendu: {}".format(feature, constraint['type'])
        elif constraint['type'] == str:
            if client[feature] not in constraint['values']:
                return "Champ {}: valeur fournie en dehors des valeurs acceptables {}".format(feature, constraint['values'])
        elif constraint['type'] == float or constraint['type'] == int:
            if client[feature] not in constraint['range']:
                return "Champ {}: valeur fournie en dehors des valeurs acceptables {}".format(feature, constraint['values'])
        


