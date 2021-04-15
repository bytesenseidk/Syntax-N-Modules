from PyPDF2 import PdfFileWriter, PdfFileReader


class PasswordProtect_PDF(object):
    def __init__(self, file_path, password="toor"):
        self.file_path = file_path
        self.password = password
        self.writer = PdfFileWriter()
        self.pdf = PdfFileReader(file_path)
    
    
    def apply(self):
        for page in range(self.pdf.numPages):
            self.writer.addPage(self.pdf.getPage(page))
        self.writer.encrypt(self.password)

        with open(f"Secure_{self.file_path}", "wb") as file:
            self.writer.write(file)
            file.close()

        print(f"Secure_{self.file_path} Created...")


if __name__ == "__main__":
    protect = PasswordProtect_PDF("pdf_file.pdf", "python_genius")
    protect.apply()

