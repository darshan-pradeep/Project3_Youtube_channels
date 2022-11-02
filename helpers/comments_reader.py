import pymongo
import os

def mongo_read(client,video_id):   
    parent_comments_coll=os.environ['MONGODB_PARENT_COMMENTS_COLL']
    reply_comments_coll=os.environ['MONGODB_REPLY_COMMENTS_COLL']
    db_name=os.environ['MONGODB_DB_NAME']
    
    db = client.test
    
    database=client[db_name]
    collection1=database[parent_comments_coll]
    collection2=database[reply_comments_coll]
    vidid=video_id
    parent_comment_ids=[]
    parent_comments=collection1.find({'video_id':vidid})
    final=[]
    for parent_comment in parent_comments:
        d={}
        d['parent_user_name']=parent_comment['parent_user_name']
        d['parent_comment']=parent_comment['parent_comment']
        reply=[]
        reply_comments=collection2.find({'reply_parent_id':parent_comment['parent_comment_id']})
        reply_comments_count=collection2.count_documents({'reply_parent_id':parent_comment['parent_comment_id']})
        if reply_comments_count==0:
            reply.append('No replies yet !!')
        else:
            for reply_comment in reply_comments.sort('reply_id',pymongo.ASCENDING): #shows first reply
                #first and latest reply last 
                re={}
                re['reply_user_name']=reply_comment['reply_user_name']
                re['reply_comment']=reply_comment['reply_text']
                reply.append(re)
        d['replies']=reply
        final.append(d)
    return final


    
    