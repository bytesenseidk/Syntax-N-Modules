
class List_Comprehenssion(object):
    def __repr__(self):
        string = str(f"Bad Way:  {self.bad_way()}\n"
                     f"Easy Way: {self.easy_way()}\n")
        return string


    def bad_way(self):
        evens = []
        for i in range(10):
            if i % 2 == 0:
                evens.append(i)
        return evens


    def easy_way(self):
        evens = [i for i in range(10) if i % 2 == 0]
        return evens
    

if __name__ == "__main__":
    print(List_Comprehenssion())
