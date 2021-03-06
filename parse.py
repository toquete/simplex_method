import re

def parse_function(str):
    function = str.replace(' ', '')
    function = filter(lambda x: x, re.split(r'x\d', function))

    return [float(x) for x in function]

def parse_restriction(str):
    eq = {}
    sep = ''
    
    if str.find('<=') != -1:
        eq['type'] = 'le'
        sep = '<='
    elif str.find('>=') != -1:
        eq['type'] = 'ge'
        sep = '>='
    else:
        eq['type'] = 'e'
        sep = '='

    str = str.split(sep)

    z = str[1]
    xs = str[0].replace(' ', '')

    eq['z'] = float(z)

    import re
    xs = filter(lambda x: x,re.split(r'x\d', xs))
    eq['idx'] = [float(x) for x in xs]

    return eq