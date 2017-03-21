import os
import re

def var_check(data,data_name,var,path):
    for i in data:
        if i.count('"%s"' %var) > 0:
            path_cor = re.split(r'\\',path)[-1]
            return data_name + ' from ' + path_cor

s_name = set()

variable = raw_input('Type variable name for searching: ').upper()
print '\n'

for root, dirs, fls in os.walk('D:/users/F65605B/Documents/Rafael Pitta/Geral Calibracao/ESTRATEGIAS/GPEC'):
    for name in fls:
        if name.endswith('.mdl'):
            f = open(root+'/'+name,'r')
            f_list = f.read().splitlines()
            s_name.add(var_check(f_list,name,variable,root))           
            f.close()

s_name.remove(None)

for i in s_name:
    print i
