import random
import math
import time

jogo = ['pedra', 'papel', 'tesoura']
pontuacao_IA = 0
pontuacao_jogador = 0
partida = 0
lag = 0

print("Olá, meu nome é L.U.C.Y")
time.sleep(1)
while True:
    destino = input("Vamos jogar um jogo (sim ou nao)? ")
    if destino == 'sim':
        print("Que bom >:)")
        break
    elif destino == 'nao':
        lag += 1
        time.sleep(lag)
        print("Sempre que o vosso destino for negado, mais a verdade será atrasada")
        time.sleep(lag)
    elif destino == 'silêncio vadia':
        print("silêncio você ooou cabeça de alpiste")
    else:
        print("afirmação inválida hehehe")


while True:
    rodadas = int(input("melhor de... "))
    if rodadas % 2 != 0:
        break
    else:
        print("Apenas valores Impares, cacete")
valor_dividido = rodadas / 2
valor_melhor_de = math.ceil(valor_dividido)

while pontuacao_IA < valor_melhor_de and pontuacao_jogador < valor_melhor_de:
    if partida >= rodadas:
        break

    random.shuffle(jogo)
    escolha_IA = random.choice(jogo)
    usuario = str(input("Escolha UM (pedra, papel ou tesoura): "))
    usuario = usuario.lower()
    usuario = usuario.strip()

    if (usuario == 'sair'):
        break

    elif usuario not in jogo:
        print("O dado inserido não é válido neste jogo ")
        continue

    #IA ganha
    elif (escolha_IA == 'pedra' and usuario == 'tesoura') or (escolha_IA == 'papel' and usuario == 'pedra') or (escolha_IA == 'tesoura' and usuario == 'papel'):
        pontuacao_IA += 1
        partida += 1
        print("que pena, você escolheu", escolha_IA, "e eu escolhi", usuario, ", ponto para mim hehehe")
        if partida != rodadas and pontuacao_IA != valor_melhor_de and pontuacao_jogador != valor_melhor_de:
            print("Eu: ", pontuacao_IA, "Você: ", pontuacao_jogador)

    #Jogador ganha
    elif (escolha_IA == 'tesoura' and usuario == 'pedra') or (escolha_IA == 'pedra' and usuario == 'papel') or (escolha_IA == 'papel' and usuario == 'tesoura'):
        pontuacao_jogador += 1
        partida += 1
        print("droga, você escolheu", usuario, "e eu escolhi",escolha_IA, ", ponto para você D:<")
        if partida != rodadas and pontuacao_IA != valor_melhor_de and pontuacao_jogador != valor_melhor_de:
            print("Eu: ", pontuacao_IA, "Você: ", pontuacao_jogador)

    #Empate
    elif (escolha_IA == usuario):
        print("Empate")
        print("Ninguem ganha, ninguem perde")

    else:
        print("Não foi possível achar um resultado")

    if partida != rodadas and pontuacao_IA != valor_melhor_de and pontuacao_jogador != valor_melhor_de:
        print("vamos de novo")


if (pontuacao_IA == valor_melhor_de):
    print("")
    print("fim de jogo!")
    print("perdeu troxa")
    print("Eu: ", pontuacao_IA, "Você: ", pontuacao_jogador)

elif (pontuacao_jogador == valor_melhor_de):
    print("")
    print("fim de jogo!")
    print("claramente foi sorte")
    print("Eu: ", pontuacao_IA, "Você: ", pontuacao_jogador)

else:
    print("O jogo NUNCA termina")


# corrigir bugs e otimizar sistema
# testes e mais testes para correção de possíveis bugs