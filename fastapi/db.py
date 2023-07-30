import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
connection_string = os.getenv("DATABASE_CONNECTION")



client = MongoClient(connection_string)

database = client["Hero"]
student_collection = database["studentusers"]
print(student_collection)