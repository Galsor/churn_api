from functools import wraps
import psycopg2
from sqlalchemy import create_engine
from churn_api.infrastructure.config.config import config


class Connection(object):
    def __init__(self): 
        """
	    config_file : dict
		    The YAML file describing the connexion configuration to postgresql
        """
        param = config["postgresql"]
        self.username = param["username"]
        self.password = param["password"]
        self.hostname = param["hostname"]
        self.database = param["database"]
        self.port = param["port"]

    def connect(self, sqlalchemy_engine=False):
        """
        Explanation
        -----------
        the return object should be used with pd.read_sql()

        Example
        -------
        >>> import pandas as pd
        >>> engine = Connexion(CONFIG_PATH).connect()
        >>> df = pd.read_sql("SELECT * FROM table;", engine)
        """
        if sqlalchemy_engine:
            return self._sqlalchemy
        else:
            return self._psycopg2

    @property
    def _sqlalchemy(self):
        """Return connexion using sqlalchemy engine because DataFrame.to_sql is not supported by psycopg2 for postgresql"""
        url = "postgresql://{0}:{1}@{2}:{3}/{4}".format(self.username, 
                                                        self.password, 
                                                        self.hostname, 
                                                        self.port,
                                                        self.database)
        engine = create_engine(url)
        return engine
        
    @property
    def _psycopg2(self):
        return psycopg2.connect(user=self.username,
                                password=self.password,
                                host=self.hostname,
                                database=self.database,
                                port=self.port)

def db_connect():
    def wrap(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                conn = Connection().connect()
                return_val = f(conn, *args, **kwargs)
            
            finally:
                conn.close()
            
            return return_val
        return wrapper
    return wrap