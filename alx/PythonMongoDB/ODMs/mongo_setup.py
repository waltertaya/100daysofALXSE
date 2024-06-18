from mongoengine import connect

import os
from dotenv import load_dotenv

load_dotenv()

def global_init():
    connection_string = "mongodb+srv://${dbUsername}:${dbPassword}@waltertayadb.y2nbk2w.mongodb.net/test?retryWrites=true&w=majority"

    dbUsername = os.getenv('DB_USERNAME')
    dbPassword = os.getenv('DB_PASSWORD')

    connect(host=connection_string.replace("${dbUsername}", dbUsername).replace("${dbPassword}", dbPassword))
