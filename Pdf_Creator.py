from fpdf import FPDF

def from_text(file_path):
    file_name = str(file_path.split("\\")[-1])
    parser = FPDF()
    # Create blank pdf page
    parser.add_page()
    # Font settings
    parser.set_font("Arial", size=15)
    # Opens the text file
    with open(file_path, "r") as file:
        # For every line in the text-file
        for row, line in enumerate(file):
            # Write that line to the PDF Page
            line = line.encode('latin-1', 'replace').decode('latin-1')
            parser.cell(200, 10, txt=line, ln=row, align="c")
    return parser.output(f"{file_name}.pdf")

if __name__ == "__main__":
    filepath = input(f"Enter path to your text file: ")
    from_text(filepath)

