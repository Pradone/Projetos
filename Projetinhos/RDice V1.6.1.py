import random

final = []

while True:
    while True:
        try:
            tipo_de_d = int(input("qual dado deseja rolar (d4, d6, d8, d10, d12, d20, d100): d"))
            numero_de_dados = int(input("Quantos dados deseja rolar? "))
            if tipo_de_d < 0:
                continue
            elif tipo_de_d == 20:
                valor_adicional = 0
                valor_pericia = int(input("Deseja adicionar algum valor de perícia? "))
            else:
                valor_adicional = int(input("Deseja adicionar algum valor fixo? "))
                valor_pericia = 0
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    resultados = []
    for i in range(numero_de_dados):
        rolar_dado = random.randint(1,  tipo_de_d)
        resultados.append(rolar_dado + valor_pericia)

    d20_natural = [valor - valor_pericia for valor in resultados]

    d20_natural.sort(reverse=True)
    resultados.sort(reverse=True)
    soma_resultados = sum(resultados)
    soma = soma_resultados + valor_adicional

    if len(resultados) == 1:
        print("O valor do seu dado foi:", resultados)
    else:
        print("Os valores dos seus dados foram:", resultados)

    if tipo_de_d != 20:
        print("A soma de todos foi: ", soma)
    if tipo_de_d == 20 and valor_pericia != 0:
        print("Os valores naturais dos d20 foram:", d20_natural)

    combo = input("Deseja rolar de novo? ")
    final.append(soma)
    
    if combo == "sim":
        continue
    else:
        break
    
soma_2 = sum(final)
if tipo_de_d != 20:
    print("Seu valor final foi: ", soma_2)
else:
    print("Olhos sempre abertos!")    
    

# corrigir bugs e otimizar sistema
# testes e mais testes para correção de possíveis bugs