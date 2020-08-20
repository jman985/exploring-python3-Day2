import os
import psycopg2
import requests
from flask import Flask, jsonify

# jsonify functions basically like json stringify, handling the responses from cursor


db = "dbname=%s host=%s " % ('pet-hotel', 'localhost')
schema = "schema.sql"
conn = psycopg2.connect(db)
cur = conn.cursor()

# Psycopg start  <------------ DO NOT CHANGE
# Test db connection
try:
    connection = psycopg2.connect(host = "localhost",
                                  database = "pet-hotel")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

            # Connect to an existing database
#>>> conn = psycopg2.connect("dbname=test user=postgres")
# Psycopg End <------------ END DO NOT CHANGE

# create app
def create_app(test_config=None):
    # configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        )
    # from . import db
    # db.init_app(app)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # GET ROUTES - JOSH
    @app.route('/pets', methods=['GET'])
    def getpets():
        cur.execute("SELECT * FROM pet;")
        print("Selecting rows from mobile table using cursor.fetchall")
        pets = cur.fetchall() 
        return "data from pets table is {}".format(pets)
        
    @app.route('/owners', methods=['GET'])
    def getowners():
        cur.execute("SELECT * FROM owner;")
        print("Selecting rows from mobile table using cursor.fetchall")
        owners = cur.fetchall() 
        return "data from pets table is {}".format(owners)

        # POST ROUTE - BRUNO


        # PUT ROUTE - AMIR


        # DELETE ROUTE - MASE
    
    return app