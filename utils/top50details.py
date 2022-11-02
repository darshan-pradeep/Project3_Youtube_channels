from helpers import mongo_connection
from helpers import base64_mongo

def top50_snowflakes(cs,author_name):
    query=f"SELECT * from sql_table where video_author='{author_name}'"
    top_details=cs.execute(query).fetchall()
    return top_details



def main(top_details):
    client=mongo_connection.mongo_connector()
    all_thumbnails=base64_mongo.main(client,top_details)
    return all_thumbnails
    



