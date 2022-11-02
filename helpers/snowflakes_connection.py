import snowflake.connector
import os

def main():
    snowflakes_credentials={'account':os.environ['SNOWFLAKES_ACCOUNT'],
                        'user':os.environ['SNOWFLAKES_USER'],
                        'password':os.environ['SNOWFLAKES_PASSWORD'],
                        'database_name':os.environ['SNOWFLAKES_DATABASE'],
                        'schema_name':os.environ['SNOWFLAKES_SCHEMA'],
                        'warehouse_name':os.environ['SNOWFLAKES_WAREHOUSE']}

    ctx = snowflake.connector.connect(
            user=snowflakes_credentials['user'],
            password=snowflakes_credentials['password'],
            account=snowflakes_credentials['account'],
            warehouse=snowflakes_credentials['warehouse_name'],
            database=snowflakes_credentials['database_name'],
            schema=snowflakes_credentials['schema_name']
            )
    cs = ctx.cursor()
    print('Connection established successfully with Snowflakes')
    return ctx,cs
        
