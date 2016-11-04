import numpy as np

f = [-6, 1]

sa = [
    { 'type': 'le', 'idx': [4, 1], 'z': 21},
    { 'type': 'ge', 'idx': [2, 3], 'z': 13},
    { 'type': 'e', 'idx': [1, -1], 'z': -1}
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
            else:
                eq_['idx'].append(0)

#Montando matriz do simplex
mat = [eq['idx'] + [eq['z']] for eq in sa]
f.extend([0] * (len(mat[0]) - len(f)))
mat = [f] + mat

print mat


