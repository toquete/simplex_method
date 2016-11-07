import numpy as np
from pprintpp import pprint

def print_matrix(matrix):
    for i, row in enumerate(matrix):
        for col in row:
            print '%6.2f' % col,
        print ''
        if i == 0:
            print ''
    print '\n'


#Funcao
f = [4, 1, 1]

#Funcao objetivo artificial
w = []

sa = [
    { 'type': 'e', 'idx': [2.0, 1.0, 2.0], 'z': 4.0},
    { 'type': 'e', 'idx': [3.0, 3.0, 1.0], 'z': 3.0},
    # { 'type': 'e', 'idx': [1, 2], 'z': 12}
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

#Montando matriz do simplex da funcao objetivo artificial
w = [0] * (len(mat[0]) - len(w) - 1) + w + [0]
mat_w = [w] + mat

print_matrix(mat_w)

#Definir quem e a base
b = []
for c_idx, col in enumerate(mat_w[0]):
    if col == 1:
        #Pega linha do pivo
        for r_idx, row in enumerate(mat_w[1:]):
            if row[c_idx] == 1:
                b.append([r_idx + 1, c_idx])
                break

steps = 0
#Primeira fase
while True:
    print 'PASSO %d' % steps

    for b_ in b:

        #Zera as colunas da base
        for r_idx, row in enumerate(mat_w):
            if r_idx != b_[0]:
                coefficient = -(row[b_[1]] / mat_w[b_[0]][b_[1]])

                m_row = np.mat(row)
                m_row_base = np.mat(mat_w[b_[0]])

                mat_w[r_idx] = np.asarray(m_row + (m_row_base * coefficient)).reshape(-1).tolist()

    print_matrix(mat_w)

    b_tmp = None
    b_tmp_value = 0

    #Verifica se a funcao pode crescer
    for c_idx, col in enumerate(mat_w[0][:-1]):
        if col < b_tmp_value:
            b_tmp = c_idx
            b_tmp_value = col

    if b_tmp == None:
        break

    #Estudo do bloqueio
    bloq_tmp = None
    bloq_tmp_value = 999999 #Rever essa PORRA

    for b_ in b:
        #Ve qual dos valores e menor
        try:
            bloq_aux = mat_w[b_[0]][len(mat_w[b_[0]]) - 1] / mat_w[b_[0]][b_tmp]
        except:
            bloq_aux = 0

        if bloq_aux >= 0 and bloq_aux < bloq_tmp_value:
            bloq_tmp_value = bloq_aux
            bloq_tmp = b_

    #Altera no vetor base com a nova variavel
    b[b.index(bloq_tmp)][1] = b_tmp

    new_b = b[b.index(bloq_tmp)]

    #Divide a linha pro pivo ser igual a 1
    mat_w[new_b[0]] = np.asarray(np.mat(mat_w[new_b[0]]) / mat_w[new_b[0]][b_tmp]).reshape(-1).tolist()

    steps += 1