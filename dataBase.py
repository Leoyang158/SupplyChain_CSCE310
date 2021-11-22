import  psycopg2
import csv

host = 'ec2-44-199-86-61.compute-1.amazonaws.com'

dbname = 'd9gadra8cohjt0'

user = 'jytzjupaqfytoj'

port = '5432'

password = '2235f9e7e2f3c4a1778c6dc71fd709d492b59563698615697430ebf7262767f1'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# using cur to execute the query here
cur.execut
# print(cur.fetchhone())

