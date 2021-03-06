import sys

from parse import parse_function, parse_restriction
from simplex import simplex
from utils import multiply_array_by_scalar

print 'Metodo simplex de duas fases\n'

while True:
    obj = raw_input('Objetivo da funcao [max|min]: ')

    if obj in ['max', 'min']:
        break

    print 'Opcao invalida\n'

func = raw_input('\nEscreva sua funcao [ex: 1x1 + 0x2 + 3x3] (EXPLICITE OS COEFICIENTE 0 e 1): \n\nz = ')
func = parse_function(func)

if obj == 'max':
    func = multiply_array_by_scalar(func, -1)

eq_number = int(raw_input('\nNumero de restricoes: '))

sa = []

print ''

for i in range(1, eq_number + 1):
    eq = raw_input('Restricao %d: ' % (i))
    sa.append(parse_restriction(eq))

print '\n'

result, z = simplex(func, sa)

print ''

for i, x in enumerate(result):
    print 'x%d = %.2f' % (i + 1, x)

if obj == 'max':
    z *= -1

print '\nz = %.2f' % z

raw_input()