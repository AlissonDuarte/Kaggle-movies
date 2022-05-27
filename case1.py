import pandas as pd
import mysql.connector


#Cria conexão com o banco de dados
con = mysql.connector.connect(host='35.199.127.241',
                              db='looqbox_challenge',
                              user='looqbox-challenge',
                              password='looq-challenge')


#Checa conexão e informa a versão o banco de dados
if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor", db_info)

def my_data(store_code, product_code, date):
    """Os primeiros parâmetros devem ser do tipo Int,
    já a data deve ser do tipo String e estar no formato 'yyyy-mm-dd'"""
    store_code = store_code
    product_code = product_code
    date = date
    cursor = con.cursor()
    buscador = f'select * from data_product_sales where product_code= "{product_code}" and store_code = "{store_code}" and date = "{date}" limit 1'
    cursor.execute(buscador)
    linhas = cursor.fetchall()
    df = pd.DataFrame(linhas, columns=['store_code', 'product_code', 'date', 'sales_value', 'sales_qty'])
    print(df)
    cursor.close()
    con.close()

my_data(1, 18, '2019-01-03')