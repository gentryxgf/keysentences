from process import get_keywords, pre_processing, _word_distribution, _sentence_weight, filter_keywords, \
    pre_processing_2, pre_processing_3, pre_processing_4
from output import output_text_sentences, output_keywords, output_key_sentences, output_text, output_text_sentences1
import random


def run(path):
    random.seed()
    rand = random.randint(0, 1000)
    filename = path.split('/')[-1]
    sentence_dic, rawtext, sentence_to_folie_map = pre_processing(filename)
    output_text(rawtext, filename, rand)
    output_text_sentences(sentence_dic, filename, rand)
    keywords = get_keywords(rawtext)
    output_keywords(filter_keywords(keywords), filename, rand, 1)
    output_keywords(keywords, filename, rand)

    word_distribution = _word_distribution(sentence_dic)
    sentence_weight = _sentence_weight(word_distribution, sentence_dic)

    key_sentences = list()
    for i in range(0, 10):
        sent_num = sentence_weight[i][0]
        sentence = sentence_dic[sent_num].text
        folie = sentence_to_folie_map[sent_num]
        output_str = str(i)+": " + " folie: "+str(folie) + sentence + "\n"
        key_sentences.append(output_str)
    output_key_sentences(key_sentences, filename, rand)


def run2(path):
    random.seed()
    rand = random.randint(0, 1000)
    filename = path.split('/')[-1]
    content = pre_processing_2(filename)
    keywords = get_keywords(content)
    output_keywords(keywords, filename, rand)
    filter_keys = filter_keywords(keywords)
    output_keywords(filter_keys, filename, rand, 1)
    output_text(content, filename, rand)
    dict1 = pre_processing_3(content)
    dict2 = pre_processing_4(dict1, filter_keys)
    output_text_sentences1(dict1, filename, rand)
    output_text_sentences1(dict2, filename, rand)


run2("data/x.pdf")

