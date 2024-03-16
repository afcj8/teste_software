from craps import Craps

craps = Craps()

while not craps.fimDeJogo():
  print('Digite ENTER para continuar')
  input()
  soma = craps.rolarDados()
  print('Soma:', soma)

if craps.vencedor == 1:
  print('Você ganhou!')
elif craps.vencedor == 2:
  print('A banca ganhou')
else:
  raise RuntimeError('Resultado inesperado')
