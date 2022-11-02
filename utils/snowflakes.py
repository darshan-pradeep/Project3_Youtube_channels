from helpers import snowflakes_connection
from helpers import video_authors_list
import os

    

def main():
    ctx,cs=snowflakes_connection.main()
    # cs.close()
    # ctx.close()
    return ctx,cs
    
    
    