import numpy as np

def print_matrix(matrix):
    for xablau in range(0, len(matrix[0])):
        print '%6d' % xablau,
    print '\n'
    for i, row in enumerate(matrix):

        for col in row:
            print '%6.2f' % col,
        print ''
        if i == 0:
            print ''
    print '\n'


def simplex(func, sa):

    #Funcao objetivo artificial
    w = []

    # Base
    b = []

    #Add variaveis de folga ou de excesso
    for eq in sa:
        if eq['type'] != 'e':
            for i, eq_ in enumerate(sa):
                if eq_ == eq:
                    if eq_['type'] == 'le':
                        b.append([i + 1, len(eq_['idx'])])
                        eq_['idx'].append(1)
                    else:
                        eq_['idx'].append(-1)
                else:
                    eq_['idx'].append(0)

    #Add variaveis artificiais
    for eq in sa:
        if eq['type'] != 'le':
            for i, eq_ in enumerate(sa):
                if eq_ == eq:
                    b.append([i + 1, len(eq_['idx'])])

                    eq_['idx'].append(1)

                    #Add variavel na funcao objetivo artifical
                    w.append(1)
                else:
                    eq_['idx'].append(0)

    # print "ENCONTROU A BASE"
    # print bnew

    #Montando matriz do simplex
    mat = [eq['idx'] + [eq['z']] for eq in sa]

    #Montando matriz do simplex da funcao objetivo artificial
    w = [0] * (len(mat[0]) - len(w) - 1) + w + [0]
    mat = [w] + mat

    #Definir quem e a base
    # b = []
    # for c_idx, col in enumerate(mat[0]):
    #     if col == 1:
    #         #Pega linha do pivo
    #         for r_idx, row in enumerate(mat[1:]):
    #             if row[c_idx] == 1:
    #                 b.append([r_idx + 1, c_idx])
    #                 break

    print 'FASE 1\n'

    print_matrix(mat)

    steps = 0
    #Primeira fase
    while True:
        print b

        print 'PASSO %d' % steps

        for b_ in b:

            #Zera as colunas da base
            for r_idx, row in enumerate(mat):
                if r_idx != b_[0]:
                    coefficient = -(row[b_[1]] / mat[b_[0]][b_[1]])

                    m_row = np.mat(row)
                    m_row_base = np.mat(mat[b_[0]])

                    mat[r_idx] = np.asarray(m_row + (m_row_base * coefficient)).reshape(-1).tolist()

        print_matrix(mat)

        b_tmp = None
        b_tmp_value = 0

        #Verifica se a funcao pode crescer
        for c_idx, col in enumerate(mat[0][:-1]):
            if col < b_tmp_value:
                b_tmp = c_idx
                b_tmp_value = col

        if b_tmp == None:
            break

        #Estudo do bloqueio
        bloq_tmp = None
        bloq_tmp_value = 999999

        for b_ in b:
            #Ve qual dos valores e menor
            try:
                bloq_aux = mat[b_[0]][-1] / mat[b_[0]][b_tmp]
            except:
                bloq_aux = -999999

            if bloq_aux >= 0 and bloq_aux <= bloq_tmp_value:
                bloq_tmp_value = bloq_aux
                bloq_tmp = b_

        #Altera no vetor base com a nova variavel
        b[b.index(bloq_tmp)][1] = b_tmp

        new_b = b[b.index(bloq_tmp)]

        #Divide a linha pro pivo ser igual a 1
        mat[new_b[0]] = np.asarray(np.mat(mat[new_b[0]]) / mat[new_b[0]][b_tmp]).reshape(-1).tolist()

        steps += 1

        if steps == 10:
            break

    #Removendo as colunas das variaveis artificiais
    if not all(w_ == 0 for w_ in w):
        mat = [x[:-3] + x[-1:] for x in mat]

    #Encontrando a base
    # b = []
    # for c_idx, col in enumerate(mat[0]):
    #     b_row = 0

    #     found_one = 0
    #     found_not_zero = 0

    #     for r_idx, row in enumerate(mat[1:]):

    #         if row[c_idx] == 1:
    #             found_one += 1
    #             b_row = r_idx + 1
    #         elif row[c_idx] != 0:
    #             found_not_zero += 1

    #     if found_one == 1 and found_not_zero == 0:
    #         b.append([b_row, c_idx])

    #Montando a matriz do simplex
    f = func + [0] * (len(mat[0]) - len(func))
    mat = [f] + mat[1:]

    print 'FASE 2\n'
    print_matrix(mat)

    steps = 0
    #Segunda fase
    while True:
        print 'PASSO %d' % steps

        for b_ in b:

            #Zera as colunas da base
            for r_idx, row in enumerate(mat):
                if r_idx != b_[0]:
                    coefficient = -(row[b_[1]] / mat[b_[0]][b_[1]])

                    m_row = np.mat(row)
                    m_row_base = np.mat(mat[b_[0]])

                    mat[r_idx] = np.asarray(m_row + (m_row_base * coefficient)).reshape(-1).tolist()

        print_matrix(mat)

        b_tmp = None
        b_tmp_value = 0

        #Verifica se a funcao pode crescer
        for c_idx, col in enumerate(mat[0][:-1]):
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
                bloq_aux = mat[b_[0]][len(mat[b_[0]]) - 1] / mat[b_[0]][b_tmp]
            except:
                bloq_aux = None

            if bloq_aux != None and bloq_aux >= 0 and bloq_aux < bloq_tmp_value:
                bloq_tmp_value = bloq_aux
                bloq_tmp = b_


        print b
        print b_tmp
        print bloq_tmp
         #Altera no vetor base com a nova variavel
        b[b.index(bloq_tmp)][1] = b_tmp

        new_b = b[b.index(bloq_tmp)]

        #Divide a linha pro pivo ser igual a 1
        mat[new_b[0]] = np.asarray(np.mat(mat[new_b[0]]) / mat[new_b[0]][b_tmp]).reshape(-1).tolist()

        steps += 1

        if steps == 10:
            break

    result = [0] * len(func)

    for b_ in b:
        if b_[1] < len(result):
            result[b_[1]] = mat[b_[0]][-1]

    # for i, x in enumerate(result):
    #     print 'x%d = %.2f' % (i + 1, x)

    return result, -mat[0][-1]