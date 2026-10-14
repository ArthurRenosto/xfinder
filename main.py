from modules.banners import Banners

class Main():
    
    def __init__(self):
        pass

    def menu_inicial(self):

        Banners.main_banner()
        response = int(input("[1] Import wordlists \n[2] Ports \n[3] Subdomains \n[4] Directories \n[5] OSINT \n :: "))


xfinder = Main()
xfinder.menu_inicial()

