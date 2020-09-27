

import os
import PyPDF2
from pdf2docx import parse

class Docx_Pdf(object):
    def __init__(self, file_path):
        self.file_path = file_path.split("\\")
        self.file_name = self.file_path[-1]
        self.file_ext = self.file_name.split(".")[-1]
        self.file_path = os.path.join(*self.file_path)
        self.main()
    
    def __repr__(self):
        return f"{self.file_name} Converted..."

    def main(self):
        if self.file_ext == "pdf":
            pdf = PyPDF2.PdfFileReader(open(self.file_path, "rb"))
            with open(self.file_path.replace(".pdf", ".docx"), "a") as file:
                for page in pdf.pages:
                    file.write(page.extractText())
        else:
            new_filename = self.file_path.replace(".pdf", ".docx")
            return parse(self.file_path, new_filename, start=0, end=1)

if __name__ == "__main__":
    file = input(r"Drag and Drop file here:\n >> ")
    pdf_tool = Docx_Pdf(file)
    print(pdf_tool)


