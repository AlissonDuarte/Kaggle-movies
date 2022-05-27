import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mysql.connector
from collections import Counter


# Conexão com o banco de dados
con = mysql.connector.connect(host='35.199.127.241',
                              db='looqbox_challenge',
                              user='looqbox-challenge',
                              password='looq-challenge')

#Cria o cursor que irá receber a querry e executa-la posteriormente
cursor = con.cursor()
querry = 'Select* from IMDB_movies'
cursor.execute(querry)
dframe = cursor.fetchall() #Retorna em formato de array os dados coletados
tabela = pd.DataFrame(data=dframe, columns=['Id', 'Title', 'Genre', 'Director',
                                        'Actors', 'Year', 'Runtime', 'Rating', 'Votes',
                                        'RevenueMillions', 'Metascore'])

#Dimensões da tabela
LinhaXcoluna = tabela.shape
#print(LinhaXcoluna)


#Tratar valores faltantes
null = tabela.isnull().sum()
#print(null)


#Substituindo valores nulos pela média
tabela['RevenueMillions'] = tabela['RevenueMillions'].astype('float64')
mediaRevenue = tabela['RevenueMillions'].mean()
tabela['RevenueMillions'].fillna(mediaRevenue, inplace=True)


tabela['Metascore'] = tabela['Metascore'].apply(lambda x: str(x).replace(",", "."))
tabela['Metascore'] = tabela['Metascore'].astype('float64')
mediaMetascore = tabela['Metascore'].mean()
tabela['Metascore'].fillna(mediaMetascore, inplace=True)



#10 filmes com maior duração
runtime_10 = tabela['Runtime'].sort_values(ascending=False).head(10)
idFilme = [828, 88, 965, 311, 82, 267, 430, 75, 271, 36]

nameRuntime = tabela['Title'][idFilme]
# retorna uma coluna associando o título do filme com o indice automático do dataframe



sns.set_theme(style="dark")
"""grafico = sns.barplot(x=runtime_10, y=nameRuntime,palette="mako", saturation=.5)
plt.title("Filmes mais longos")
plt.xlabel('Runtime(Min)') #define nome do eixo x
plt.ylabel('Movie Name')  # define nome do eixo y
#print(plt.show())
"""

"""#Filmes lançados por ano
filmes_ano = tabela['Year']
sns.countplot(x=tabela['Year'],data=filmes_ano, palette='flare')
plt.title("Filmes por ano")
plt.xlabel('Year')
plt.ylabel('Count')
print(plt.show())
"""


#Manipulando lista Genre
generos1 = []

#Retorna cada linha da coluna Genre como um array e os armazena-os dentro de uma lista
for valor in tabela['Genre']:
    generos1.append(valor.split(','))

generos = []
for gen in generos1:
    for gene in gen:  #itera sobre cada vetor dentro dos array's iterados no 'for' anterior
        generos.append(gene)  #Anexa cada vetor iterado anteriormente em uma nova lista

#Conta a quantidade de cada vetor na lista e transforma esses dados em um dict
num_generos = dict(Counter(generos).items())
#print(num_generos)
keys = sorted(num_generos, key = num_generos.get, reverse=False) #Organiza as chaves pelos valores em ordem crescente
values = [num_generos[x] for x in keys ] #armazena os valores do dict em uma lista


"""seaborn.lineplot(x=keys, y=values, data=num_generos)
plt.xticks(rotation=60)
plt.title('Frequência por gênero')
plt.xlabel('Gengers')
plt.ylabel('Count')
sns.set(rc={'figure.figsize':(10,5)})
plt.plot()
print(plt.show())
"""



"""#Mapa de correlações, para enxergar pontos de mineração e extrair possíveis informações
#sobre correlações e demais insights"
sns.heatmap(tabela.corr(), cmap='BrBG')
plt.title('Matriz de correlação')
print(plt.show())"""


"""receita = tabela['RevenueMillions']
votos = tabela['Votes']
sns.scatterplot(x= receita, y=votos, alpha=.5, palette="flare", hue=votos)
plt.xticks(rotation=60)
plt.plot()
print(plt.show())"""
