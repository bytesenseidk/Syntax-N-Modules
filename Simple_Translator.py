from tabulate import tabulate
from googletrans import Translator

class Simple_Translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.cursor = Translator(service_urls=["translate.google.com"])
    
    def __repr__(self):
        translated = self.cursor.translate(self.word, 
                            dest=self.language).text

        data = [["Language:", "Word or Sentence:"],
                ["English", self.word],
                ["Russian", str(translated)]]
        
        table = str(tabulate(data, headers="firstrow", tablefmt="grid"))
        return table

if __name__ == "__main__":
    translate = input(r"Enter word or Sentence: ")
    language = "ru"
    print(Simple_Translator(translate, language))

