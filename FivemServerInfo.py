# -*- coding: utf-8 -*-
#Made with love by Mat

### IMPORT ###
import os
import os, sys, time, os.path, ctypes, getpass
from pystyle import Center, Anime, Colors, Colorate, System
from colorama import Fore
from requests import get

### COLORI E VAR ###
VERSIONETOOL = "0.0.1 [BETA]"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX


### SCHERMATA ###
def impostatitolo(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | github.com/itsmat")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | github.com/itsmat\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def titolohome():
    print(f"""\n\n
            $$\      $$\            $$\            $$$$$$\                                                          $$$$$$\            $$$$$$\           
            $$$\    $$$ |           $$ |          $$  __$$\                                                         \_$$  _|          $$  __$$\          
            $$$$\  $$$$ | $$$$$$\ $$$$$$\         $$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\          $$ |  $$$$$$$\  $$ /  \__|$$$$$$\  
            $$\$$\$$ $$ | \____$$\\_$$  _|        \$$$$$$\  $$  __$$\ $$  __$$ \$$\  $$  |$$  __$$\ $$  __$$\          $$ |  $$  __$$\ $$$$\    $$  __$$\ 
            $$ \$$$  $$ | $$$$$$$ | $$ |           \____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / $$$$$$$$ |$$ |  \__|        $$ |  $$ |  $$ |$$  _|   $$ /  $$ |
            $$ |\$  /$$ |$$  __$$ | $$ |$$\       $$\   $$ |$$   ____|$$ |       \$$$  /  $$   ____|$$ |              $$ |  $$ |  $$ |$$ |     $$ |  $$ |
            $$ | \_/ $$ |\$$$$$$$ | \$$$$  |      \$$$$$$  |\$$$$$$$\ $$ |        \$  /   \$$$$$$$\ $$ |            $$$$$$\ $$ |  $$ |$$ |     \$$$$$$  |
            \__|     \__| \_______|  \____/        \______/  \_______|\__|         \_/     \_______|\__|            \______|\__|  \__|\__|      \______/ 
\n""".replace('█', f'{g}█{y}'))

banner = r"""
░█████╗░░█████╗░██████╗░██╗░█████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗
██║░░╚═╝███████║██████╔╝██║██║░░╚═╝███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║
██║░░██╗██╔══██║██╔══██╗██║██║░░██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║
╚█████╔╝██║░░██║██║░░██║██║╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░
"""[1:]

def transizione():
    clear()
    caricamento()
    clear()

def caricamento():
	carattere = ['|', '/', '-', '\\']
	for i in carattere+carattere+carattere:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Caricamento... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

global ipserver
ipserver = 'Nessun server impostato'
global portaserver
portaserver = '30120'
def main():
    global ipserver
    global portaserver
    impostatitolo(f"Mat Server Info Tool {VERSIONETOOL} - Caricamento")
    #System.Size(160, 40) #120, 30
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1)
    clear()
    impostatitolo(f"Mat Server Info Tool {VERSIONETOOL}")
    titolohome()
    print(f"""      {y}[{b}+{y}]{g} Main:                                                                            {y}[{b}+{y}]{c} Settings:
          {y}[{w}1{y}]{g} Info server                                                                      {y}[{w}10{y}]{c} Imposta porta server (default 30120)
          {y}[{w}2{y}]{g} Lista players                                                                    {y}[{w}11{y}]{c} Imposta ip server  
          {y}[{w}3{y}]{g} Lista players con identifiers        

                                                                                     {m}Made by Mat#3616 | github.com/itsmat
                                                                                     {m}IP Server     : {b}{ipserver}
                                                                                     {m}Porta         : {b}{portaserver}
\t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global scelta
    scelta = input(f"""{y}[{b}#{y}]{w} : """)
    if scelta == '1' or scelta == '01':
        if ipserver != 'Nessun server impostato':
            try:
                dynamic = get(f'http://{ipserver}:{portaserver}/dynamic.json', timeout=5)
                print('Attendi...')
                getdynamic = dynamic.json()
                hostname = getdynamic["hostname"]
                online = str(getdynamic["clients"])
                massimi = str(getdynamic["sv_maxclients"])
                iv = str(getdynamic["iv"])
                gametype = str(getdynamic["gametype"])
                mapname = str(getdynamic["mapname"])

                print(f'''
{y}Info ricavate:{m} github.com/itsmat {w}

HostName: {hostname}
Players: {online}/{massimi}
IV: {iv}
GameType: {gametype}
MapName: {mapname}''')
                input(f"{y}[{b}#{y}]{w} Premi invio per tornare alla home")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP Server mancante [tasto 11 nella home]!")
            main()

    if scelta == '2' or scelta == '02':
        if ipserver != 'Nessun server impostato':
            try:
                players = get(f'http://{ipserver}:{portaserver}/players.json', timeout=5)
                print('Attendi...')
                getplayers = players.json()
                for player in getplayers:
                    print(f"{y}[{player['id']}] {w}| {g}{player['name']} {w}| {c}Ping:{player['ping']}{w}")

                input(f"{y}[{b}#{y}]{w} Premi invio per tornare alla home")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP Server mancante [tasto 11 nella home]!")
            main()

    if scelta == '3' or scelta == '03':
        if ipserver != 'Nessun server impostato':
            try:
                players = get(f'http://{ipserver}:{portaserver}/players.json', timeout=5)
                print('Attendi...')
                getplayers = players.json()
                for player in getplayers:
                    print(f"{y}[{player['id']}] {w}| {g}{player['name']} {w}| {c}{player['identifiers']}{w}")

                input(f"{y}[{b}#{y}]{w} Premi invio per tornare alla home")
                main()
            except Exception as errore:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
                main()
        else:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} IP Server mancante [tasto 11 nella home]!")
            main()

    elif scelta == '10' or scelta == '010':
        transizione()
        diocaporta = input(f'''{y}[{b}#{y}]{w} Inserisci la porta del server:    ''')
        portaserver = diocaporta
        main()
    elif scelta == '11' or scelta == '011':
        transizione()
        diocane = input(f'''{y}[{b}#{y}]{w} Inserisci l'ip NUMERICO del server:    ''')
        ipserver = diocane
        main()
    elif scelta == 'exit' or scelta == 'chiudi':
        transizione()
        sys.exit()
    else:
        clear()
        main()


main()
