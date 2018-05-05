'''
Created on Apr 1, 2018
@author: ishank
'''

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=test user=postgres password=anshu267")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (200, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
print(cur.fetchone())
print(cur.fetchone())
    
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
