import random

def symbole_kręcidło():
    symbole = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbole) for _ in range(3)]

def print_kręcidło(kręcidło):
    print("\033[1;34;40m◢◤▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◥◣")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("Ⅱ   "," Ⅱ ".join(kręcidło),"   Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("◥◣▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◢◤\033[39m'")

def dostań_wypłatę(kręcidło, postaw):
    if kręcidło[0] == kręcidło[1] == kręcidło[2]:
        if kręcidło[0] == '🍒':
            return postaw * 3
        elif kręcidło[0] == '🍉':
            return postaw * 4
        elif kręcidło[0] == '🍋':
            return postaw * 5
        elif kręcidło[0] == '🔔':
            return postaw * 10
        elif kręcidło[0] == '⭐':
            return postaw * 20
        elif kręcidło[0] == '🎰':
            return postaw * 1000
        
    return 0

def spin_kręcidło():
    return symbole_kręcidło()

def skibidi():
    balans = 1000

    print("\033[1;34;40m◢◤▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◥◣")
    print("\033[1;34;40mⅡ    \033[37mSiema \033[33mSigmo👀   \033[1;34;40mⅡ ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ      \033[37mSymbole:     \033[1;34;40m Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ 🍒 🍉 🍋 🔔 ⭐ 🎰  Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print ("\033[1;34;40m◥◣▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◢◤ \033[39m'")

    while balans > 0:
        print(f"twój hajs: \033[32m${balans}\033[39m")

        postaw = input("daj tyle hajsu: ")

        if not postaw.isdigit():
            print("daj normalny numer pls")
            continue

        postaw = int(postaw)

        if postaw > balans:
            print("za biedny jesteś")
            continue

        if postaw <= 0:
            print("Nie dotykaj liczb minusowych")
            continue

        balans -= postaw

        kręcidło = spin_kręcidło()
        print("Kręcenie...\n")
        print_kręcidło(kręcidło)

        wypłatę = dostań_wypłatę(kręcidło, postaw)

        if wypłatę > 0:
            print(f"Mega Big Win omg: ${wypłatę}")
        else:
            print("unlucky :(")

        balans += wypłatę

        zagraj_ponownie = input("Chcesz Przegrać więcej hajsu? \033[32m(Y/N): \033[39m").upper()

        if zagraj_ponownie != 'Y':
            break

    print("\033[1;34;40m◢◤▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◥◣")
    print("\033[1;34;40mⅡ      \033[31m Koniec       \033[1;34;40mⅡ ")
    print("\033[1;34;40mⅡ      \033[31m Gry          \033[1;34;40mⅡ")
    print("\033[1;34;40mⅡ      \033[31m GG          \033[1;34;40m Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ 🍒 🍉 🍋 🔔 ⭐ 🎰  Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print("\033[1;34;40mⅡ                    Ⅱ")
    print ("\033[1;34;40m◥◣▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬◢◤ \033[39m")

if __name__ == '__main__':
    skibidi()

# class fg:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'

# class bg:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'

# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'