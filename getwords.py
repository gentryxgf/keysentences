from lxml import etree
import requests


def get_html(search_word):
    #basic_url = 'https://relatedwords.io/'
    basic_url = 'https://github.com/jiqizhixin/Artificial-Intelligence-Terminology-Database/blob/master/data/'
    url = basic_url + str(search_word) + '.md'
    rep = requests.get(url)
    html = etree.HTML(rep.text)
    words = html.xpath('//*[@id="readme"]/article/table/tbody/tr/td[2]/text()')
    return words


def get_html_2(search_word):
    basic_url = 'https://relatedwords.org/relatedto/'
    url = basic_url + str(search_word)
    rep = requests.get(url)
    html = etree.HTML(rep.text)
    words = html.xpath('//*[@id="results-area"]/div/a/text()')
    return words

def writefile(words, file_name):
    output_word = list()
    for word in words:
        ws = str(word).split()
        for w in ws:
            output_word.append(w)

    res = list(set(output_word))
    with open(file_name, 'a', encoding='utf-8') as f:
        for word in res:
            f.write(word+'\n')
    print("Write over!")


if __name__ == "__main__":
    char = []
    for i in range(65, 91):
        char.append(chr(i))
    file = "word1.txt"
    for c in char:
        writefile(get_html(c), file)
