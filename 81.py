valores_lista = []
while True:
    n = int(input("DIGITE UM VALOR: "))
    valores_lista.append(n)
    parada = input("QUER CONTINUAR? [S/N]: ")

    if  parada in "nN":
        break

print("=-"*30)


print(F'VOCE DIGITOU {len(valores_lista)} elementos')
print(f"LISTA EM ORDEM DECRESCENTE: {sorted(valores_lista, reverse=True)}")

if 5 in valores_lista:
    print("O NUMERO 5 ESTÁ NA LISTA")
else:
    print("O NUMERO 5 NÃO ESTÁ NA LISTA")

