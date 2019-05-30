# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:40:19 2019

@author: jjirsa
"""

def ez_sql(server = 'server', database = 'data', username = 'user', driver= 'driver', table = 'table', rows = 'row'):
   
   import pandas as pd
   import pyodbc
   conn = pyodbc.connect(r'Driver={'+driver+'}; Server='+server+'; UID='+username+'; Database='+database+'; Trusted_Connection=yes;')
   cursor = conn.cursor()
   df = pd.read_sql_query('select top '+rows+' * from '+table+'', conn)
   return df
