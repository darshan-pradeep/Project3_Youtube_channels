from helpers import mongo_connection
from helpers import comments_reader



def main(video_id):
    client=mongo_connection.mongo_connector()
    final_comments=comments_reader.mongo_read(client,video_id)
    return final_comments