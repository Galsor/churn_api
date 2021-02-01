import json

from churn_api.domain.customer import CUSTOMERS_TABLE_COLUMNS, FEATURES
from churn_api.infrastructure.connection import db_connect


class CustomerDAO(object):
    """ Data access objects, managing database connection and exposing methods to manipulate these data."""
    def __init__(self):
        pass


    @db_connect()
    def get(connection, self, id):
        """for customer in self.customers:
            if customer[FEATURES[1]] == id:
                return customer
        """
        postgres_query = """SELECT * FROM customers WHERE ID_CLIENT = %s"""
        with connection.cursor() as cursor:
            cursor.execute(postgres_query, [id])
            customer = cursor.fetchone()
        return self.format_db_output(customer)


    @db_connect()
    def create(connection, self,data):
        values = [data[f] for f in CUSTOMERS_TABLE_COLUMNS]
        postgres_query = f"""INSERT INTO customers (ID_CLIENT,DATE_ENTREE, NOM, PAYS, SEXE, MEMBRE_ACTIF,
            NB_PRODUITS, CARTE_CREDIT, AGE, BALANCE, SCORE_CREDIT, SALAIRE) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        with connection.cursor() as cursor:
            cursor.execute(postgres_query, values)
            connection.commit()
        customer = self.get(data[CUSTOMERS_TABLE_COLUMNS[0]])
        return self.format_db_output(customer)

    @db_connect()
    def update(connection, self, id, data):
        values = [data[f] for f in FEATURES if f!=FEATURES[1]]
        values.append(id)
        postgres_query = """UPDATE customers 
                            SET DATE_ENTREE=%s, NOM=%s, PAYS=%s, SEXE=%s, MEMBRE_ACTIF=%s, NB_PRODUITS=%s, CARTE_CREDIT=%s, AGE=%s, BALANCE=%s, SCORE_CREDIT=%s, SALAIRE=%s
                            WHERE ID_CLIENT=%s"""
        with connection.cursor() as cursor:
            cursor.execute(postgres_query, values)
            connection.commit()
        customer = self.get(id)
        return self.format_db_output(customer)

    @db_connect()
    def delete(connection, self, id):
        """customer = self.get(id)
        self.customers.remove(customer)   """
        postgres_query = """DELETE FROM customers WHERE ID_CLIENT=%s"""
        with connection.cursor() as cursor:
            cursor.execute(postgres_query, [id])
            connection.commit()
        return f"Customer {id} deleted."

    def format_db_output(self, customer):
        return {k:v for k,v in zip(CUSTOMERS_TABLE_COLUMNS,customer)}

    def create_customer(self):
        ID_CLIENT = input("Inserez l'identifiant du client")
        NOM = input("Inserez le nom du client")
        DATE_ENTREE = input("Inserez la date du début de contrat du client avec la banque")
        PAYS = input("Dans quel pays le client est-il localisé ?")
        SEXE = input("Quel est le sexe du client ?")
        MEMBRE_ACTIF = input("Le client est-il un membre actif de la banque ?")
        NB_PRODUITS = input("A combien de produits le client a souscrit ?")
        CARTE_CREDIT = input("Le client a t-il une carte de crédit ?")
        AGE = input("Quel est l'age du client ?")
        BALANCE = input("Inserez le solde du client")
        SCORE_CREDIT = input("Inserez le score de credit du client")
        SALAIRE = input("Inserez le montant du salaire du client")
        new_customer = {"ID_CLIENT": ID_CLIENT,
         "NOM": NOM,
         "DATE_ENTREE": DATE_ENTREE,
         "PAYS": PAYS,
         "SEXE": SEXE,
         "MEMBRE_ACTIF": MEMBRE_ACTIF,
         "NB_PRODUITS": NB_PRODUITS,
         "CARTE_CREDIT": CARTE_CREDIT,
         "AGE": AGE,
         "BALANCE": BALANCE,
         "SCORE_CREDIT": SCORE_CREDIT,
         "SALAIRE": SALAIRE
         }
        with open('new_customer.json', 'w') as outfile:
            json.dump(new_customer, outfile)
        return outfile


@db_connect()
def init_customers_table(connection):
    """Create the customer table"""
    commands = (
        """CREATE TABLE customers (
            ID_CLIENT INTEGER PRIMARY KEY, 
            DATE_ENTREE VARCHAR(10) NOT NULL, 
            NOM VARCHAR(255) NOT NULL, 
            PAYS VARCHAR(255), 
            SEXE VARCHAR(1), 
            MEMBRE_ACTIF VARCHAR(3), 
            NB_PRODUITS INTEGER, 
            CARTE_CREDIT VARCHAR(3), 
            AGE INTEGER, BALANCE INTEGER, 
            SCORE_CREDIT INTEGER, 
            SALAIRE INTEGER
            )
    """,)
    with connection.cursor() as cursor:
        for command in commands:
            cursor.execute(command)
        connection.commit()