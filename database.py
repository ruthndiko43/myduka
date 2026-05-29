import psycopg2

#establishing a connection to a postgrees database
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='1234',dbname='myduka')

#cur object
cur=conn.cursor()

cur.execute("select * from products")
products_data = cur.fetchall()
print(products_data)