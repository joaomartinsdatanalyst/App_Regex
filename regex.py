import re

def comeca_com_e_tem_x_caracteres(elemento, comeca_com, caracteres):
    elemento_2 = [elemento]
    resultado = []
    n_max = len(elemento_2[0])
    n_car = elemento_2[0].count(comeca_com)
    for ii in range(1, n_car+1):
        if ii == 1:  
            pos_1 = elemento_2[0].find(comeca_com)
            try:
                resultado.append(elemento_2[0][pos_1:caracteres])
                continue
            except:
                continue
        else:
            try:
                pos_2 = elemento_2[0][(pos_1+len(comeca_com)):n_max].find(comeca_com)
                pos_2 += pos_1+len(comeca_com)
                resultado.append(elemento_2[0][pos_2:(pos_2+caracteres)])
                pos_1 = pos_2
                continue
            except:
                continue
    return resultado



def comeca_com_e_nao_tem_x_caracteres(elemento, comeca_com):
    elemento_2 = [elemento]
    resultado = []
    n_max = len(elemento_2[0])
    n_car = elemento_2[0].count(comeca_com)
    for ii in range(1, n_car+1):
        if ii == 1:  
            pos_1 = elemento_2[0].find(comeca_com)
            try:
                array = elemento_2[0][pos_1:n_max]
                padrao = re.compile(rf"{re.escape(comeca_com)}\S*")
                result = padrao.findall(array+' ')
                n_sublista = len(result)
                if n_sublista > 0:
                    for iii in range(0, n_sublista):
                        resultado.append(result[iii])
                continue
            except:
                continue
        else:
            try:
                pos_2 = elemento_2[0][(pos_1+len(comeca_com)):n_max].find(comeca_com)
                pos_2 += pos_1+len(comeca_com)
                array = elemento_2[0][pos_2:n_max]
                padrao = re.compile(rf"{re.escape(comeca_com)}\S*")
                result = padrao.findall(array+' ')
                n_sublista = len(result)
                if n_sublista > 0:
                    for iii in range(0, n_sublista):
                        resultado.append(result[iii])
                pos_1 = pos_2
                continue
            except:
                continue
    return resultado