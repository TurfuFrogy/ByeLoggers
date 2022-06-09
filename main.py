import requests, os, ctypes, itertools, time, threading
from colorama import Fore, init; init(autoreset=True, convert=True)

class ByeLoggers:
    def __init__(self):
        if os.name == "nt":
            os.system("mode con: cols=138 lines=30")

        self.tLocker = threading.Lock()
        self.session = requests.Session()

        self.proxiesScraped = False

        self.sent = 0

    def title(self, title: str):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"ByeLoggers | By Frogy | {title}")
        else:
            print(f"\33]0;ByeLoggers | By Frogy | {title}\a", end="", flush=True)

    def logo(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print(f"""{Fore.LIGHTMAGENTA_EX}
                                           ____             __                                    
                                          / __ )__  _____  / /   ____  ____ _____ ____  __________
                                         / __  / / / / _ \/ /   / __ \/ __ `/ __ `/ _ \/ ___/ ___/
                                        / /_/ / /_/ /  __/ /___/ /_/ / /_/ / /_/ /  __/ /  (__  ) 
                                       /_____/\__, /\___/_____/\____/\__, /\__, /\___/_/  /____/  
                                             /____/                 /____//____/                  
                                                             {Fore.LIGHTCYAN_EX}An IP Logger Spammer by Frogy

{Fore.RESET}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
        """)

    def scrapeProxies(self):
        while True:
            self.proxies = itertools.cycle(requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all").text.splitlines())
            self.proxiesScraped = True
            
            time.sleep(10)

    def stats(self):
        self.logo()

        while True:
            self.title(f"{self.url} have been spammed {self.sent} times")

            print(f"{Fore.LIGHTMAGENTA_EX}{self.sent} {Fore.LIGHTYELLOW_EX}requests sent.", end="\r")

            time.sleep(1)

    def spam(self):
        while True:
            try:
                proxy = next(self.proxies)

                send = self.session.get(self.url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
                }, proxies={
                    "http": f"socks4://{proxy}",
                    "https": f"socks4://{proxy}"
                })

                self.sent += 1
            except:
                pass

    def starter(self):
        self.title("Initialization")

        self.logo()

        self.url = input(f"{Fore.LIGHTYELLOW_EX}Please enter the IP Logger URL.\n\n{Fore.RESET}~# ")

        while True:
            try:
                self.logo()

                threadCount = int(input(f"{Fore.LIGHTYELLOW_EX}Please enter the number of threads (suggested: 1000).\n\n{Fore.RESET}~# "))

                break
            except KeyboardInterrupt:
                exit()
            except:
                pass

        self.title("Starting")

        threading.Thread(target=self.scrapeProxies).start()

        while not self.proxiesScraped:
            time.sleep(0.1)

        threading.Thread(target=self.stats).start()

        for _ in range(threadCount):
            threading.Thread(target=self.spam).start()

if __name__ == "__main__":
    try:
        ByeLoggers().starter()
    except KeyboardInterrupt:
        exit()