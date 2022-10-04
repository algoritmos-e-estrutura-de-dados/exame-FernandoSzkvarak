def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao): 
    contador = 0
    menor = len(figurinhas_da_maria)
    menor2 = len(figurinhas_da_joao)
    if menor > menor2:
        menor = menor2


    for figurinha1 in figurinhas_da_maria:
        for figurinha2 in figurinhas_da_maria:
            if figurinha1 == figurinha2:
                contador += 1
        if contador != 1:
            figurinhas_da_maria.remove(figurinha1)
        contador = 0

    for figurinha1 in figurinhas_da_joao:
        for figurinha2 in figurinhas_da_joao:
            if figurinha1 == figurinha2:
                contador += 1
        if contador != 1:
            figurinhas_da_joao.remove(figurinha1)
        contador = 0

        if menor == menor2:
            for figurinha1 in figurinhas_da_joao:
                for figurinha2 in figurinhas_da_maria:
                    if figurinha1 == figurinha2:
                        contador += 1
                if contador >= 1:
                    figurinhas_da_joao.remove(figurinha1)
                contador = 0
            troca = len(figurinhas_da_joao)
        else:
            for figurinha1 in figurinhas_da_maria:
                for figurinha2 in figurinhas_da_joao:
                    if figurinha1 == figurinha2:
                        contador += 1
                if contador >= 1:
                    figurinhas_da_maria.remove(figurinha1)
                contador = 0
            troca = len(figurinhas_da_maria)



    return troca

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))