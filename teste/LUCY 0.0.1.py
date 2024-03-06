import random

# Dicionário de perguntas e respostas
conversas = {
    "Olá": ["Olá!", "Oie!", "Oi!", "Olá, como posso ajudar?"],
    "Como você está?": ["Estou bem, obrigado por perguntar!", "Estou ótimo!", "Nunca estive melhor!"],
    "Qual é o seu nome?": ["Meu nome é LUCY.", "Eu sou a LUCY.", "Você pode me chamar de LUCY."],
    "Qual é a sua idade?": ["Eu sou uma Inteligencia Artificial, eu não tenho idade.", "Idade é uma noção humana, não se aplica a mim."],
    "O que você pode fazer?": ["Posso responder perguntas, conversar e fornecer informações.", "Estou aqui para ajudar com o que precisar."],
    "Obrigado": ["De nada!", "Não há de quê!", "Estou sempre aqui para ajudar!"],
    "Qual a sua versão?": ["No momento me apresento na versão 0.0.1, e ainda estou em fase de testes", "Sou apenas um protótipo"]
}

# Função para responder à pergunta do usuário
def responder(pergunta):
    resposta_padrao = "Desculpe, não entendi sua pergunta. Poderia reformular?"
    if pergunta in conversas:
        return random.choice(conversas[pergunta])
    else:
        return resposta_padrao

# Loop do chat
print("Bem-vindo à LUCY. Digite 'sair' para encerrar o chat.")
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == 'sair':
        print("Chat encerrado, até mais")
        break
    resposta = responder(pergunta)
    print("LUCY:", resposta)
