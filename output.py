
def util_file_name(filename, file, rand):
    file_split = filename.split(".")
    output_filename = file_split[0] + "_" + str(rand) + file + ".txt"
    return output_filename


"""
输出整篇文章内容
content： string
filename： 源文件名称
"""


def output_text(content, filename, rand):
    output = util_file_name(filename, "_text", rand)
    with open(output, "w", encoding="utf-8") as file:
        file.write(content)
    print("Text output success!")


"""
输出关键词
content：list
filename：源文件名称
f: 是否经过筛选
"""


def output_keywords(content, filename, rand, f=0):
    if f:
        output = util_file_name(filename, "_filter_keywords", rand)
    else:
        output = util_file_name(filename, "_keywords", rand)
    with open(output, "w", encoding="utf-8") as file:
        for word in content:
            file.write(word + '\n')
    print("Keywords output success!")


"""
输出句子
content：dict
filename:源文件名称
"""


def output_text_sentences(content, filename, rand):
    output = util_file_name(filename, "_text_sentences", rand)
    with open(output, "w", encoding="utf-8") as file:
        for key in content:
            file.write(str(key) + ": " + content[key].text + "\n")
    print("Text sentences output success!")


"""
new
"""


def output_text_sentences1(content, filename, rand):
    output = util_file_name(filename, "_text_sentences", rand)
    with open(output, "w", encoding="utf-8") as file:
        for key in content:
            file.write(str(key) + ": " + str(content[key]) + "\n")

    print("Text sentences output success!")


"""
输出关键句
content:
filename:
"""


def output_key_sentences(content, filename, rand, f=0):
    if f:
        output = util_file_name(filename, "_key_sentences_filter", rand)
    else:
        output = util_file_name(filename, "_key_sentences", rand)
    with open(output, "w", encoding="utf-8") as file:
        for sentence in content:
            file.write(sentence)
    print("Key sentences output success!")
