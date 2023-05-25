import sys
import os
import transacao


try:
  transacao.arquivar()
except FileNotFoundError:
  transacao.criar_arquivo()
  
print("----------------------- MENU -----------------------")
print("[LER]   Extrato\n[ADD]   Adicionar transação\n[ATT]   Atualizar transação\n[DEL]   Deletar transação\n[BUD]   Budget")

acao = input().upper()
if acao == 'LER':
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
  transacao.add()
  transacao.arquivar()
  
elif acao == 'ATT':
  transacao.atualizar()
  
elif acao == 'DEL':
  transacao.deletar()

elif acao == 'BUD':
  transacao.budget()
else:
  print("Função não existente.")
    
