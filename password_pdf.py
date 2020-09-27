from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    # Read in the pdf file
    for page in range(pdf.numPages):
        # For every page in the pdf file, add that to the new file
        parser.addPage(pdf.getPage(page))
    # Encrypts the pdf, which enable the password Protect feature  
    parser.encrypt(password)
    # Opens the encrypted file, 
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} Created...")

if __name__ == "__main__":
    file = "kivy.pdf"
    password = "python_genius"
    secure_pdf(file, password)

