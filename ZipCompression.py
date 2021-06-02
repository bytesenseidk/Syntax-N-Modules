import os
from zipfile import ZipFile

def zip_me(path):
    """ Target folder path & name """
    folder_name = path.split("\\")[-1]
    rel_path = path.strip(folder_name)

    """ Save zipfile to the target folder path """
    os.chdir(rel_path)

    zip_file = ZipFile(f"{folder_name}.zip", "w")

    for root, dirs, files in os.walk(folder_name, topdown=False):
        """ Files in sub-folders """
        for name in files:
            file = os.path.join(root, name)
            zip_file.write(file)

        """ Sub-folders in target folder """
        for name in dirs:
            folders = os.path.join(root, name)
            zip_file.write(folders)
    zip_file.close()
        
if __name__ == "__main__":
    path = input(r"Path to target folder: ")
    zip_me(path)

