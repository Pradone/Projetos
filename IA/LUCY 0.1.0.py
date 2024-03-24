import random
import PPT_in_AI as pedraPTesoura


conversas = {
    "Olá": ["Olá!", "Oie!", "Oi!", "Olá, como posso ajudar?"],
    "Como você está?": ["Estou bem, obrigado por perguntar!", "Estou ótimo!", "Nunca estive melhor!"],
    "Qual é o seu nome?": ["Meu nome é LUCY.", "Eu sou a LUCY.", "Você pode me chamar de LUCY."],
    "Qual é a sua idade?": ["Eu sou uma Inteligencia Artificial, eu não tenho idade.", "Idade é uma noção humana, não se aplica a mim."],
    "O que você pode fazer?": ["Posso responder perguntas, conversar e fornecer informações.", "Estou aqui para ajudar com o que precisar."],
    "Obrigado": ["De nada!", "Não há de quê!", "Estou sempre aqui para ajudar!"],
    "Qual a sua versão?": ["No momento me apresento na versão 0.1.0, e ainda estou em fase de testes", "Sou apenas um protótipo", "Ainda não sou uma Inteligência Artificial efetivamente, mas meu dev esta trabalhando duro para isso ser uma realidade em breve!"],
    "Quais são as novidades da nova versão?": ["Agora tenho um protótipo de central de jogos, me pergunte 'Quero jogar um jogo' para testar!"]
}
externos = {
    "Quero jogar um jogo": []
}

def responder(pergunta):
    resposta_padrao = "Desculpe, não entendi sua pergunta. Poderia reformular?"
    if pergunta in conversas:
        return random.choice(conversas[pergunta])
    elif pergunta in externos:
        return jogos()
    else:
        return resposta_padrao

def jogos():
    jogo = input("Claro! Qual gostaria de jogar? ")
    
    not_yet = "Desculpe, ainda nao tenho esse jogo"
    if jogo == 'Pedra, papel ou tesoura':
        return pedraPTesoura.PPT()
    else:
        return not_yet
    


print("Bem-vindo à LUCY. Digite 'sair' para encerrar o chat.")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair' or pergunta.lower() == 'tchau':
        print("Chat encerrado, até mais!")
        break
    resposta = responder(pergunta)
    print("LUCY:", resposta)
