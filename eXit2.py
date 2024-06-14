#!/bin/python3

ascii = '''
████████████████████████████████████████████████▓▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▓╨╨╨╨╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╙╟▓▓██▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌``¡≥≥▒▒▒≥≥≥▒≥≥≥▒▒▒Q░░░░░▒Q░Q░▒▒▒▒▒≥▒≥▒▒≥≥≥≥░?^╠╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌--░╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣╣╬╬╬╬╬╬╬╬╬╢╬╬╠╠╠╠▒▒▒╫▒--╠╫██▓▓▓▓▓▓▓▓▓███
█████████████████▌(ⁿ;╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╠╠╠╠╠╠╠╠╬▒ƒⁿ╠╣▓▓█████▓▓█████
█████████████████▌-,»░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▒▒▒╬▒Γ,░╬▓▓██▓▓▓▓▓█████
█████████████████▌⌐¬;╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╩╩╩╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░⌐¬╚╣▓▓▓▓▓▓▓▓▓██▓▓▓
█████████████████▌""7▒╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬∩. .╠╬╬╬╬╬╬╬╬╬╬▒▒▒▒▒▒▒▒╬▒b"≤╟█▓▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌~~~┘~╙╙╙╙╙╙╙║╫╫╫╫░~~~~~║╫╫╫╫╢╢╢╢╢╠▒▒▒▒▒▒▒▒╫▒~~5╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌`````````````╙╙╙╙?````^╠╢╬╬╬╬╬╬╬╠╠▒▒▒▒▒▒▒▒╬▒░`5╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌-----------------------║╫╫╬╢╢╢╢╢╠▒▒▒▒▒▒▒▒▒╫▒--░╬╬╣▓▓▓▓▓████▓▓▓
█████████████████▌;;;ⁿ                 ,ƒ╠╬╬╬╬╬╬╬╬╬╠╠╠╠╠╠╠╠░╬▒░;░╠╬╬╬╬▓██████▓▓▓
█████████████████▓ΓΓΓΓ                 '░╠╬╬╬╬╬╬╬╬╬▒▒▒▒▒▒▒▒▒╬▒ΓΓ░╬╬╬╬╬█████▓▓▓▓▓
█████████████████▌¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬;╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╚░╬░⌐¬░╟████▓▓▓██▓▓▓▓╬
█████████████████▌"""". .........  ...777╠╬╬╬╬╬╬╬▒▒▒▒▒▒▒▒▒▒ñ╠▒""ñ╟▓▓▓▓██▓▓▓▓▓╬╬╬
█████████████████▌~~~~~~~~~~~~~~~~~~~»»~∞║╫╫╫╢╢╢╢▒▒▒▒▒▒▒▒▒░░╠░~~░╫▓▓██▓▓▓▓▓╫╫▓██
█████████████████▌````````````````??????░╟▓╫╬╬╬╬╬▒▒▒▒▒▒▒▒▒▒▒╠▒░`3╫██▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌----------------------Å╫█▓╫╢╢╢▒▒▒▒▒▒▒▒▒░░░╠▒--░╫▓▓██▓▓▓▓▓▓▓▓▓▓
█████████████████▌;;;ⁿ          ;ƒƒƒƒƒƒ;≥╟█▓╬╬╬╬╠╠╠╠╠╠▒░╠░░░╠░ƒ;░╟██▓▓▓▓▓▓▓▓▓▓▓▓
█████████████████▌----          -======░╚╟▓▓╬╬╬╬▒▒▒▒▒╩▒░▒░░░╠▒=-░╟██▓▓███▓▓▓▓▓▓▓
█████████████████▌¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬j╠╬╬╬╬╬╬╬╬╬╬╩▒░░╩░░░╠░⌐¬░╟███████▓▓▓▓▓█▓
█████████████████▌........""7.:"""""""""l╠╬╬╬╬╬╬╬╬▒▒▒▒▒▒▒▒▒▒╠▒".⌠╟███████▓▓▓▓▓▓▓
█████████████████▌~~~~»»~~~~~~~~~~~~~ⁿⁿⁿⁿ║╢╢╢╢╢╢▒╩▒▒╚╙░░░░░░╠░~~≤╫███████▓▓▓▓▓▓▓
█████████████████▌^^^^?????????????¿````^╠╬╬╬╬▒▒▒▒▒▒▒▒▒▒▒▒▒▒╠▒░^5╫█████▓▓▓▓▓▓▓▓▓
█████████████████▌----~~------------~~~~-║╫╢╢╢╢╠╠╠╠╠╚╚╚╚╚▒░▒╠▒--░╫█████████▓▓╬╢╢
█████████████████▌;;;;,                ,;╠╬╬╬╬╠╠╠╠╠░░░░░░░░░╠░░;╠╫█████████▓▓╬╬╬
█████████████████▌-----------------------╠╬╬╬╬╬▒▒▒▒▒░░░░░░░░╠░░-░╣███████▓▓█████
█████████████████▌¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬╠╬╬╬╬╬╬╬╬╬░░░░░░░░░╠░¬¬╠╣██████████████
█████████████████▌.....                ..╠╬╬╬╬╬▒▒▒▒▒▒▒▒▒▒▒▒▒╠▒..ñ╟██████████████
█████████████████▌~~~~~~~~~~~~~~~~~~~~~~~╠╫╫╬╢╠╠▒▒▒▒▒░░░░░░░╠░~~░╫██████████████
█████████████████▌^^^^``````````````````^╠╬╬╬╬╬╬╠▒▒▒▒▒▒▒▒▒▒▒╠▒^^3╫████████████▓▓
█████████████████▌----──────────────────-║╫╫╫╫╫╫╫╫▒▒▒▒▒▒▒░░░╠▒--¡╫██████████████
██████████████████░((;ⁿⁿ;ⁿ;(;ⁿⁿ((;ⁿⁿⁿⁿⁿ;░╟▓▓▓▓▓╬╬╬╬╬╬╬╬╠╠░░░╠░░(░╫██████████████
██████████████████░---------------------░╟▓▓▓▓███▓▓▓▓╬╬╬╬╬▒▒╬░░-░╟██████████████
██████████████████▒╔╔╦▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓▓▓▓▓▓▓▓▓████████▓▓▓▒Q╔╔╣██████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
███████████████████████████████▓╫╫╫╫█████╫╫╫╫▓██████████████████████████████████
███████████████████╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╣█████████████╬╬╬╬██████████████████
█████████████████╬╬╬▓███▓╬╬╬╣████▓╬╬╬╬╬╬╬╬╬███████▓╬╬╬╬██▓▓╬╬╬╬╣▓▓██████████████
██████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣████▓╬╬╬╬╬╬╬╬╬████████╬╬╬╬╬█████╬╬╬╬███████████████
█████████████╬╬╬╬▓███████████████╬╬╬╬╬╬╬╬╬╬╬███████▓╬╬╬╬█████▓╬╬╬╬╬█████████████
███████████▓╬╬╬╬╬███╬╬╬╬╬╣█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██████╬╬╬╬╬╬████▓╬╬╬╬╣████████████
██████████╬╬╬╬╬╬╬╬╬╬╬╬╬▓▓████╬╬╬╬╬╬╬▓██╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬██████▓╬╬╬╬╬██████████
█████████████╫╫╫╫╫╫╫██████╬╫╫╫╫╫╫╫╫█████▓╫╫╫╫╫╫╫╢█████╫╫╫╫╫████████╫╫╫╫╫╫╫╢█████
██████████████████████████╬╬╬╬╬╬╬▓███████▓╬╬╬╬╬╬╬██████████████████████▓▓▓██████
███████████████████████▓╬╬╬╬╬╬╬▓██████████╬╬╬╬╬╬╬╬╬╬████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████
'''
print(ascii)
def print_ascii_art():
    print(ascii)

mensagem_secreta = "Você encontrou uma mensagem secreta: 'Eu amo você'."

def print_ascii_art():
    print(ascii)

def start_game():
    print_ascii_art()
    start_again()

def start_again():
    input('Pressione Enter para continuar...')
    trapped()

def trapped():
    print("Você está preso em uma masmorra com seu amigo." + "\n" + "Você vê um barril. O que você faz?")
    action = input(">")
    if action.lower() == "move barrel":
        dungeon()
    else:
        print("Você não pode fazer isso aqui.")
        trapped()

def dungeon():
    print("O barril rola para o lado e você encontra um túnel secreto." + "\n" + "O que você faz?")
    action = input(">")
    if action.lower() == "enter tunnel":
        bye()
    else:
        print("Você não pode fazer isso aqui.")
        dungeon()

def bye():
    print("Você começa a escapar, mas seu amigo está muito fraco para ir com você. Eles lhe entregam uma nota." + "\n" + "O que você faz?")
    action = input(">")
    if action.lower() == "read note":
        read_note()
    elif action.lower() == "lit a match":
        lit_match()
    else:
        print("Você não pode fazer isso aqui.")
        bye()

def read_note():
    global match_lit
    if match_lit:
        print("Você lê a nota e vê que ela diz: 'Não me deixe aqui'." + "\n" + "O que você faz?")
        action = input(">")
        if action.lower() == "stay":
            stay()
        elif action.lower() == "leave":
            leave()
        else:
            print("Você não pode fazer isso aqui.")
            read_note()
    else:
        print("Está muito escuro para ler a nota.")
        bye()

def lit_match():
    global match_lit
    match_lit = True
    print("Você acende um fósforo e agora pode ver melhor.")
    bye()

match_lit = False

def stay():
    print(mensagem_secreta)
    
def leave():
    print("Você decide deixar seu amigo para trás e continuar sozinho." + "\n" + "Você rasteja através do túnel e ele leva a uma praia.")
    action = input(">")
    if action.lower() == "look":
        look()
    else:
        print("Você não pode fazer isso aqui.")
        leave()

def look():
    print("Na água você vê um barco." + "\n" + "O que você faz?")
    action = input(">")
    if action.lower() == "get on boat":
        congrats()
    else:
        print("Você não pode fazer isso aqui.")
        look()

def congrats():
    print("Parabéns, você está indo para um novo mundo!." + "\n" + "Você quer jogar novamente?")
    action = input(">")
    if action.lower() == "yes":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        quit()

start_game()
