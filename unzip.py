from zipfile import ZipFile

def unzipper(file):
    with ZipFile(file, "r") as zip:
        zip.printdir()
        print("Extracting all the files...")
        zip.extractall()
        print("Extraction complete")

if __name__ == "__main__":
    zip_file = input(r"Path to compressed file: ")
    unzipper(zip_file)

