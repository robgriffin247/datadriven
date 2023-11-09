import pandas as pd 
from database_tools.get_table import get_table

tables = pd.DataFrame({
    'schema':['CORE', 'CORE', 'STAGING'],
    'table':['DIM_PEOPLE', 'OBT_EVALUATED_JOB_ADS', 'STG_ARBETSFORMEDLINGEN_SKILLS']})

for index, row in tables.iterrows():
    df = get_table(schema=f'{row.schema}', table=f'{row.table}')
    df.to_csv(f'datadriven/data/{row.schema}_{row.table}.csv')
