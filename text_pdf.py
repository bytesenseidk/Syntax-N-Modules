

import PyPDF2
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

class Text_Pdf(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = self.file_path.split("\\")[-1]
        self.file_ext = self.file_name.split(".")[-1]
        self.main()
    
    def __repr__(self):
        return f"{self.file_name} Converted..."

    def main(self):
        if self.file_ext == "pdf":
            pdf = PyPDF2.PdfFileReader(open(self.file_path, "rb"))
            with open(f"{self.file_name.strip('.pdf')}.txt", "a") as file:
                for page in pdf.pages:
                    file.write(page.extractText())
        else:
            parser = FPDF()
            parser.add_page()
            parser.set_font("Arial", size=15)
            with open(self.file_path, "r") as file:
                for row, line in enumerate(file):
                    line = line.encode('latin-1', 'replace').decode('latin-1')
                    parser.cell(200, 10, txt=line, ln=row, align="c")
            return parser.output(f"{self.file_name.strip('.txt')}.pdf")

if __name__ == "__main__":
    file = input("Drag and Drop file here:\n >> ")
    pdf_tool = Text_Pdf(file)
    print(pdf_tool)


