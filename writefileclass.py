import random
import os

from loadfileclass import LoadFile


class WriteToTxt:
    def __init__(self, path):
        self.path = path
        random.seed()
        self.rand = random.randint(0, 1000)
        self.direct = self.makedir()

    def makedir(self):
        cwd = os.path.abspath('.')
        filename = self.path.split('/')[-1].split('.')[0]
        dirname = filename + "_" + str(self.rand)
        direct = cwd + "\\" + dirname
        os.makedirs(direct, exist_ok=True)
        print(direct + "   Created success!")
        return direct

    def write_text(self, content):
        txt_name = "text.txt"
        with open(self.direct + "\\" + txt_name, "w", encoding='utf-8') as file:
            file.write(content)
        print(str(self.rand) + txt_name + "output success!")

    def write_keywords(self, keys, f=0):
        if f:
            txt_name = "keywords_filter.txt"
        else:
            txt_name = "keywords.txt"
        with open(self.direct + "\\" + txt_name, "w", encoding='utf-8') as file:
            for word in keys:
                file.write(word + '\n')
        print(str(self.rand) + txt_name + "output success!")

    def write_sentences(self, sentences, f=0):
        if f:
            txt_name = "sentences_filter.txt"
        else:
            txt_name = "sentences.txt"
        with open(self.direct + "\\" + txt_name, "w", encoding='utf-8') as file:
            for key in sentences:
                file.write(str(key) + ": " + str(sentences[key]) + "\n")
        print(str(self.rand) + txt_name + "output success!")