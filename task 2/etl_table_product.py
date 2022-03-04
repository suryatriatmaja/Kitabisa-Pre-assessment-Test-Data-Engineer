import psycopg2

#Postgres configuration
connection = psycopg2.connect(user="postgres",
                              password="221296",
                              host="localhost",
                              port="5432",
                              database="postgres")
#Set autocommit
connection.autocommit = True
cursor = connection.cursor()

#Query create table product
create_table = 'CREATE TABLE IF NOT EXISTS public.product(id character varying COLLATE pg_catalog."default",type character varying COLLATE pg_catalog."default",name character varying COLLATE pg_catalog."default",ppu real,batters json,topping json) TABLESPACE pg_default'

#Data json
data_json = '[{"id":"0001","type":"donut","name":"Cake","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1002","type":"Chocolate"},{"id":"1003","type":"Blueberry"},{"id":"1004","type":"Devil''sFood"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5007","type":"PowderedSugar"},{"id":"5006","type":"ChocolatewithSprinkles"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]},{"id":"0002","type":"donut","name":"Raised","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5005","type":"Sugar"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]},{"id":"0003","type":"donut","name":"OldFashioned","ppu":0.55,"batters":{"batter":[{"id":"1001","type":"Regular"},{"id":"1002","type":"Chocolate"}]},"topping":[{"id":"5001","type":"None"},{"id":"5002","type":"Glazed"},{"id":"5003","type":"Chocolate"},{"id":"5004","type":"Maple"}]}]'

try:
    #Execute query create table product
    cursor.execute(create_table)

    # Execute query sql to insert data json to table product in postgres database
    insert_query = "insert into product select * from json_populate_recordset (NULL::product, '"+data_json+"')"
    cursor.execute(insert_query)
    print("insert data data to table product succes!")
except (Exception, psycopg2.Error) as error:
    print("Error while execute query ", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")