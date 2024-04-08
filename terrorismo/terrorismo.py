"""
with open(self.arquivo, newline='') as csvfile: # Esta linha abre o arquivo especificado pelo 
nome de arquivo (self.arquivo)


O argumento newline='' é usado para garantir que as linhas do arquivo CSV sejam lidas corretamente, 
independentemente do sistema operacional (Windows, Linux,)

o módulo csv.DictReader, que lê o arquivo CSV e retorna um dicionário para cada linha, onde as 
chaves são os nomes da colunas
"""

import csv

class AtentadosTerroristas:
    def __init__(self,arquivo):
        self.arquivo = arquivo

    
    # Função que recebe o arquivo CSV a ser normalizado
    def ler_arquivo(self):
        with open(self.arquivo, newline='') as csvfile:
                    arquivo_csv = csv.reader(csvfile, delimiter=',')
                    linhas = list(arquivo_csv) # Lê todas as linhas do arquivo
                    #for linha in arquivo_csv:
                         #print(linha)

        # Percorre as linhas do arquivo para procurar células vazias
        for linha in linhas:
            for i, valor in enumerate(linha):
                if not valor.strip():  # Se a célula estiver completamente vazia
                    linha[i] = '0'

        # Escreve as linhas atualizadas em um novo arquivo CSV
        with open('resultado.csv', 'w', newline='') as arquivo_saida:
            arquivo_csv = csv.writer(arquivo_saida)
            arquivo_csv.writerows(linhas)
    
    
    # Função que recebe o arquivo CSV normalizado
    def ler_arquivo_normalizado(self):

        with open(self.arquivo, newline='') as csvfile:
                    arquivo_csv = csv.DictReader(csvfile, delimiter=',')
                    return list(arquivo_csv)
                    #for linha in arquivo_csv:
                         #print(linha)

    def atentado_maior_numero_de_mortes(self):
        dados = self.ler_arquivo_normalizado() # Chama a funçaõ ler_arquivo(self)
        maior_numero_mortes = 0
        pais_maior_numero_mortes = ""

        for linha in dados:
            numero_mortes = int(linha['Number Killed']) # Armazena o valor do número de mortes

            if numero_mortes > maior_numero_mortes:
                maior_numero_mortes = numero_mortes
                pais_maior_numero_mortes = linha['Country'] # Armazena nome da cidade com maior número de feridos ('country')
        
        return pais_maior_numero_mortes, maior_numero_mortes
    
    def atentado_maior_numero_de_feridos(self):
         dados = self.ler_arquivo_normalizado() # Chama a função ler_arquivo(self)
         maior_numero_feridos = 0
         pais_maior_numero_feridos = ""

         for linha in dados:
            numero_feridos = int(linha['Number Injured']) # Armazena o valor do número de feridos

            if numero_feridos > maior_numero_feridos:
                 maior_numero_feridos = numero_feridos
                 pais_maior_numero_feridos = linha['Country']

         return pais_maior_numero_feridos, maior_numero_feridos




dados = AtentadosTerroristas('terrorismo.csv')
#print(terror.ler_arquivo())
normalizar_dados = dados.ler_arquivo()

dados_normalizados = AtentadosTerroristas('resultado.csv')

atentado_com_mais_mortes = dados_normalizados.atentado_maior_numero_de_mortes()
print(f'Relatório: País do Atentado com mais morte -->', atentado_com_mais_mortes)

atentado_com_mais_feridos = dados_normalizados.atentado_maior_numero_de_feridos()
print(f'Relatório: País do Atentado com mais feridos -->', atentado_com_mais_feridos)




