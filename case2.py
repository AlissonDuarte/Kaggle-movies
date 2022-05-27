import mysql.connector
import pandas as pd

con = mysql.connector.connect(host='35.199.127.241',
                              db='looqbox_challenge',
                              user='looqbox-challenge',
                              password='looq-challenge')

#Cria o 'cursor' que irá armazenar e posteriormente executar a querry no banco de dados
cursor = con.cursor()
querry ="""SELECT
      STORE_CODE,
      STORE_NAME,
      START_DATE,
      END_DATE,
      BUSINESS_NAME,
      BUSINESS_CODE
FROM data_store_cad"""

querry_2 = """SELECT
        STORE_CODE,
        DATE,
        SALES_VALUE,
        SALES_QTY
FROM data_store_sales
WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
"""


cursor.execute(querry)
#fetchall usado para que os colhidos pela querry sejam sejam lidos
querry1 = cursor.fetchall()

#Gera um dataframe com os dados da querry passada
df1 = pd.DataFrame(data=querry1, columns=['STORE_CODE',
                                          'STORE_NAME',
                                          'START_DATE',
                                          'END_DATE',
                                          'BUSINESS_NAME',
                                          'BUSINESS_CODE'])


cursor.execute(querry_2)
querry2 = cursor.fetchall()

df2 = pd.DataFrame(data = querry2, columns=['STORE_CODE',
                                            'DATE',
                                            'SALES_VALUE',
                                            'SALES_QTY'])



#Método merge(), combina dois dataframes diferentes, o parâmetro 'how=' seleciona a interseção entre os dataframes
#sendo o parâmetro 'on=' o meio de ligação entre eles, agindo como uma chave primária e chave estrangeira

df3 = pd.merge(df1, df2, how = 'inner', on='STORE_CODE')

df = df3[df3['DATE'].isin(pd.date_range('2019-10-01', '2019-12-31'))]

print(df.to_string()) #método 'to_string' usado para que o pycharm não ocultasse as linhas retornadas. Dispensável
