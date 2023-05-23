# cada transação é um dicionário com 3 chaves(nome,categoria,valor) que fica armazenado na lista dados
dados = []


def criar_arquivo():
  arquivo = open('transacoes.csv', 'w')
    

def arquivar():
  """Ler o arquivo CSV e transforma cada linha em um dicionário que fica armazenado em uma lista"""
  with open('transacoes.csv', 'r') as arquivo:
    for index, dado in enumerate(arquivo):
      dado = dado.rstrip('\n')
      colunas = dado.split(',')
      valor = float(colunas[2])
      dict = {
        "id": index + 1,
        "nome": colunas[0].replace("*",","),
        "categoria": colunas[1],
        "valor": valor
      }
      dados.append(dict)

  return dados


def extrato():
  """Printa cada dicionário"""
  print("----------------------- EXTRATO -----------------------")
  print(f'ID'.ljust(15), 'NOME'.ljust(15), 'CATEGORIA'.ljust(15), 'VALOR'.ljust(15))
  for dict in dados:
    for chave, valor in dict.items():
      valor = str(valor)
      print(valor.ljust(15), end=' ')
    print()


def filtrar():
  """Filtra o dicionário de acordo com categoria. (Se não existir continua pedindo input do user)"""
  while True:
    try:
      categoria = input("Digite a categoria que deseja filtrar: ").title()
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
  """Adiciona uma transação"""
  try:
    with open('transacoes.csv', 'a') as arquivo:
      print("Adicione uma transação: ")
      nome = input("Nome: ").title()
      # tratar erro nome com ,
      if ',' in nome:
        nome = nome.replace(',','*')
      categoria = input("Categoria: ").title()
      valor = input("Valor: ")
      arquivo.write(f'{nome},{categoria},{valor}\n')
  finally:
    print("Transação adicionada com sucesso!")
  

def atualizar():
  """Atualiza os dados de uma transação. Se ID não existir continua pedindo input do user"""
  extrato()
  while True:
    id = int(input("Digite o ID da transação deseja alterar: "))
    id_encontrado = False
    try:
      for dict in dados:
        if id == dict['id']:
          id_encontrado = True
          print("Atualize uma transação: ")
          nome = input("Nome: ").title()
          categoria = input("Categoria: ").title()
          valor = input("Valor: ")
          dados[id-1] = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "valor": valor
          }

          with open('transacoes.csv', 'w') as arquivo:
            for dict in dados:
              # tratar erro nome com ,
              dict['nome'] = dict['nome'].replace(',','*')
              arquivo.write(f"{dict['nome']},{dict['categoria']},{dict['valor']}\n")
          break
      if not id_encontrado:
        raise ValueError
    except ValueError: 
      print("Transação não existe.")
    else:
      print("Transação atualizada com sucesso!")
      break


def deletar():
  """Deleta uma transação. Se ID não existir, continua pedindo input do user"""
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
      # tira a transação dos dados e reescreve o arquivo csv
      dados.pop(id - 1)
      with open('transacoes.csv', 'w') as arquivo:
        for dict in dados:
          # tratar erro nome com ,
          dict['nome'] = dict['nome'].replace(',','*')
          arquivo.write(f"{dict['nome']},{dict['categoria']},{dict['valor']}\n")
    except ValueError:
      print("Transação não existe.")
    else:
      print("Transação deletada com sucesso!")
      break
  

def budget():
  """User coloca input de um orçamento. É calculado o valor total já gasto e o valor poupado"""
  budget = float(input("Digite seu budget: "))
  total = 0
  for dict in dados:
    total += dict['valor']
  sobra = budget - total
  print(f"BUDGET".ljust(15), "GASTO".ljust(15), "POUPADO")
  print(str(budget).ljust(15), str(total).ljust(15), str(sobra).ljust(15))
  
