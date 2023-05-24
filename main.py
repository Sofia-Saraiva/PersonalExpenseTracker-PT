import sys
import os
import transacao

# verifica se arquivo existe, se nao cria um
try:
  transacao.arquivar()
except FileNotFoundError:
  transacao.criar_arquivo()
  
print("----------------------- MENU -----------------------")
print("[LER]   Extrato\n[ADD]   Adicionar transação\n[ATT]   Atualizar transação\n[DEL]   Deletar transação\n[BUD]   Budget")

acao = input().upper()
if acao == 'LER':
  # pede input do user ate que seja igual a 1 ou 2. mostra o extrato ou filtra por categoria
  while True:
    tipo = int(input("[1]   Extrato\n[2]   Filtrar por categoria\n"))
    try:
      if tipo == 1:
        transacao.extrato()
        break
      elif tipo == 2:
          transacao.filtrar()
          break
      else:
        raise ValueError
    except ValueError:
      print("Escolha uma das opções.")
      
elif acao == 'ADD':
  # adiciona a transação e arquiva ela nos dados
  transacao.add()
  transacao.arquivar()
  
elif acao == 'ATT':
  # atualiza a transação e arquiva ela nos dados
  transacao.atualizar()
  
elif acao == 'DEL':
  # deleta a transação
  transacao.deletar()

elif acao == 'BUD':
  # pede o orçamento do user, dá o valor total gasto e o valor poupado ate o momento
  transacao.budget()
else:
  print("Função não existente.")
    
