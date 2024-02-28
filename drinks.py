import csv

class Drinks:
    def __init__(self,arquivo) -> None:
        self.arquivo = arquivo

    def ler_arquivo(self):
        with open(self.arquivo, newline='') as csvfile:
                    arquivo_csv = csv.DictReader(csvfile, delimiter=',')
                    return list(arquivo_csv)
                    

    def pais_maior_consumo_de_cerveja(self):
        dados = self.ler_arquivo()
        maior_consumo = 0
        pais_maior_consumo = ""

        for linha in dados:
            consumo = int(linha['beer_servings'])

            if consumo > maior_consumo:
                maior_consumo = consumo
                pais_maior_consumo = linha['country']
        
        return pais_maior_consumo




drink = Drinks('drinks.csv')

pais_com_maior_consumo = drink.pais_maior_consumo_de_cerveja()

print(pais_com_maior_consumo)
