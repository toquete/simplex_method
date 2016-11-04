import numpy as np
from pprintpp import pprint

#Funcao
f = [-10, -6]

#Funcao objetivo artificial
w = []

sa = [
    { 'type': 'ge', 'idx': [4, 2], 'z': 24},
    { 'type': 'le', 'idx': [1, 0], 'z': 8},
    { 'type': 'e', 'idx': [1, 2], 'z': 12}
]

#Add variaveis de folga ou de excesso
for eq in sa:
    if eq['type'] != 'e':
        for eq_ in sa:
            if eq_ == eq:
                eq_['idx'].append(1 * (1 if eq_['type'] == 'le' else -1))
            else:
                eq_['idx'].append(0)

#Add variaveis artificiais
for eq in sa:
    if eq['type'] != 'le':
        for eq_ in sa:
            if eq_ == eq:
                eq_['idx'].append(1)

                #Add variavel na funcao objetivo artifical
                w.append(1)
            else:
                eq_['idx'].append(0)

#Montando matriz do simplex
mat = [eq['idx'] + [eq['z']] for eq in sa]
f.extend([0] * (len(mat[0]) - len(f)))
# mat = [f] + mat

w = [0] * (len(mat[0]) - len(w) - 1) + w + [0]
mat_w = [w] + mat

#Definir quem e a base
b =[]
for c_idx, col in enumerate(mat_w[0]):
    if col == 1:
        b.append(c_idx)

pprint(mat_w)

#Pegar os 'pivos'
# b_pivots = []
while True:
    for b_ in b:
        b_row = 0

        #Pega linha do pivo
        for r_idx, row in enumerate(mat_w[1:]):
            if row[b_] == 1:
                b_row = r_idx + 1
                break

        #Zera as colunas da base
        for r_idx, row in enumerate(mat_w):
            if r_idx != b_row:
                coefficient = -(row[b_] / mat_w[b_row][b_])

                m_row = np.mat(row)
                m_row_base = np.mat(mat_w[b_row])

                mat_w[r_idx] = np.asarray(m_row + (m_row_base * coefficient)).reshape(-1).tolist()

    pprint(mat_w)

    b_tmp = None
    b_tmp_value = 0

    #Verifica se a funcao pode crescer
    for c_idx, col in enumerate(mat_w[0]):

        if col > b_tmp_value:
            b_tmp = c_idx
            b_tmp_value = col

    if b_tmp:
        print 'Pode crescer'

    break

