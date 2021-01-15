# Vamos começar importando nossas dependências 
# explicarei ao longo da analise suas funções

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Agora com todas as bibliotecas importadas
# Podemos carregar o nosso banco de dados. 
# Na Url temos o link do dataset e no objeto 'nomes' listamos os atributos 
# Carregamos o dataset com a ferramenta pandas, no modo leitura e seu tipo de arquivo 'csv'

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master
/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# Depois de carregar o dataset, basta chamar os dados desejados com a função print. 

print(dataset.shape) #nesta função teremos a  dimensão do nosso dataset (150, 50) = 150 itens e 5 atributos

print(dataset.head(10)) # Esta função listará os 10 primeiros dados do dataset, se mudar 10, por 20, serão os 20 dados

print(dataset.describe()) # Tabela de resumo estatístico: média, desvio padrão, quartil e percentil

print(dataset.groupby('class').size()) # distribuição das classes, numero total em cada 

# Agora iremos trabalhar com linda depêndencia de gráficos chamada matplotlib <3

# Podemos começar com o gráfico de bigode 

dataset.plot(kind=’box’, subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# Nosso famoso histograma

dataset.hist()
plt.show()

