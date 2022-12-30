# Atividade 1 - Executar o código seguinte:

nomes = ['Maria', 'Julieta', 'Fernado', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
qtd_letras = {}


for nome in nomes:
  qtd_letras[nome] = len(nome)
print(qtd_letras)

print('='*60)

# Atividade 2 - Reescrever o código da atividade 1 utilizando o conceito de compreensão de dicionários.

nomes1 = ['Maria', 'Julieta', 'Fernado', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
qtd_letras2 = {item: len(item) for item in nomes1}
print(qtd_letras2)

print('='*60)

# Atividade 3 - Criar uma função area(r, pi) que calcula a área de um círculo. Deve-se usar um valor padrão para o pi e deve ser possível utilizar a declaração explícita do valor exato do pi desejado.

from modulo import area

print(area(15))
print(area(15, 3.1415))

print('='*60)


# Atividade 4 - Reescrever a função da atividade 3 utilizando o conceito de funções anônimas.

areas = lambda r, pi = 3.14: pi*(r**2)
print(areas(15))

print('='*60)


# Atividade 5 - Criar módulo com funções que recebem uma lista do tipo inteira como argumento. Reaproveitar funções.

from processalista import *

a = [3, 4, 5, 6, 7, 8, 9, 10,11,12]

maior_menor_impar(a)

print('='*60)


# Atividade 6 - Desenvolver duas funções que receberão a relação de disponibilidade de cada médico e que retornarão os dias disponíveis.

cardiologista = {'terça', 'quarta'}
ortopedista = {'terça', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terça', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

def disp_dois_especialistas(medico01, medico02):
  d = medico01 & medico02
  print(d)

def disp_tres_especialistas(medico01, medico02, medico03):
  d = medico01 & medico02 & medico03
  print(d)

disp_dois_especialistas(ortopedista, neurologista)
disp_tres_especialistas(dermatologista, neurologista, psiquiatra)

