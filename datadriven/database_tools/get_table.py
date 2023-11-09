import os
import pandas as pd
from snowflake import connector

def get_table(schema, table, 
              select=None, where=None, 
              group_by=None, order_by=None, 
              limit=None, verbose=True):
    
    query = f"""
    select {'*' if select==None else f'{select}'}
    from DATADRIVEN.{schema}.{table}
    {'' if where==None else f'where {where}'}
    {'' if group_by==None else f'group by {group_by}'}
    {'' if order_by==None else f'order by {order_by}'}
    {'' if limit==None else f'limit {limit}'}
    """
    with connector.connect(
            user=os.getenv('SNOWFLAKE_USERNAME'),
            password=os.getenv('SNOWFLAKE_PASSWORD'),
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            warehouse='ADHOC') as conn:
        
        cursor = conn.cursor()
        cursor.execute(query)
        df = cursor.fetch_pandas_all()
    
    if verbose:
        print(f'Fetched data from {schema}.{table}!')
    else:
        pass

    return df