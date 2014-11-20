def posibles(personas):
    if personas == []:
        return ['']
    lista = []
    for i in range(len(personas)):
        for j in posibles(personas[:i] + personas[i + 1:]):
            lista.append(personas[i]+','+j)
    return lista

def piezas_posibles(piezas, personas):
    lista = [i.split(',') for i in [j[:-1] for j in posibles(personas)]]
    pos = []
    for i in lista:
    	for j in piezas:
    		pos.append(i[:j+1])
    return pos

personas = ["jose", "pedro", "diego"]
print([i.split(',') for i in [j[:-1] for j in posibles(personas)]])
print(piezas_posibles([1,2], personas))