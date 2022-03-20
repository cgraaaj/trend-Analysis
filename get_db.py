import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database():

    MONGO_PASS = os.environ.get("MONGO_PASS")
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://velan_mongodb:{MONGO_PASS}@cluster0.64cqd.mongodb.net/tradeStrategies?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['tradeStrategies']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    db = get_database()