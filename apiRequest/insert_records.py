import psycopg2
from api_request import fetchData

def connectToDb():
    print('Connecting to Postgres Database ...')

    try:
        conn = psycopg2.connect(
            host= 'db',
            port = 5432,
            dbname = 'db',
            user = 'admin',
            password='admin'
        )
        return conn
    
    except psycopg2.errors as e:
        print('Database Connection Failed : ',e)
        raise

def create_table(conn):
    print('Creating Table if not exist ...')
    try:
        cursor = conn.cursor()
        cursor.execute('''
            Create schema if not exists dev;
            create table if not exists dev.raw_weather_data(
                       id SERIAL PRIMARY KEY,
                       city TEXT,
                       temprature FLOAT,
                       weather_description TEXT,
                       wind_speed FLOAT,
                       time TIMESTAMP,
                       inserted_at TIMESTAMP DEFAULT Now(),
                       utc_offset TEXT);
        ''')
        conn.commit()
        print('Table was created successfully')
    except psycopg2.errors as e:
        print('Failed to create table : ',e)
        raise

def insert_data(conn,data):
    print('Inserting Weather data into raw_weather_data table ...')
    print(data)

    try:
        cursor = conn.cursor()
        cursor.execute('''
            Insert into dev.raw_weather_data(
                       city,
                       temprature,
                       weather_description,
                       wind_speed,
                       time,
                       inserted_at,
                       utc_offset) values (%s,%s,%s,%s,%s, Now(), %s)

        ''',(
            data['location']['name'],
            data['current']['temperature'],
            data['current']['weather_descriptions'][0],
            data['current']['wind_speed'],
            data['location']['localtime'],
            data['location']['utc_offset']
        ))
        conn.commit()
        print('Data Successfully Inserted')
    
    except psycopg2.errors as e:
        print('Error Inserting Data into the database : ',e)
        raise

def main():
    print('Initiating Steps to insert Data ...')
    try:
        data = fetchData()
        conn = connectToDb()
        create_table(conn)
        insert_data(conn,data)
    except psycopg2.errors as e:
        print('Error While Inserting Data : ',e)
    finally:
        if 'conn' in locals():
            conn.close()
            print('Database Connection Closed')