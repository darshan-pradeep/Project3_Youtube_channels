
def read_snowflakes(cs):
    authors_list=cs.execute('select distinct video_author,channel_logo from sql_table').fetchall()
    
    # print(authors_list)
    return authors_list