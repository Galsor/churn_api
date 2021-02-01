# Churn Predictor 

Contributors: Antoine Meilliez, Marie Verdoux, Rayann Harmouni

## Usage
### 1 - Installation
You need an updated version of Python 3.8 to run this project. Check it with 
```
$ python3 --version
```
Process the following steps to install the project
```
# Clone the repository
$ git clone https://gitlab.com/yotta-academy/mle-bootcamp/projects/ml-prod-projects/fall-2020/churn_api.git

# Move in the repository
$ cd churn_api

# Initialize the project
$ source init.sh
$ source activate.sh

# Your Are Ready !
```
## 2 - Run the API locally

In your shell, run the following command:
``` 
$ python churn_api/application/server.py

```
You should see an hypertext link: http://0.0.0.0:5000/



If you click over the link, you can see the different commands you could do with the API. 

If you want to run command API commands, open another shell thumbnail and place yourself on the churn_api repository. 

``` 
$ cd churn_api/application

```

 - Create customer :
 
```
$ curl -X POST "http://0.0.0.0:5000/customers/" -H  "accept: application/json" -H  "Content-Type: application/json" -d @client.json

or 

$ curl -X POST "http://0.0.0.0:5000/customers/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"ID_CLIENT\": id,  \"NOM\": \"character\",  \"DATE_ENTREE\": \"date\",  \"PAYS\": \"character\",  \"SEXE\": \"character\",  \"MEMBRE_ACTIF\": \"booleen\",  \"NB_PRODUITS\": nombre,  \"CARTE_CREDIT\": \"booleen\",  \"AGE\": integer,  \"BALANCE\": float,  \"SCORE_CREDIT\": float,  \"SALAIRE\": float}"
```
 
 - Delete a customer given its identifier:
 
```
$ curl -X DELETE "http://0.0.0.0:5000/customers/id" -H  "accept:  
 application/json"
 
```
 - Fetch a given customer
 
``` 
$ curl -X GET "http://0.0.0.0:5000/customers/5678" -H  "accept: application/json"

```

 - Update customer
 
```
$ curl -X PUT "http://0.0.0.0:5000/customers/id" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"ID_CLIENT\": id,  \"NOM\": \"character\",  \"DATE_ENTREE\": \"date\",  \"PAYS\": \"character\",  \"SEXE\": \"character\",  \"MEMBRE_ACTIF\": \"booleen\",  \"NB_PRODUITS\": nombre,  \"CARTE_CREDIT\": \"booleen\",  \"AGE\": integer,  \"BALANCE\": float,  \"SCORE_CREDIT\": float,  \"SALAIRE\": float}"

```

 -  Make a prediction: 
 
``` 
$ curl -X  curl -X POST "http://0.0.0.0:5000/predictions/churn" -H  "accept: application/json" -H  "Content-Type: application/json" -d @client.json

or 

$  curl -X  curl -X POST "http://0.0.0.0:5000/predictions/churn" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"ID_CLIENT\": id,  \"NOM\": \"character\",  \"DATE_ENTREE\": \"date\",  \"PAYS\": \"character\",  \"SEXE\": \"character\",  \"MEMBRE_ACTIF\": \"booleen\",  \"NB_PRODUITS\": nombre,  \"CARTE_CREDIT\": \"booleen\",  \"AGE\": integer,  \"BALANCE\": float,  \"SCORE_CREDIT\": float,  \"SALAIRE\": float}"
```
## 3 - Run the API online

## 4 - Documentation

To see the documentation :

```
$ cd docs

$ firefox _build/html/index.html
or 
$ google-chrome _build/html/index.html

```

## Project Organisation

``` 

├── activate.sh
├── churn_api
│   ├── application
│   │   ├── false_client.json
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── server.cpython-38.pyc
│   │   │   └── train_model_for_appetence.cpython-38.pyc
│   │   └── server.py
│   ├── domain
│   │   ├── constraints.py
│   │   ├── customer.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── customer.cpython-38.pyc
│   │       ├── __init__.cpython-38.pyc
│   │       └── messages.cpython-38.pyc
│   ├── infrastructure
│   │   ├── config
│   │   │   ├── config.py
│   │   │   ├── config_template.yml
│   │   │   ├── config.yml
│   │   │   ├── key.json
│   │   │   └── __pycache__
│   │   │       └── config.cpython-38.pyc
│   │   ├── connection.py
│   │   ├── connexion_functions.py
│   │   ├── customers_table.py
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── __pycache__
│   │       ├── connection.cpython-38.pyc
│   │       ├── connexion.cpython-38.pyc
│   │       ├── connexion_functions.cpython-38.pyc
│   │       ├── customers_table.cpython-38.pyc
│   │       ├── __init__.cpython-38.pyc
│   │       └── model.cpython-38.pyc
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── settings.py
│   └── test
│       ├── functional
│       │   ├── client.json
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-38.pyc
│       │   │   ├── test_app.cpython-38.pyc
│       │   │   ├── test_customer.cpython-38.pyc
│       │   │   ├── test_server.cpython-38.pyc
│       │   │   └── test_server.cpython-38-pytest-5.4.2.pyc
│       │   ├── test_app.py
│       │   ├── test_customer.py
│       │   └── test_server.py
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-38.pyc
│       └── unit
│           ├── __init__.py
│           └── __pycache__
│               ├── __init__.cpython-38.pyc
│               ├── test.cpython-38.pyc
│               ├── test_customer.cpython-38.pyc
│               └── test_hello_world.cpython-38-pytest-5.4.2.pyc
├── cloud_sql_proxy
├── conf.py
├── deployment
│   └── deployment_template.yml
├── Dockerfile
├── docs
│   ├── _build
│   │   ├── doctrees
│   │   │   ├── application.doctree
│   │   │   ├── churn_api.churn_api.application.doctree
│   │   │   ├── churn_api.churn_api.doctree
│   │   │   ├── churn_api.churn_api.domain.doctree
│   │   │   ├── churn_api.churn_api.infrastructure.doctree
│   │   │   ├── churn_api.churn_api.test.doctree
│   │   │   ├── churn_api.doctree
│   │   │   ├── churn_api.application.doctree
│   │   │   ├── churn_api.doctree
│   │   │   ├── churn_api.domain.doctree
│   │   │   ├── churn_api.infrastructure.doctree
│   │   │   ├── churn_api.test.doctree
│   │   │   ├── churn_api.test.functional.doctree
│   │   │   ├── churn_api.test.functional.test_app.doctree
│   │   │   ├── churn_api.test.functional.test_customer.doctree
│   │   │   ├── churn_api.test.unit.doctree
│   │   │   ├── churn_api.test.unit.test_server.doctree
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   └── modules.doctree
│   │   └── html
│   │       ├── application.html
│   │       ├── churn_api.churn_api.application.html
│   │       ├── churn_api.churn_api.domain.html
│   │       ├── churn_api.churn_api.html
│   │       ├── churn_api.churn_api.infrastructure.html
│   │       ├── churn_api.churn_api.test.html
│   │       ├── churn_api.html
│   │       ├── churn_api.application.html
│   │       ├── churn_api.domain.html
│   │       ├── churn_api.html
│   │       ├── churn_api.infrastructure.html
│   │       ├── churn_api.test.functional.html
│   │       ├── churn_api.test.functional.test_app.html
│   │       ├── churn_api.test.functional.test_customer.html
│   │       ├── churn_api.test.html
│   │       ├── churn_api.test.unit.html
│   │       ├── churn_api.test.unit.test_server.html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       ├── _sources
│   │       │   ├── application.rst.txt
│   │       │   ├── churn_api.churn_api.application.rst.txt
│   │       │   ├── churn_api.churn_api.domain.rst.txt
│   │       │   ├── churn_api.churn_api.infrastructure.rst.txt
│   │       │   ├── churn_api.churn_api.rst.txt
│   │       │   ├── churn_api.churn_api.test.rst.txt
│   │       │   ├── churn_api.rst.txt
│   │       │   ├── churn_api.application.rst.txt
│   │       │   ├── churn_api.domain.rst.txt
│   │       │   ├── churn_api.infrastructure.rst.txt
│   │       │   ├── churn_api.rst.txt
│   │       │   ├── churn_api.test.functional.rst.txt
│   │       │   ├── churn_api.test.functional.test_app.rst.txt
│   │       │   ├── churn_api.test.functional.test_customer.rst.txt
│   │       │   ├── churn_api.test.rst.txt
│   │       │   ├── churn_api.test.unit.rst.txt
│   │       │   ├── churn_api.test.unit.test_server.rst.txt
│   │       │   ├── index.rst.txt
│   │       │   └── modules.rst.txt
│   │       └── _static
│   │           ├── alabaster.css
│   │           ├── basic.css
│   │           ├── custom.css
│   │           ├── doctools.js
│   │           ├── documentation_options.js
│   │           ├── file.png
│   │           ├── jquery-3.5.1.js
│   │           ├── jquery.js
│   │           ├── language_data.js
│   │           ├── minus.png
│   │           ├── plus.png
│   │           ├── pygments.css
│   │           ├── searchtools.js
│   │           ├── underscore-1.3.1.js
│   │           └── underscore.js
│   ├── churn_api.application.rst
│   ├── churn_api.domain.rst
│   ├── churn_api.infrastructure.rst
│   ├── churn_api.rst
│   ├── churn_api.test.functional.rst
│   ├── churn_api.test.rst
│   ├── churn_api.test.unit.rst
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── modules.rst
│   ├── requirements.txt
│   ├── _static
│   └── _templates
├── index.rst
├── __init__.py
├── init_sql.sh
├── make.bat
├── Makefile
├── new_customer.json
├── README.md
├── requirements.txt
├── run_sql_proxy.sh
├── setup.py
└── source
    └── conf.py


```