import os



def main(client,top_details):
    l=[]
    db_name=os.environ['MONGODB_DB_NAME']
    coll_name=os.environ['MONGODB_BASE64_COLL_NAME']
    database=client[db_name]
    collection=database[coll_name]
    print('Database and Collection for thumbnails accessed successfully')
    all_thumbnails=[]
    for item in top_details:
        obj=collection.find({'video_id':item[0]})
        for i in obj:
            l.append(i['base_64'])
    return l
