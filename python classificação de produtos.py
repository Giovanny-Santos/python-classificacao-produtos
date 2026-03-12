idbasico = 0
idcolocado = []
idimpar = []
idpar = []
idbasico = int(idbasico)
docepar = 0
doceimpar = 0
for i in range(10):
    print("Digite o id: ")
    idbasico = input()
    idcolocado.append(idbasico)
    if int(idbasico) % 2 == 0:
        idpar.append(idbasico)
        docepar += 1
    else:
        idimpar.append(idbasico)
        doceimpar += 1
print("todos os IDS colocados: ", idcolocado)
print("todos os IDS pares colocados: ", idpar)
print("todos os IDS impar colocados: ", idimpar)
print("a quantidade de doce par é: ",docepar)
print("a quantidade de doce impar é: ",doceimpar)