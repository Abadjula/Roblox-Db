try:
    import requests
    from bs4 import BeautifulSoup
    from colorama import Fore
    import os

    def clear():
        if os.name == "nt":
            os.system("cls")
            os.system("title RobloxDb")
        else:
            os.system("clear")

    clear()

    zero = 0

    GREEN = Fore.GREEN
    MAGENTA = Fore.MAGENTA
    GREY = Fore.LIGHTBLACK_EX
    RED = Fore.RED
    LIGHTBLUE = Fore.LIGHTBLUE_EX
    RESET = Fore.RESET

    while True:

        zero += 1

        Username = []
        DisplayName = []
        About = []

        url = f"https://www.roblox.com/users/{zero}/profile"
        s = requests.Session()
        r = s.get(url).text

        soup = BeautifulSoup(r, "html.parser")

        RobloxUsernames = soup.find_all("h2", {"class", "profile-name text-overflow"})
        RobloxDisplayNames = soup.find_all("div", {"class": "profile-display-name font-caption-body text text-overflow"})
        RobloxABouts = soup.find_all("span", {"class": "profile-about-content-text linkify"})

        for RobloxUsername in RobloxUsernames:
            Username.append(RobloxUsername.get_text())
        for RobloxDisplayName in RobloxDisplayNames:
            DisplayName.append(RobloxDisplayName.get_text())
        for RobloxAbout in RobloxABouts:
            About.append(RobloxAbout.get_text())

        if Username == []:
            print(f"{MAGENTA}[{RESET}{GREEN}*{RESET}{MAGENTA}]{RESET}{LIGHTBLUE}Status:{RESET} [{RED}BANNED{RESET}]")
            #input("\nEnter any key to exit. . .")
        else:
            print(f"\n{MAGENTA}[{RESET}{GREEN}*{RESET}{MAGENTA}]{RESET}{LIGHTBLUE}Username:{RESET}{GREY}", "".join(Username), f"{RESET}")
            print(f"{MAGENTA}[{RESET}{GREEN}*{RESET}{MAGENTA}]{RESET}{LIGHTBLUE}Display Name:{RESET}{GREY}", "".join(DisplayName), f"{RESET}")
            print(f"{MAGENTA}[{RESET}{GREEN}*{RESET}{MAGENTA}]{RESET}{LIGHTBLUE}Id:{RESET}{GREY}", zero, f"{RESET}")
            print(f"{MAGENTA}[{RESET}{GREEN}*{RESET}{MAGENTA}]{RESET}{LIGHTBLUE}About:{RESET}{GREY}", "".join(About), f"{RESET}\n")
            #input("\nEnter any key to countinue. . .")
except Exception as error:
    print(f"[{RED}ERROR{RESET}]{GREY} {error}{RESET}")
    input("\nEnter any key to exit. . .")