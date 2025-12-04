import socket
from utils.wordlist_importer import WordlistImporter

class SubdomainScanner:
    def __init__(self):
        self.importer = WordlistImporter()

    def run(self):
        domain = input("domain: ")
        filename = input("Select the wordlist: ")

        words = self.importer.load_wordlist(filename)

        if not words:
            print("Empty wordlist or cannot load file.")
            return

        for word in words:
            sub = f"{word}.{domain}"
            try:
                socket.gethostbyname(sub)
                print(f"[FOUND] {sub}")
            except:
                pass