import pandas as pd

import sqlite3
import uuid

excel_file_path = 'MOCK_DATA.xlsx'
df = pd.read_excel(excel_file_path)
df['UniqueID'] = [str(uuid.uuid4())for _ in range(len(df))]
conn = sqlite3.connect('Users.sqlite3')

table_name = 'users'
sxema = '''
    CREATE TABLE IF NOT EXISTS user(
        UniqueID TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT,
        ip_adress TEXT,
        country TEXT
    );

'''
conn.execute(sxema)
df.to_sql(table_name,conn, if_exists=r'replace', index=False)


conn.commit()
conn.close()
