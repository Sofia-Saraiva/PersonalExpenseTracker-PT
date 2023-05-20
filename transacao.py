dados = []

# tratar erro ,

# LER O ARQUIVO CSV E TRANSFORMA CADA LINHA EM UM DICIONÁRIO, ADICIONANDO NA LISTA DADOS
def arquivar():
  with open('transacoes.csv', 'r') as arquivo:
    for index, dado in enumerate(arquivo):
      dado = dado.rstrip('\n')
      colunas = dado.split(',')
      valor = float(colunas[2])
      dict = {
        "id": index + 1,
        "nome": colunas[0],
        "categoria": colunas[1],
        "valor": valor
      }
      dados.append(dict)

  return dados


def extrato():
  print("----------------------- EXTRATO -----------------------")
  print(f''.ljust(15), 'NOME'.ljust(15), 'CATEGORIA'.ljust(15), 'VALOR'.ljust(15))
  for dict in dados:
    for chave, valor in dict.items():
      valor = str(valor)
      print(valor.ljust(15), end=' ')
    print()


def filtrar():
  while True:
    try:
      categoria = input("Digite a categoria que deseja filtrar: ").upper()
      categoria_encontrada = False
      print("----------------------- EXTRATO -----------------------")
      print(f'ID'.ljust(15), 'NOME'.ljust(15), 'CATEGORIA'.ljust(15), 'VALOR'.ljust(15))
      for dict in dados:
        if categoria in dict['categoria']:
          categoria_encontrada = True
          for chave, valor in dict.items():
            valor = str(valor)
            print(valor.ljust(15), end=' ')
          print()   
      if not categoria_encontrada:
        raise ValueError
    except ValueError: 
      print("Categoria não encontrada.")
    else:
      break
    

def add():
  try:
    with open('transacoes.csv', 'a') as arquivo:
      nome, categoria, valor = input("Adicione uma transação: ").upper().split(',')
      arquivo.write(f'{nome},{categoria},{valor}\n')
  finally:
    print("Transação adicionada com sucesso!")
  

def atualizar():
  extrato()
  while True:
    id = int(input("Digite o ID da transação deseja alterar: "))
    id_encontrado = False
    try:
      for dict in dados:
        if id == dict['id']:
          id_encontrado = True
          atualizado = input("Digite os dados da transação: ").upper().split(',')
          dados[id-1] = {
            "id": id,
            "nome": atualizado[0],
            "categoria": atualizado[1],
            "valor": atualizado[2]
          }
      if not id_encontrado:
        raise ValueError
    except ValueError: 
      print("Transação não existe.")
    else:
      print("Transação atualizada com sucesso!")
      with open('transacoes.csv', 'w+') as arquivo:
        for dict in dados:
          arquivo.write(f"{dict['nome']},{dict['categoria']},{dict['valor']}\n")
      break



def deletar():
  extrato()
  while True:
    id = int(input("Digite o ID da transação que deseja deletar: "))
    id_encontrado = False
    try:
      for dict in dados:
        if id == dict['id']:
          id_encontrado = True
      if not id_encontrado:
        raise ValueError
      dados.pop(id - 1)
      with open('transacoes.csv', 'w+') as arquivo:
        for dict in dados:
          arquivo.write(f"{dict['nome']},{dict['categoria']},{dict['valor']}\n")
    except ValueError:
      print("Transação não existe.")
    else:
      print("Transação deletada com sucesso!")
      break
  

def budget():
  budget = float(input("Digite seu budget: "))
  total = 0
  for dict in dados:
    total += dict['valor']
  sobra = budget - total
  print(f"BUDGET".ljust(15), "GASTO".ljust(15), "POUPADO")
  print(str(budget).ljust(15), str(total).ljust(15), str(sobra).ljust(15))
  

