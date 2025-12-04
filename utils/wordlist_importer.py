import os
import shutil

class WordlistImporter:
    def __init__(self):
        self.wordlists = os.path.join("utils", "wordlists")
        os.makedirs(self.wordlists, exist_ok=True)

    def importer(self):
        path = input("Specify the path to the wordlist or add it manually in xfinder/utils/wordlists\n\n:: ")

        if not os.path.exists(path):
            print("File not found.")
            return None

        filename = os.path.basename(path)
        dest_path = os.path.join(self.wordlists, filename)

        try:
            shutil.copy(path, dest_path)
            print(f"Wordlist imported to: {dest_path}")
        except Exception as e:
            print(f"Error copying file: {e}")
            return None

        return dest_path

    def load_wordlist(self, filename):
        filepath = os.path.join(self.wordlists, filename)

        if not os.path.exists(filepath):
            print("Wordlist not found.")
            return []

        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines()]