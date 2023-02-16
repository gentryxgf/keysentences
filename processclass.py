import re
from summa import keywords
import spacy
from loadfileclass import LoadFile


class Process:
    def __init__(self, content):
        self.content = content
        self.nlp = spacy.load("en_core_web_sm")

    def get_raw_text(self):
        raw_text = ""
        for key in self.content:
            data = self.content[key]
            data = data.lower()
            data = data.replace("\n", " ", 1)
            # data = data.replace("-", "")
            if key > len(self.content) - 3:
                dl = data.split("references")
                dl = dl[0:-1]
                if len(dl) > 0:
                    data_new = ""
                    for d in dl:
                        data_new += d
                    data = data_new
                    raw_text += data + ""
                    return raw_text
            raw_text += data + " "
        return raw_text

    def get_sentences(self, raw_text):
        i = 0
        sentence_dic = {}

        data = re.sub(' +', ' ', raw_text)
        doc = self.nlp(data)
        # sentence seperation
        sentence_spans = list(doc.sents)
        for sents in sentence_spans:
            sents_str = sents.text
            sents_str = sents_str.rstrip("\r\n")
            sents_str = sents_str.replace("\n", " ")
            sents_str = sents_str.replace("-", "")
            sents_str = re.sub(' +', ' ', sents_str)
            tokenlist = self.nlp(sents_str)
            count = 0
            hasVerb = False
            hasNomen = False
            value = list()
            words = list()
            for token in tokenlist:
                # words = list()
                if token.pos_ == "VERB":
                    hasVerb = True
                if token.pos_ == "PROPN" or token.pos_ == "NOUN":
                    # hasNomen = True
                    words.append(token.text)
                count += 1

            if count > 5 and hasVerb:
                value.append(tokenlist)
                value.append(words)
                sentence_dic[i] = value
                i += 1
        return sentence_dic

    def get_filter_sentences(self, sentence_dic, filter_keys):
        filter_keys_sentences_dict = dict()
        filter_keys_set = set(filter_keys)
        for key in sentence_dic:
            value = list()
            l = list(set(sentence_dic[key][1]).intersection(filter_keys_set))
            if len(l) > 2:
                value.append(sentence_dic[key])
                value.append(l)
                filter_keys_sentences_dict[key] = value
        return filter_keys_sentences_dict

    def get_keywords(self, raw_text):
        keywords_text_rank = keywords.keywords(raw_text)
        doc = self.nlp(keywords_text_rank)
        keywords_list = list()
        for token in doc:
            if token.pos_ == "PROPN" or token.pos_ == "NOUN":
                keywords_list.append(token.text)
        return keywords_list

    def get_filter_keywords(self, keywords_list):
        my_word_list = list()
        with open("word.txt", "r", encoding='utf-8') as file:
            for line in file.readlines():
                my_word_list.append(line.split("\n")[0])
        filter_list = list(set(keywords_list).intersection(set(my_word_list)))
        return filter_list