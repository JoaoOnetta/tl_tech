import random

def adivinhar_numero():
    print("Estou pensando em um número entre 1 e 100.")
    input("Pressione Enter quando estiver pronto para começar...")

    tentativas = 0
    baixo = 1
    alto = 100

    while True:
        tentativas += 1
        palpite = random.randint(baixo, alto)
        print(f"Meu palpite é: {palpite}")
        resposta = input("Está certo? (= para sim, > para mais alto, < para mais baixo): ").lower()

        if resposta == '=':
            print(f"Uhul! Adivinhei seu número em {tentativas} tentativas!")
            break
        elif resposta == '>':
            baixo = palpite + 1
        elif resposta == '<':
            alto = palpite - 1
        else:
            print("Resposta inválida. Por favor, responda com '=', '>' ou '<'.")

if __name__ == "_main_":
    adivinhar_numero()