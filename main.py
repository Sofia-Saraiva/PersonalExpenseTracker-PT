import sys
import os
import transacao

print("----------------------- MENU -----------------------")
print("[LER] Extrato\n[ADD] Adicionar transação\n[ATT] Atualizar transação\n[DEL] Deletar transação\n[BUD] Budget")
transacao.arquivar()

acao = input().upper()
if acao == 'LER':
  while True:
    tipo = int(input("1 - Extrato\n2 - Filtrar por categoria\n"))
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
  transacao.arquivar()
  
elif acao == 'DEL':
  transacao.deletar()
  dados = []
  transacao.arquivar()

elif acao == 'BUD':
  transacao.budget()
else:
  print("Função não existente.")
    
