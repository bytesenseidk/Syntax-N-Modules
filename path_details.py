class Path_Worker(object):
    def __init__(self, file_path):
        self.file = file_path
        self.file_path = file_path.split("\\")
        self.file_name = self.file_path[-1]
        self.dir_letter = self.file_path[0] + "\\"
        self.file_ext = self.file_name.split(".")[-1]
        
    def __repr__(self):
        return str("\n"
            f"Drive Letter:   {self.dir_letter}\n"
            f"Origional Path: {self.file}\n"
            f"File Name:      {self.file_name}\n"
            f"File Extension: {self.file_ext}")

if __name__ == "__main__":
    print("Drop a file here: ")
    file = input(r"  >> ").strip('"')
    print(Path_Worker(file))
    
    
