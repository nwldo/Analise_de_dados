"""
with open(self.arquivo, newline='') as csvfile: # Esta linha abre o arquivo especificado pelo 
nome de arquivo (self.arquivo)


O argumento newline='' é usado para garantir que as linhas do arquivo CSV sejam lidas corretamente, 
independentemente do sistema operacional (Windows, Linux,)

o módulo csv.DictReader, que lê o arquivo CSV e retorna um dicionário para cada linha, onde as 
chaves são os nomes da colunas
"""

import csv

class Drinks:
    def __init__(self,arquivo) -> None:
        self.arquivo = arquivo

    def ler_arquivo(self):
        with open(self.arquivo, newline='') as csvfile:
                    arquivo_csv = csv.DictReader(csvfile, delimiter=',')
                    #return list(arquivo_csv)
                    for linha in arquivo_csv:
                         print(linha)


    def pais_maior_consumo_de_cerveja(self):
        dados = self.ler_arquivo() # Chama a funçaõ ler_arquivo(self) que retorna um dicionário
        maior_consumo = 0
        pais_maior_consumo = ""

        for linha in dados:
            consumo = float(linha['beer_servings']) # Armazena o valor da coluna ('beer_servings') --> consumo de cerveja

            if consumo > maior_consumo:
                maior_consumo = consumo
                pais_maior_consumo = linha['country'] # Armazena nome da cidade com maior consumo ('country')
        
        return pais_maior_consumo
    
    def bebida_mais_consumida(self):
        dados = self.ler_arquivo()
        consumo_cerveja = 0
        consumo_destiladas = 0
        consumo_vinhos = 0
        maior_consumo = 0
        bebida_maior_consumo = ''

        for linha in dados:
              cerveja = float(linha['beer_servings'])
              destiladas = float(linha['spirit_servings'])
              vinhos = float(linha['wine_servings'])

              consumo_cerveja += cerveja
              consumo_destiladas += destiladas
              consumo_vinhos += vinhos

        maior_consumo = consumo_cerveja

        if consumo_destiladas > maior_consumo:
            if consumo_destiladas > consumo_vinhos:
                bebida_maior_consumo = 'spirit_servings'
                return consumo_destiladas
        elif consumo_vinhos > maior_consumo:
            if consumo_vinhos > consumo_destiladas:
                bebida_maior_consumo = 'wine_servings'
                return consumo_vinhos
        else:
            bebida_maior_consumo = 'beer_servings'
            return maior_consumo, bebida_maior_consumo




drink = Drinks('drinks.csv')

#pais_com_maior_consumo = drink.pais_maior_consumo_de_cerveja()
#bebida_com_maior_consumo = drink.bebida_mais_consumida()

#print(pais_com_maior_consumo)
#print(bebida_com_maior_consumo)

print(drink.ler_arquivo())
