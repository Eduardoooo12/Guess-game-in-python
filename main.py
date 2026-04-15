# começar com os imports, como o time, OS e random
from time import sleep
from random import randint
from os import system, name

# ========================================================================================================
# código pra eu usar as cores mais facilmente durante o código
# Estilos
reset = "\033[0m"
negrito = "\033[1m"
italico = "\033[3m"
sublinhado = "\033[4m"

# Cores do texto (normais)
preto = "\033[30m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
branco = "\033[37m"

# Cores do texto (brilhantes)
preto_bril = "\033[90m"
vermelho_bril = "\033[91m"
verde_bril = "\033[92m"
amarelo_bril = "\033[93m"
azul_bril = "\033[94m"
magenta_bril = "\033[95m"
ciano_bril = "\033[96m"
branco_bril = "\033[97m"

# Cores de fundo (normais)
fundo_preto = "\033[40m"
fundo_vermelho = "\033[41m"
fundo_verde = "\033[42m"
fundo_amarelo = "\033[43m"
fundo_azul = "\033[44m"
fundo_magenta = "\033[45m"
fundo_ciano = "\033[46m"
fundo_branco = "\033[47m"

# Cores de fundo (brilhantes)
fundo_preto_bril = "\033[100m"
fundo_vermelho_bril = "\033[101m"
fundo_verde_bril = "\033[102m"
fundo_amarelo_bril = "\033[103m"
fundo_azul_bril = "\033[104m"
fundo_magenta_bril = "\033[105m"
fundo_ciano_bril = "\033[106m"
fundo_branco_bril = "\033[107m"

# ========================================================================================================
# funcoes legais, como escrever devagar limpar a tela e a de "sortear" um número aleatório entre 1 e 100
# talvez essa de sortear o número, seja removida numa atualização futura do código

# função de escrever devagar


def write_slowy(text, temp=0.03, end="\n", f=print):
    for char in text:
        f(char, end="", flush=True)
        sleep(temp)
    if end:
        f(end, end="")


# função de criar menu de opções


def show_options_menu(option1, option2, option3):
    options = [option1, option2, option3]
    for c in range(3):
        write_slowy(f"{magenta}{c + 1}{reset}. {options[c]}")


# função de limpar a tela


def clear_screen():
    system("cls" if name == "nt" else "clear")


# função de criar um número aleatório


def random_number(num1=1, num2=100):
    number = randint(num1, num2)
    return number  # Modificado para retornar o número


# Função de mostrar mensagem padrão de erro


def show_main_error():
    return print(f"{vermelho}Algo deu errado, tente novamente ! {reset}")


# ========================================================================================================
# Função de mostrar aviso sobre os pontos


def show_warning():
    sleep(2)
    write_slowy(f"{amarelo} ##### ATENÇÃO #####{reset}")
    write_slowy(f"""{vermelho} Todos os pontos que você fizer nesse jogo
serão perdidos assim que ele for encerrado{reset}""")
    print()
    input(f"{verde}pressione qualquer tecla para continuar.{reset}")
    clear_screen()


# ========================================================================================================
# Função do tutorial


def show_tutorial():
    clear_screen()
    write_slowy(f"{amarelo_bril}Bem-vindo(a) ao GUESS GAME TUTORIAL...{reset}")
    sleep(2)
    write_slowy(f"{azul}Aqui você aprenderá a como jogar este jogo!{reset}")
    sleep(1)
    print()
    write_slowy(f"{verde}O objetivo do jogo é adivinhar um número secreto!{reset}")
    sleep(1.5)
    write_slowy(
        f"{ciano}Você terá um número limitado de tentativas por dificuldade:{reset}"
    )
    sleep(1)
    print()
    write_slowy(f"{verde}-> NORMAL: 10 tentativas (número entre 1-100){reset}")
    write_slowy(f"{amarelo}-> HARD: 7 tentativas (número entre 1-200){reset}")
    write_slowy(f"{vermelho}-> HARDCORE: 5 tentativas (número entre 1-500){reset}")
    sleep(2)
    print()
    write_slowy(
        f"{magenta}A cada rodada, você receberá dicas se o número é maior ou menor!{reset}"
    )
    sleep(1.5)
    print()

    while True:
        try:
            resp = int(
                input(
                    f"{verde}Pressione 1 para voltar ao menu ou 2 para fechar o jogo: {
                        reset
                    }"
                )
            )
            if resp == 1:
                write_slowy(f"{amarelo}Voltando ao menu principal...{reset}")
                sleep(1.5)
                show_menu()
                break
            elif resp == 2:
                write_slowy(f"{vermelho}Encerrando jogo...{reset}")
                sleep(2)
                write_slowy(f"{amarelo}Volte sempre :D{reset}")
                exit()
            else:
                show_main_error()
        except ValueError:
            show_main_error()


# ========================================================================================================
# Função principal do jogo


def main_game():
    clear_screen()
    write_slowy(f"{amarelo}Por favor, selecione a dificuldade:{reset}")
    print()
    print(f"{magenta}1{reset}. {verde}Normal (10 tentativas){reset}")
    print(f"{magenta}2{reset}. {amarelo}Hard (7 tentativas){reset}")
    print(f"{magenta}3{reset}. {vermelho}HARDCORE (5 tentativas){reset}")
    print(f"{magenta}4{reset}. {verde}Normal (sem limite){reset}")
    print(f"{magenta}5{reset}. {amarelo}Hard (sem limite){reset}")
    print(f"{magenta}6{reset}. {vermelho}HARDCORE (sem limite){reset}")
    print()

    while True:
        try:
            difficulty = int(
                input(f"{verde}Digite o número da dificuldade desejada: {reset}")
            )

            if difficulty == 1:  # Normal
                max_attempts = 10
                num_range = (1, 100)
                difficulty_name = "NORMAL"
                difficulty_color = verde
                break
            elif difficulty == 2:  # Hard
                max_attempts = 7
                num_range = (1, 200)
                difficulty_name = "HARD"
                difficulty_color = amarelo
                break
            elif difficulty == 3:  # Hardcore
                max_attempts = 5
                num_range = (1, 500)
                difficulty_name = "HARDCORE"
                difficulty_color = vermelho
                break
            elif difficulty == 4:  # Normal sem limite
                max_attempts = 9999
                num_range = (1, 100)
                difficulty_name = "Normal (sem limites)"
                difficulty_color = verde
                break
            elif difficulty == 5:  # Hard sem limite
                max_attempts = 9999
                num_range = (1, 200)
                difficulty_name = "Hard (sem limite)"
                difficulty_color = amarelo
                break
            elif difficulty == 6:  # Hardcore sem limite
                max_attempts = 9999
                num_range = (1, 500)
                difficulty_name = "Hardcore (sem limite)"
                difficulty_color = vermelho
                break
            else:
                show_main_error()
        except ValueError:
            show_main_error()

    # Iniciar o jogo com as configurações escolhidas
    start_game_round(max_attempts, num_range, difficulty_name, difficulty_color)


# ========================================================================================================
# Função que executa uma rodada do jogo


def start_game_round(max_attempts, num_range, difficulty_name, difficulty_color):
    clear_screen()
    secret_number = random_number(num_range[0], num_range[1])
    attempts = 0
    points = 0

    # Verificar se é modo sem limite
    is_unlimited = max_attempts == 9999

    write_slowy(
        f"{difficulty_color}     DIFICULDADE: {difficulty_name}{
            ' ' * (15 - len(difficulty_name))
        }{reset}"
    )
    write_slowy(
        f"{difficulty_color}     NÚMERO ENTRE {num_range[0]} E {num_range[1]}         {
            reset
        }"
    )

    if is_unlimited:
        write_slowy(f"{difficulty_color}     TENTATIVAS: SEM LIMITES{reset}")
    else:
        write_slowy(
            f"{difficulty_color}     TENTATIVAS: {max_attempts}{
                ' ' * (12 - len(str(max_attempts)))
            }              {reset}"
        )
    print()
    sleep(2)

    write_slowy(
        f"{verde_bril}Vamos começar! Tente adivinhar o número secreto...{reset}"
    )
    print()

    while True if is_unlimited else attempts < max_attempts:
        if not is_unlimited:
            attempts_left = max_attempts - attempts
            write_slowy(f"{ciano}Tentativas restantes: {attempts_left}{reset}")

        try:
            guess = int(input(f"{verde}Digite seu palpite: {reset}"))

            if guess < num_range[0] or guess > num_range[1]:
                write_slowy(
                    f"{vermelho}Por favor, digite um número entre {num_range[0]} e {
                        num_range[1]
                    }!{reset}"
                )
                continue

            attempts += 1

            if guess == secret_number:
                # Calcular pontos baseado nas tentativas restantes
                if is_unlimited:
                    points = attempts * 1
                    points_text = f"{points} pontos! "
                else:
                    points = (max_attempts - attempts + 1) * 10
                    points_text = f"{points} pontos!"

                clear_screen()
                write_slowy(
                    f"{verde_bril}               PARABÉNS!                 {reset}"
                )
                write_slowy(
                    f"{verde_bril}             VOCÊ ACERTOU!                  {reset}"
                )
                print()
                write_slowy(f"{amarelo}Número secreto: {secret_number}{reset}")
                write_slowy(f"{verde}Pontuação: {points_text}{reset}")
                write_slowy(f"{ciano}Tentativas utilizadas: {attempts}{reset}")
                print()

                # Perguntar se quer jogar novamente
                play_again()
                return

            # Dicas
            if guess < secret_number:
                write_slowy(
                    f"{vermelho}-> O número secreto é MAIOR que {guess}!{reset}"
                )
            else:
                write_slowy(f"{azul}-> O número secreto é MENOR que {guess}!{reset}")

            print()

            if not is_unlimited and attempts == max_attempts:
                clear_screen()
                write_slowy(
                    f"{vermelho_bril}              GAME OVER!                {reset}"
                )
                write_slowy(
                    f"{vermelho_bril}             VOCÊ PERDEU!                   {
                        reset
                    }"
                )
                print()
                write_slowy(f"{amarelo}Número secreto: {secret_number}{reset}")
                write_slowy(
                    f"{vermelho}Você usou todas as {max_attempts} tentativas!{reset}"
                )
                print()

                play_again()
                return

        except ValueError:
            write_slowy(f"{vermelho}Por favor, digite um número válido!{reset}")
            print()


# ========================================================================================================
# Função para jogar novamente


def play_again():
    while True:
        try:
            resp = int(
                input(
                    f"{verde}Deseja jogar novamente?{reset}\n{magenta}1{reset} - SIM\n{
                        magenta
                    }2{reset} - NÃO (Voltar ao menu)\n{magenta}3{
                        reset
                    } - SAIR DO JOGO\n{verde}Escolha: {reset}"
                )
            )

            if resp == 1:
                main_game()
                break
            elif resp == 2:
                show_menu()
                break
            elif resp == 3:
                write_slowy(f"{vermelho}Encerrando jogo...{reset}")
                sleep(2)
                write_slowy(f"{amarelo}Volte sempre :D{reset}")
                sleep(2)
                exit()
            else:
                show_main_error()
        except ValueError:
            show_main_error()


# ========================================================================================================
# Menu principal


def show_menu():
    clear_screen()
    show_warning()

    write_slowy(f"{verde_bril}==================================={reset}")
    write_slowy(f"{verde_bril}       BEM-VINDO AO GUESS GAME!      {reset}")
    write_slowy(f"{verde_bril}==================================={reset}")
    print()
    sleep(1)
    write_slowy("A seguir, as opções de menu...")
    sleep(1)
    print()
    print(f"{magenta}1{reset}. Iniciar Jogo")
    print(f"{magenta}2{reset}. Abrir Tutorial")
    print(f"{magenta}3{reset}. Fechar Jogo")
    print()

    while True:
        try:
            option_response = int(input(f"{verde}Qual opção desejas?{reset} "))
            if option_response == 1:
                main_game()
                break
            elif option_response == 2:
                show_tutorial()
                break
            elif option_response == 3:
                write_slowy(f"{vermelho}Encerrando jogo...{reset}")
                sleep(2)
                write_slowy(f"{amarelo}Volte sempre :D{reset}")
                exit()
            else:
                show_main_error()
        except ValueError:
            show_main_error()


# ========================================================================================================
# Iniciar o jogo resenha suprema
if __name__ == "__main__":
    show_menu()
