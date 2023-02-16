import PyPDF2 as PyPDF2


class LoadFile:
    def __init__(self, path):
        self.path = path

    def get_text_from_pdf(self):
        with open(self.path, 'rb') as pdf_obj:
            pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
            page_nums = pdf_reader.numPages
            text = dict()
            for i in range(0, page_nums):
                page_obj = pdf_reader.getPage(i)
                text[i] = page_obj.extractText()
        return text

    def get_path(self):
        return self.path
