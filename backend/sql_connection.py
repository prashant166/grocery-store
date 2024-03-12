from mysql import connector

__cnx = None
def get_sql_connection():
    global  __cnx
    if __cnx is None:
        __cnx = connector.connect(user='root', password='123456',
                                  host='127.0.0.1',
                                  database='grocery_store')
    return  __cnx