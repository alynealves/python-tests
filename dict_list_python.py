    
def cad_lista_fixa(qtd_pessoas, lista_campos):
      pessoas = []
      
      qtd_campos = int(input('Digite a quantidade de dados a serem preenchidos: '))#2

      print(' - DEFINIÇÃO DOS DADOS - ')
      for c in range(qtd_campos):
            lista_campos.append(input('Digite o dado a ser armazenado: '))#nome #idade

      for i in range(qtd_pessoas):
        dados = {}
        print(' - PREENCHIMENTO DOS DADOS - ')
        for campo in lista_campos:
                if campo == 'idade':
                    dados[campo] = int(input(f'Digite {campo} da {i+1} pessoa: '))
                else:
                    dados[campo] = input(f'Digite {campo} da {i+1} pessoa: ')
        pessoas.append(dados.copy())
      
      return pessoas
     
def cad_lista_dinamica(qtd_pessoas):
     pessoas = []
     
     for i in range(qtd_pessoas):
          dados = {}
          lista_campos = []
          print(' - QUANTIDADE DE DADOS - ')
          qtd_campos = int(input(f'Quantos dados irá preencher para a {i+1} pessoa? '))

          print(' - DEFINIÇÃO DOS DADOS - ')
          for c in range(qtd_campos):
                lista_campos.append(input('Digite o dado a ser armazenado: '))

          print(' - PREENCHIMENTO DOS DADOS - ')
          for campo in lista_campos:
                if campo == 'idade':
                    dados[campo] = int(input(f'Digite {campo} da pessoa: '))
                else:
                    dados[campo] = input(f'Digite {campo} da pessoa: ')

          pessoas.append(dados.copy())
     return pessoas

lista_campos = []
pessoas = []
contador = 0

print(' - CADASTRAMENTO DE PESSOAS - ')

qtd_pessoas = int(input('Quantas pessoas você deseja cadastrar? '))#2
check = input('A quantida de dados a ser preenchida é fixa ou dinâmica? ')#fixa

if check == 'fixa':
    pessoas = cad_lista_fixa(qtd_pessoas, lista_campos)
elif check == 'dinamico':
    pessoas = cad_lista_dinamica(qtd_pessoas)
          
for i in pessoas:
        contador += 1
        print(f'Os dados preenchidos da {contador} pessoa são: ')
        for c, v in i.items():
            print(f'{c} : {v}')

print(f'Os dados organizados em ordem alfabética: ')
pessoas = sorted(pessoas, key=lambda x: x['nome'])
for i in pessoas: 
        for c, v in i.items():
            print(f'{c} : {v}')

print(f'Os dados organizados do mais velho pro mais jovem: ')
pessoas = sorted(pessoas, key=lambda x: x['idade'], reverse=True) 
for i in pessoas:
     for c, v in i.items():
            print(f'{c} : {v}')