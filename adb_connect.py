#File that holds functions for connections
import psycopg2
import pandas as pd
import time

#basic function that creates connection to a postgres database and runs query
#there are many different api's for connecting to different database flavors
#input parameters to connect into this file and import into your notebook
#useful for data analysis workflows
def adb_conn():
    return psycopg2.connect(dbname = '<data_base_name>', user = '<user_name>', port = '<port_number>', host = '<host>', password = '<password>')

def run_query(query):
    print('Executing Query')
    start = time.time()
    database_connection = adb_conn()
    result = pd.read_sql(query, database_connection)
    print('Query returned {} results in {:.2f} seconds'.format(len(result),time.time() - start))
    return result


