# -*- coding: utf-8 -*-
#Made with love by Mat

### IMPORT ###
import os
import os, sys, time, os.path, ctypes, getpass
from pystyle import Center, Anime, Colors, Colorate, System
from colorama import Fore
from requests import get
#0.0.2
import requests


### COLORI E VAR ###
VERSIONETOOL = "0.0.2"
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


#0.0.2
global server
class cercamelo:
    def link():
        global server

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
	    "origin": "https://servers.fivem.net",
	    "referer": "https://servers.fivem.net/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.25"
        }

        data = requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{server['id']}", headers=headers)
        return {
        	"ip": data.json()["Data"]["connectEndPoints"][0],
        	"hostname": data.json()["Data"]["hostname"]
        }
        pass

#0.0.1
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
          {y}[{w}4{y}]{g} Ottieni ip da link (cfx.re/join/*)

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

    elif scelta == '2' or scelta == '02':
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

    elif scelta == '3' or scelta == '03':
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
    elif scelta == '4' or scelta == '04': #0.0.2
        try:
            diocane = input(f'''{y}[{b}#{y}]{w} Inserisci il link del server (esempio: cfx.re/join/vjarme):    ''')
            print(F'{y}[{b}#{y}]{w} Caricamento... Ricerca ip {diocane}')
            global server
            server = {}
            s2 = server['link'] = diocane
            server['id'] = os.path.basename(s2) 
            server['data'] = cercamelo.link()
            print(f"""{g}Operazione Completata{w}
{b}URL: {diocane} {w}---> {c}IP: {server['data']['ip']}{w}""")
            input(f"{y}[{b}#{y}]{w} Premi invio per tornare alla home")
            main()
        except Exception as errore:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Errore [{errore}]!")
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
