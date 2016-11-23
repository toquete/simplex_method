import copy
from utils import multiply_array_by_scalar, divide_array_by_scalar, sum_arrays

def print_matrix(matrix):
    for i_ in range(1, len(matrix[0])):
        x = 'x%d' % i_
        print x.rjust(6),
    print '     z',
    print '\n'
    for i, row in enumerate(matrix):

        for col in row:
            print '%6.2f' % col,
        print ''
        if i == 0:
            print ''

def print_base(base):
    print '\nBASE = {',
    for b_ in base:
        print ' x%d ' % (b_[1] + 1),
    print '}\n'

def simplex(func, sa):

    #Funcao objetivo artificial
    w = []

    #Base
    b = []

    #Numero de variaveis artificiais
    aritificial_variables = 0

    #Historico da base pra saber se ele voltou pra algum ponto
    b_history = []

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

                    #Conta o numero de variaveis artificiais
                    aritificial_variables += 1
                else:
                    eq_['idx'].append(0)

    #Montando matriz do simplex
    mat = [eq['idx'] + [eq['z']] for eq in sa]

    #Montando matriz do simplex da funcao objetivo artificial
    w = [0] * (len(mat[0]) - len(w) - 1) + w + [0]
    mat = [w] + mat

    print ' FASE 1 '.center(70, '-')
    print ''

    print_matrix(mat)

    steps = 0
    #Primeira fase
    while True:

        print_base(b)

        print 'PASSO %d\n' % steps

        for b_ in b:

            #Zera as colunas da base
            for r_idx, row in enumerate(mat):
                if r_idx != b_[0]:
                    coefficient = -(row[b_[1]] / mat[b_[0]][b_[1]])

                    m_row = copy.deepcopy(row)
                    m_row_base = copy.deepcopy(mat[b_[0]])

                    mat[r_idx] = sum_arrays(m_row, (multiply_array_by_scalar(m_row_base, coefficient)))

        print_matrix(mat)

        b_history.append(copy.deepcopy(b))

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
            if mat[b_[0]][b_tmp] <= 0:
                bloq_aux = -999999
            else:
                bloq_aux = mat[b_[0]][-1] / mat[b_[0]][b_tmp]

            if bloq_aux >= 0 and bloq_aux <= bloq_tmp_value:
                bloq_tmp_value = bloq_aux
                bloq_tmp = b_

        #Altera no vetor base com a nova variavel
        b[b.index(bloq_tmp)][1] = b_tmp

        #Verifica se esta voltando pro mesmo ponto
        if b in b_history:
            b = b_history[-1]
            print '\nSOLUCAO ADMITE INFINITAS SOLUCOES\n'
            break

        new_b = b[b.index(bloq_tmp)]

        #Divide a linha pro pivo ser igual a 1
        mat[new_b[0]] = divide_array_by_scalar(copy.deepcopy(mat[new_b[0]]), mat[new_b[0]][b_tmp])

        steps += 1

    aritificial_variables += 1

    #Removendo as colunas das variaveis artificiais
    if not all(w_ == 0 for w_ in w):
        mat = [x[:-aritificial_variables] + x[-1:] for x in mat]

    #Montando a matriz do simplex
    f = func + [0] * (len(mat[0]) - len(func))
    mat = [f] + mat[1:]

    print '\n'
    print ' FASE 2 '.center(70, '-')
    print ''

    print_matrix(mat)

    steps = 0
    #Segunda fase
    while True:
        print_base(b)

        print 'PASSO %d\n' % steps

        for b_ in b:

            #Zera as colunas da base
            for r_idx, row in enumerate(mat):
                if r_idx != b_[0]:
                    coefficient = -(row[b_[1]] / mat[b_[0]][b_[1]])

                    m_row = copy.deepcopy(row)
                    m_row_base = copy.deepcopy(mat[b_[0]])

                    mat[r_idx] = sum_arrays(m_row, (multiply_array_by_scalar(m_row_base, coefficient)))

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
                bloq_aux = mat[b_[0]][len(mat[b_[0]]) - 1] / mat[b_[0]][b_tmp]
            except:
                bloq_aux = None

            if bloq_aux != None and bloq_aux >= 0 and bloq_aux < bloq_tmp_value:
                bloq_tmp_value = bloq_aux
                bloq_tmp = b_

        # print_base(b)

         #Altera no vetor base com a nova variavel
        b[b.index(bloq_tmp)][1] = b_tmp

        new_b = b[b.index(bloq_tmp)]

        #Divide a linha pro pivo ser igual a 1
        mat[new_b[0]] = divide_array_by_scalar(copy.deepcopy(mat[new_b[0]]), mat[new_b[0]][b_tmp])

        # print_matrix(mat)

        steps += 1

        if steps == 10:
            break

    result = [0] * len(func)

    for b_ in b:
        if b_[1] < len(result):
            result[b_[1]] = mat[b_[0]][-1]

    print ''

    for i, x in enumerate(result):
        print 'x%d = %.2f' % (i + 1, x)

    print '\nz = %.2f' % (-mat[0][-1])

    return result, -mat[0][-1]