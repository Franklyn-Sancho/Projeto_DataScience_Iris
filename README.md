<h1 align="center">Projeto em DataScience</h1>

<p>Neste projeto, iremos analisar um estudo, neste caso, um banco de dados sobre as flores iris. No conjunto de dados temos três espécies de iris (Iris setosa, iris virgínica e iris iris versicolor). Temos 150 registros com 5  atributos cada: classe e o comprimento e a largura das sépalas e pétalas, em centímetros (formando neste caso quatro atributos).</p>
   <p> Para analisar os dados, trabalhei com as ferramentas do google colab, o que facilitou, e muito, a minha vida, economizando o tempo de instação das dependencias e ferramentas no sistema. Mas caso você queira fazer da forma tradicional, diretamente em seu computador, não se preocupe, explicarei todos os passos. Para inicio de conversa, precisamos instalar o Python 3.5+. Alias, caso seu sistema operacional seja o Windows e você queira facilitadade, sem ter de recorrer as ferramentas da google, aconselho instalar as ferramentas Anaconda (Vem com tudo instalado). Mas vamos prosseguir com o nosso projeto. Agora com o Python devidamente instalado em nosso sistema, vamos a instalação de nossas dependências. Listarei cada uma delas aqui, quanto a instalações, para o artigo não ficar muito longo, basta pesquisar sobre a biblioteca e o modo de instalação para seu sistema operacional. </p>
   
   ## Lista de bibliotecas:
   * Scipy
   * Matplotlib
   * numPy
   * pandas 
   * sklearn
   * seaborn
   
 <p> Agora que estamos com nossa área de trabalho pronta, podemos iniciar o nosso projeto de analise de dados. Por amar muito a língua portuguesa, tentarei ao máximo usar os termos na nossa língua materna, talvez isso deixe tudo ainda mais claro na aplicação. Bem, neste momento, você só precisa buscar no repositório um arquivo em python, clicar nele e analisar o código comigo. Caso não domine python, não se assuste, todo o código estará comentado e explicado. </p>
 <h3 align="center">**Abra o arquivo AnaliseCode.py que está aqui mesmo no repositório**</h3>

### 1. Resultados e demonstrações:

**1.2. Dimensão da tabela:**<br>
Esta função retorna a dimensão da tabela. Neste caso retornaria: (150, 5) = 150 linhas e 5 colunas;


 ```python
 print(dataset.shape)
 ```
 
 
**1.3. Tabela de resumo estatístico:**<br>
Esta função retornará uma tabela com um resumo estatístico da nossa amostragem. Logo abaixo teremos uma imagem de exemplo:

```python
print(dataset.describe())
```
Exemplo da tabela:

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/tabelaestatistica.png"></img>

Você já teve a oportunidade de estudar estatística? Acredite, é simplesmente maravilhoso o quanto de informações podemos obter com algumas formulas. No nosso caso, funções. 
 * **count**: é a contagem, total da amostragem, 150, correto. 
 * **mean**: Média total. Antes de qualquer analise, precisamos saber que todos os dados foram calculados e armazenados em centimetros. Agora sim, vamos ao que interessa. As sépalas tem em média 5.8cm de comprimento e 3cm de largura; já as pétalas tem em média 3.75cm de comprimento e 1.20cm de largura. 
 * **std**: desvio padrão - "Colocarei a explicação em breve" :warning:
 * **min**: é o valor mínimo encontrado. 
 * **25%**: aqui começamos o assunto sobre quartis. 25% seria o 1ª quartil, ou 1/4 do valor. Significa que 25% do total da amostragem tem valores abaixo ou igual a esses resultados. Por exemplo: 25% das sépalas analisadas tem valores abaixo ou iguais a 5.1cm de comprimento; 25% das pétalas analisadas tem valores abaixo ou igual a 1.6cm de largura; e por aí vai...
 * **50%**: segundo quartil. 25%, 1/2 e também a mediana do total. Segue a mesma lógica dos 25%. Ex: 50% das sépalas analisadas tem valores menores ou iguais a 5.8cm de comprimento.
 * **75%**: 3ª quartil. 75% ou 3/4 do valor total. Segue a mesma lógica do primeiro e segundo quartil. 75% dos dados tem valores menores ou iguais a esses resultados
 * **max**: valor máximo encontrado

**1.4. Listando os primeiros registros (quantos quisermos)**<br>
esta função lista os 10 primeiros itens do seu dataset. Caso queira trazer um número especifico, basta mudar o 10 pelo numero desejado. 20 traz os 20 primeiros; 15 traz os 15; 30 traz os 30 e assim sucessivamente. 

```Python 
print(dataset.head(10))
```

### 2. Agora vamos aos nossos gráficos e uma breve explicação

 <h5 align="center"> Quando trabalhamos com ciência de dados, é natural termos de lidar com diversos tipos de dados diferentes, por isso é necessário facilitar ao máximo a nossa compreensão. Quando trabalhamos com python, somos abençoados por dois motivos, primeiro pela facilidade dos códigos e segundo por todas as bibliotecas que a tecnologia é capaz de nos proporcionar. Também podemos trabalhar com gráficos, o que facilita, e muito, a nossa visualização dos dados, muitas vezes gigantescos. O Matplotlib é o protagonista desse capítulo </h5>

**2.1. Grafico bigode ou diagrama de caixa**

<p> Quando estamos acostumados a trabalhar com histograma, é normal que a gente se assuste com essa belezura aí. Mas calma, ele é muito simples e intuitivo. Tudo melhora na nossa vida depois que aprendemos a interpretá-lo. Dexarei o link de um artigo do medium explicando como trabalhar com esse diagrama. Pra que possamos plotar ele, basta executar essa função logo abaixo  </p>

```python
dataset.plot(kind=’box’, subplots=True, layout=(2,2)
,sharex=False, sharey=False)
plt.show()
```
Exemplo do nosso gráfico: 

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/graficobigode.png"></img>

<p> Vamos a interpretação desse gráfico no contexto da análise? Para que a explicação se torne ainda mais simples, eu aconselho vocês a manterem a tabela de resumo estatístico por perto. A primeira imagem que nós temos, é um gráfico sobre o comprimento das sépalas (Sepal_lenght). Se vocês repararem no eixo X, verão que ele vai apenas do número 5 ao 8. Existem dois tráços, cada um numa extremidade, correto? o que está abaixo do número cinco é o **mínimo** e o que está na parte superior, próximo ao número 8, é o valor *máximo*. Para confirmar, vamos voltar lá na nossa tabela. Quais são os valores máximos e minimos que aparecem? 4.3cm e 7.9cm, né? Os traços correspondem ao valor descrito?   </p>
<p> Agora que descobrimos onde estão os valores máximos e mínimos, sabemos que todo o universo da amostragem está entre esses dois traços. O retângulo no centro é a 'amplitude interquartil'. Esta primeira aresta inferior, próxima ao número cinco é o 1ª quartil, que equivale a 5.10cm; a linha verde no centro do retângulo é a nossa mediana, que equivale a 5.8cm; a última aresta, acima do número 6 é o nosso 3ª quartil, 75%. E aí, os valores correspondem? viu como é simples </p>
<p> Vocês repararam as bolinhas desenhadas no segundo gráfico? lhes apresento os valores atípicos da amostragem.    </p>

#### Este é o link sobre a interpretação do gráfico: https://medium.com/@claudio.siervi/interpretando-o-diagrama-de-caixa-boxplot-1876b7c099af

**2.2. O famoso Histograma**

Podemos respirar em paz agora, pois estamos na presença de algo que conhecemos. Obrigado, python, por pensar em todos aqueles que estão aprendemos e só sabem traduzir histogramas :heart:. Meu pequeno Padawan, adianto que não teremos todas as respostas apenas com esse gráfico. Existem outras formas bem mais intuítiva de gerar informações de forma precisa. Mas calma que todos serão explicados. Bem, sem mais delongas, para gerar esse lindo histograma, basta:

```python
dataset.hist()
plt.show()
```
Simples, não? Vamos a sua imagem. 

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/histogramairis.png">

**2.3. Gráficos de linha**

O gráfico de linha é um dos mais importantes na ciência de dados. Antes da gente trabalhar com ele, primeiro é necessário instalar e importar a ferramenta Seaborn. 

```python
import seaborn as sns

sns.lineplot('petal-length', 'petal-width',
             hue='class', style='class', data=dataset)
```
Agora olha que lindão vai ficar:

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/lineplot.png">

**2.4. gráfico lmplot**

Este é um gráfico de dispersão com linhas 

```python
import seaborn as sns

sns.lmplot('petal-length', 'petal-width',
           hue='class', data=dataset)
```
Vamos as Ibagens (meme)

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/lmplot.png">

**2.5 Gráfico pairplot**

Um dos melhores comandos que existem, uma união de diversos gráficos para que a gente possa analisar por completo todos os dados de forma separada. Simplesmente incrível e o mais lindo também. Ciência de dados é isso, ter os dados e da forma mais simples possível :heart:

```python
import seaborn as sns

sns.pairplot(dataset, hue='classe')
```
Vamos as imagens desse monumento: aproveite :heart:

<img src="https://github.com/Franklyn-Sancho/Projeto_DataScience_Iris/blob/main/paitplot.png">
