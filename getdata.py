import PyPDF2 as PyPDF2
import pdfplumber
from output import output_text

def getTextFromPDF(file_name):
    pdfFileObj = open('data/'+file_name, 'rb')     # 'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages
    text = ""
    text_folie = {}

    for i in range(0, numPages):
        pageObj = pdfReader.getPage(i)
        text = text + " " + pageObj.extractText()
        text_folie[i] = pageObj.extractText()
    return text, pdfFileObj, text_folie

def getTextFromPDF_2(file_name):
    pdfFileObj = open('data/'+file_name, 'rb')     # 'rb' for read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages
    text_folie = {}

    for i in range(0, numPages):
        pageObj = pdfReader.getPage(i)
        text_folie[i] = pageObj.extractText()
    return text_folie

def getTextFromFile(file_name):
    with open('data/'+file_name+'', 'r') as file:
        data = file.read()
    return data


def extract_content(pdf_path):
    # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
    with pdfplumber.open(pdf_path) as pdf_file:
        content = ''
        # len(pdf.pages)为PDF文档页数，一页页解析
        for i in range(len(pdf_file.pages)):
            print("当前第 %s 页" % i)
            # pdf.pages[i] 是读取PDF文档第i+1页
            page_text = pdf_file.pages[i]
            # page.extract_text()函数即读取文本内容
            page_content = page_text.extract_text()
            if page_content:
                content = content + page_content + "\n"
    return content

if __name__ == "__main__":
    content = extract_content("data/x.pdf")
    output_text(content, "text.pdf", 10)
