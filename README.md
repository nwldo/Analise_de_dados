# Topicos Especiais em Programação

###  Início da resolução das listas de exercícios sobre introdução a ciência de dados e revisão de estruturas de dados em python

### 👨‍💻️ Tecnologias e Ferramentas
Para realizar as atividades da análise de dados poderá usa:
* linguagens: Python e R
* Jupyter notebook
* visual studio code
* colab python

---
## 👨‍💻️ Tecnologias Utilizadas
As atividades foram criadas utilizando as tecnologias:
- [Jupyter Notebok](https://jupyter.org/install)
- [Python](https://www.python.org/doc/)
- [Pandas](https://pypi.org/project/pandas/)
- [Pandas](https://numpy.org/install/)

---
## 📦️ Como instalar as tecnoligias
Pelo prompt de comando digite:
## No Windows
```bash
  # [Baixe e instale o Python](https://www.python.org/downloads/)
  # pip install pandas
  # pip install numpy
  # pip install notebook
  # pip install ipython
  # pip install matplotlib
 
```
---

## 📦️ Como rodar o projeto
```bash
  # Crie uma pasta no seu computador
  # Selecione o endereço da pasta e digite "cmd"
  # No prompt que se abre digite "jupyter notebook"
  # Irá ser aberto o navegador padrão com o endereço localhos:porta/tree
  # Para criar um arquivo clique em "New" será criado um Untitled depois renomeio-o
  # Digite o código na célula e para criar mais células clique no simbolo "+"

  ```

---
<img src="https://github.com/Nwldo/Analise_de_dados/blob/main/img/jupyter_1.png">
<img src="https://github.com/Nwldo/Analise_de_dados/blob/main/img/jupyter_2.png">

# Análise Descritiva de Dados com Pandas

## A função info()
A função info() no Pandas exibe informações detalhadas sobre um dataframe, incluindo número de linhas (entradas), tipo de dados (dtypes) de cada coluna, quantidade de dados não nulos em cada coluna e uso de memória. Isso permite rapidamente verificar se existem dados nulos, entender quais tipos de dados estão presentes (strings, numéricos, datas etc.) e identificar problemas como dados inconsistentes.

* Exibição de informações detalhadas sobre um dataframe, incluindo número de linhas, tipo de dados de cada coluna, quantidade de dados não nulos em cada coluna e uso de memória
* Rápida verificação de dados nulos e identificação de problemas como dados inconsistentes

## A função describe()
A função describe() é uma ferramenta valiosa para obter estatísticas descritivas sobre colunas numéricas em um dataframe. Ela fornece informações importantes sobre a distribuição dos dados, permitindo insights valiosos sem a necessidade de visualizações complexas.

* A função describe() exibe estatísticas descritivas, como count, mean, std, min, 25%, 50%, 75% e max, sobre colunas numéricas em um dataframe.

## Entendendo Média e Desvio Padrão
Duas das estatísticas mais importantes retornadas pela função describe() são a média e o desvio padrão. Compreender corretamente essas métricas é fundamental para uma análise precisa dos dados.

* A média indica o ‘centro’ dos dados, representando o equilíbrio entre valores extremos.
* O desvio padrão mede a dispersão dos valores em relação à média, indicando a variabilidade dos dados.
* Uma alta variabilidade, indicada por um desvio padrão elevado, sugere uma ampla gama de valores, desde extremamente pequenos até extremamente grandes.
* Por outro lado, um baixo desvio padrão indica que a maioria dos valores está concentrada próxima à média, representando menor variabilidade.

## Valor Mínimo e Valor Máximo
Além da média e do desvio padrão, as métricas de valor mínimo e valor máximo também são essenciais para compreender a distribuição dos dados.

* O valor mínimo representa o menor valor presente nos dados, enquanto o valor máximo representa o maior valor.
