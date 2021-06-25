#Desafio técnico Loggi

import pprint

num_pacotes = 15
lista_pacotes = []
pacotes_validos = []
pacotes_invalidos = []
regiao_origem = []
regiao_destino = []
codigo_invalido = 0
aux_valido =0

for i in range(num_pacotes):
        bar_code = input()
        lista_pacotes.append(bar_code)  
    

#Obtenção dos pacotes inválidos.
for pacote in lista_pacotes:
    if(pacote[3:6]=='111'):
        regiao_destino.append("Centro-Oeste")
    elif(pacote[3:6]=='333'):
        regiao_destino.append("Nordeste")
    elif(pacote[3:6]=='555'):
        regiao_destino.append("Norte")
    elif(pacote[3:6]=='888'):
        regiao_destino.append("Sudeste")
    elif(pacote[3:6]=='000'):
        regiao_destino.append("Sul")
    else:
        pacotes_invalidos.append(pacote)

    if(pacote[:3]=='111'):
        regiao_origem.append("Centro-Oeste")
    elif(pacote[:3]=='333'):
        regiao_origem.append("Nordeste")
    elif(pacote[:3]=='555'):
        regiao_origem.append("Norte")
    elif(pacote[:3]=='888'):
        regiao_origem.append("Sudeste")
    elif(pacote[:3]=='000'):
        regiao_origem.append("Sul")
    else:
        pacotes_invalidos.append(pacote)

    if((pacote[:3]=='000') and pacote[12:15]):
        aux_valido = aux_valido + 1

    if(pacote[9:12]=='584'):
        pacotes_invalidos.append(pacote)

    if ((pacote[:3]=='111') and (pacote[12:15]=='000')):
        pacotes_invalidos.append(pacote) 

#Item a)        
print(regiao_destino)

#item b)
pacotes_validos = lista_pacotes

for pacote in pacotes_invalidos:
    pacotes_validos.remove(pacote)
    
print(pacotes_invalidos)

print(pacotes_validos)

#Item c)
if(aux_valido >=1):
    print('Há {0} pacote(s) com origem na Região Sul e Brinquedos em seu conteúdo'.format(aux_valido))

#item d)
destino_centro_oeste = []
destino_nordeste = []
destino_norte = []
destino_sudeste = []
destino_sul = []
macro = []

for pacote in pacotes_validos:
    if(pacote[3:6]=='111'):
        destino_centro_oeste.append(pacote)
    elif(pacote[3:6]=='333'):
        destino_nordeste.append(pacote)
    elif(pacote[3:6]=='555'):
        destino_norte.append(pacote)
    elif(pacote[3:6]=='888'):
        destino_sudeste.append(pacote)
    elif(pacote[3:6]=='000'):
        destino_sul.append(pacote)

macro.append(destino_centro_oeste)
macro.append(destino_nordeste)
macro.append(destino_norte)
macro.append(destino_sudeste)
macro.append(destino_sul)

#Agrupamento por destino.
print(macro)

#item e)

pacotes_vendedor = {}

for pacotes in pacotes_validos:
    pacote = pacotes[9:12]
    pacotes_vendedor.setdefault(pacote,0)
    pacotes_vendedor[pacote] +=1

pprint.pprint(pacotes_vendedor)

#item f)

#Listagem por destino
pacotes_destino = {}

for pacotes in pacotes_validos:
    pacote = pacotes[3:6]
    pacotes_destino.setdefault(pacote,0)
    pacotes_destino[pacote] = pacotes 

pprint.pprint(pacotes_destino)

#Listagem por tipo
pacotes_tipo = {}

for pacotes in pacotes_validos:      
    pacote = pacotes[12:15]
    pacotes_tipo.setdefault(pacote,0)
    pacotes_tipo[pacote] = pacotes

pprint.pprint(pacotes_tipo)

   


