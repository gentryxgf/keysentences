import spacy
import re
from summa import keywords
import operator
from collections import defaultdict

from getdata import getTextFromPDF, getTextFromPDF_2
from output import output_text, output_text_sentences1

nlp = spacy.load("en_core_web_sm")


def get_keywords(text):
    keywords_text_rank = keywords.keywords(text)
    doc = nlp(keywords_text_rank)
    keywords_list = list()
    for token in doc:
        if token.pos_ == "PROPN" or token.pos_ == "NOUN":
            keywords_list.append(token.text)
    return keywords_list


def filter_keywords(keywords_list):
    my_word_list = list()
    with open("word.txt", "r", encoding='utf-8') as file:
        for line in file.readlines():
            my_word_list.append(line.split("\n")[0])
    filter_list = list(set(keywords_list).intersection(set(my_word_list)))
    return filter_list


def _word_distribution(sentence_processed):
    """
        Compute word probabilistic distribution
    """
    word_distr = defaultdict(int)
    word_count = 0.0
    for k in sentence_processed:
        for word_l in sentence_processed[k]:
            word = word_l.text
            word_distr[word] += 1
            word_count += 1
    for word in word_distr:
        word_distr[word] = word_distr[word] / word_count
    return word_distr


def _sentence_weight(word_distribution, sentence_processed):
    """Compute weight with respect to sentences
    Args:
            word_distribution: probabilistic distribution of terms in document
            sentence_processed: dict of processed sentences generated by pre_processing
    Return:
            sentence_weight: dict of weight of each sentence
    """
    sentence_weight = {}

    for sentence_id in sentence_processed:
        for word_l in sentence_processed[sentence_id]:
            word = word_l.text
            if word_distribution[word] and sentence_id in sentence_weight:
                sentence_weight[sentence_id] += word_distribution[word]
            else:
                sentence_weight[sentence_id] = word_distribution[word]

        sentence_weight[sentence_id] = sentence_weight[
            sentence_id] / float(len(sentence_processed[sentence_id]))

    sentence_weight = sorted(sentence_weight.items(), key=operator.itemgetter(1), reverse=True)
    return sentence_weight


def pre_processing(source_text):
    data, pdfFileObj, data_folie = getTextFromPDF(source_text)
    sentence_folien_map = {}
    folien_num = 1
    i = 0
    sentence_dic = {}
    raw_text = ""

    for key in data_folie:
        data = data_folie[key]
        # todo highlight text in outputfile
        data = data.lower()
        data = data.replace("\n", " ", 1)
        raw_text += data + " "

        data = re.sub(' +', ' ', data)
        doc = nlp(data)

        # sentence seperation
        sentence_spans = list(doc.sents)

        for sents in sentence_spans:
            sents_str = sents.text
            sents_str = sents_str.rstrip("\r\n")
            sents_str = sents_str.replace("\n", " ")

            sents_str = re.sub(' +', ' ', sents_str)
            tokenlist = nlp(sents_str)
            count = 0
            hasVerb = False
            hasNomen = False
            for token in tokenlist:
                if token.pos_ == "VERB":
                    hasVerb = True
                #if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                #    hasNomen = True
                count += 1

            if count > 5 and hasVerb:
                sentence_dic[i] = tokenlist
                sentence_folien_map[i] = folien_num
                i += 1

        folien_num += 1

    return sentence_dic, raw_text, sentence_folien_map


def pre_processing_2(source_text):
    raw_text = ""
    new_data_folie = {}
    data_folie = getTextFromPDF_2(source_text)
    for key in data_folie:
        data = data_folie[key]
        data = data.lower()
        data = data.replace("\n", " ", 1)
        # data = data.replace("-", "")
        if key > len(data_folie) - 3:
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
        new_data_folie[key] = data
    return raw_text


def pre_processing_3(raw_text):

    i = 0
    sentence_dic = {}

    data = re.sub(' +', ' ', raw_text)
    doc = nlp(data)
    # sentence seperation
    sentence_spans = list(doc.sents)
    for sents in sentence_spans:
        sents_str = sents.text
        sents_str = sents_str.rstrip("\r\n")
        sents_str = sents_str.replace("\n", " ")
        sents_str = sents_str.replace("-", "")
        sents_str = re.sub(' +', ' ', sents_str)
        tokenlist = nlp(sents_str)
        count = 0
        hasVerb = False
        hasNomen = False
        value = list()
        words = list()
        for token in tokenlist:
            #words = list()
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

def pre_processing_4(sentence_dic, filter_keys):
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


if __name__ == "__main__":
    path = "data/1.pdf"
    filename = path.split('/')[-1]
    content = pre_processing_2(filename)
    output_text(content, filename, 88888)
    dict = pre_processing_3(content)
    output_text_sentences1(dict, filename, 88888)