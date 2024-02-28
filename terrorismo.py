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
    def __init__(self,arquivo) -> None:
        self.arquivo = arquivo

    def ler_arquivo(self):
        with open(self.arquivo, newline='') as csvfile:
                    arquivo_csv = csv.DictReader(csvfile, delimiter=',')
                    return list(arquivo_csv)


    def atentado_maior_numero_de_mortes(self):
        dados = self.ler_arquivo() # Chama a funçaõ ler_arquivo(self) que retorna um dicionário
        maior_numero_mortes = 0
        pais_maior_numero_mortes = ""

        for linha in dados:
            quantidade = int(linha['Number Killed']) # Armazena o valor do número de mortes

            if quantidade > maior_numero_mortes:
                maior_numero_mortes = quantidade
                pais_maior_numero_mortes = linha['Country'] # Armazena nome da cidade com maior consumo ('country')
        
        return pais_maior_numero_mortes
    




terror = AtentadosTerroristas('terrorismo.csv')
atentado_com_mais_mortes = terror.atentado_maior_numero_de_mortes()
print(atentado_com_mais_mortes)

