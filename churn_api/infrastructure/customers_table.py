

def get_tables(connection):
    """print the names of the existing tables in the remote database"""
    with connection.cursor() as cursor:
        cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';""")
        for table in cursor.fetchall():
            print(table)
