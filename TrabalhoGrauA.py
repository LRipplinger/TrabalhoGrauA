import random

# Função para jogar o dado
def jogar_dado():
    input("Pressione Enter para jogar o dado...")
    return random.randint(1, 6)

# Funções para os desafios matemáticos
def desafio_1():
    print("Números primos até 100:")
    for num in range(2, 101):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num, end=' ')
    print()

def desafio_2():
    print("Somatório dos números de 1 até 100:", sum(range(1, 101)))

def desafio_3():
    a, b = 0, 1
    print("Série de Fibonacci até o décimo elemento:")
    for _ in range(10):
        print(a, end=' ')
        a, b = b, a + b
    print()

def desafio_4():
    raio = 2.5
    area = 3.14 * raio ** 2
    print("Área de um círculo com raio 2.5:", area)

def desafio_5():
    fatorial = 1
    for i in range(1, 6):
        fatorial *= i
    print("Fatorial de 5:", fatorial)

def desafio_6():
    print("Os 5 primeiros números divisíveis por 2 e por 5:", [i for i in range(10, 51) if i % 2 == 0 and i % 5 == 0])

# Função para executar o desafio matemático
def executar_desafio():
    desafios = [desafio_1, desafio_2, desafio_3, desafio_4, desafio_5, desafio_6]
    random.choice(desafios)()

# Função para escolher a formatura
def formatura():
    opcoes = {
        1: "Direito",
        2: "Medicina",
        3: "Arquitetura",
        4: "Nutrição",
        5: "Análise e Desenvolvimento de Sistemas",
        6: "Jogos Digitais"
    }
    escolha = random.randint(1, 6)
    print("Você se formou em", opcoes[escolha], "!!!")

# Função principal do jogo
def jogo_da_vida():
    posicao_jogador_1 = 0
    posicao_jogador_2 = 0
    relacionamento_jogador_1 = "Solteiro"
    relacionamento_jogador_2 = "Solteiro"
    filhos_jogador_1 = 0
    filhos_jogador_2 = 0

    while True:
        input("Jogador 1: Pressione Enter para jogar o dado...")
        resultado_jogador_1 = jogar_dado()
        print("Resultado do dado para Jogador 1:", resultado_jogador_1)
        posicao_jogador_1 += resultado_jogador_1

        if posicao_jogador_1 == 3:
            executar_desafio()
        elif posicao_jogador_1 == 6:
            print("Jogador 1 perdeu uma rodada!")
        elif posicao_jogador_1 == 9:
            filhos = jogar_dado()
            if filhos == 5:
                filhos_jogador_1 += 2
                print("Jogador 1 teve gêmeos!")
            else:
                filhos_jogador_1 += 1
                print("Jogador 1 teve um filho!")
        elif posicao_jogador_1 == 12:
            print("Jogador 1 casou!")
            relacionamento_jogador_1 = "Casado"
        elif posicao_jogador_1 == 15:
            print("Jogador 1 ficou famoso!")
        elif posicao_jogador_1 == 18:
            premio = random.choice([2.5, 5000, 50000, 500000, 5000000])
            print("Jogador 1 ganhou R$", premio, "na loteria!")
        elif posicao_jogador_1 == 21:
            if relacionamento_jogador_1 == "Solteiro":
                relacionamento_jogador_1 = "Casado"
                print("Jogador 1 encontrou um novo amor e casou-se!")
            elif relacionamento_jogador_1 == "Casado":
                print("Jogador 1 caiu na casa do novo amor, mas já é casado!")
            elif relacionamento_jogador_1 == "Divorciado":
                print("Jogador 1 caiu na casa do novo amor, mas já é divorciado!")
        elif posicao_jogador_1 > 21:
            print("Jogador 1 morreu!!! Game Over!!!")
            print("Jogador 2 ganhou!")
            break

        input("Jogador 2: Pressione Enter para jogar o dado...")
        resultado_jogador_2 = jogar_dado()
        print("Resultado do dado para Jogador 2:", resultado_jogador_2)
        posicao_jogador_2 += resultado_jogador_2

        if posicao_jogador_2 == 3:
            executar_desafio()
        elif posicao_jogador_2 == 6:
            print("Jogador 2 perdeu uma rodada!")
        elif posicao_jogador_2 == 9:
            filhos = jogar_dado()
            if filhos == 5:
                filhos_jogador_2 += 2
                print("Jogador 2 teve gêmeos!")
            else:
                filhos_jogador_2 += 1
                print("Jogador 2 teve um filho!")
        elif posicao_jogador_2 == 12:
            print("Jogador 2 casou!")
            relacionamento_jogador_2 = "Casado"
        elif posicao_jogador_2 == 15:
            print("Jogador 2 ficou famoso!")
        elif posicao_jogador_2 == 18:
            premio = random.choice([2.5, 5000, 50000, 500000, 5000000])
            print("Jogador 2 ganhou R$", premio, "na loteria!")
        elif posicao_jogador_2 == 21:
            if relacionamento_jogador_2 == "Solteiro":
                relacionamento_jogador_2 = "Casado"
                print("Jogador 2 encontrou um novo amor e casou-se!")
            elif relacionamento_jogador_2 == "Casado":
                print("Jogador 2 caiu na casa do novo amor, mas já é casado!")
            elif relacionamento_jogador_2 == "Divorciado":
                print("Jogador 2 caiu na casa do novo amor, mas já é divorciado!")
        elif posicao_jogador_2 > 21:
            print("Jogador 2 morreu!!! Game Over!!!")
            print("Jogador 1 ganhou!")
            break

# Inicia o jogo
jogo_da_vida()
