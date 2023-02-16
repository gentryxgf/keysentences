from writefileclass import WriteToTxt
from processclass import Process
from loadfileclass import LoadFile

load = LoadFile("data/5.pdf")

write = WriteToTxt(load.get_path())

process = Process(load.get_text_from_pdf())

raw_text = process.get_raw_text()
write.write_text(raw_text)

sentences = process.get_sentences(raw_text)
write.write_sentences(sentences)

keywords = process.get_keywords(raw_text)
write.write_keywords(keywords)

filter_keywords = process.get_filter_keywords(keywords)
write.write_keywords(filter_keywords, 1)

filter_sentences = process.get_filter_sentences(sentences, filter_keywords)
write.write_sentences(filter_sentences, 1)