import os

def configure():
    flags = {
        'Default': '',
        'Read entire query': '-a', 
        'Retrieve n number of results': '-n', 
        'Display only a link to where the answer is from': '-l',
        'Display the answer in color': '-c',
        'Specify search engine': '-e'
    }
    for index, flag in enumerate(flags.keys()):
        print(f"[{index}] {flag}")
    
    answer = int(input("\nSelect a flag: "))
    if answer > len(flags.keys()) or answer < 0:
        print("Invalid input")
        return configure()
    else:
        flag = flags[list(flags)[answer]]
        return flag

def question_constructor():
    # flag = configure()
    while True:
        print("\nType your question or type 'exit' to exit")
        question = input("\nEnter your question: ")
        if question == "exit":
            break
        print('\n')
        question = f"howdoi {question}"
        os.system(question)
        
        
if __name__ == "__main__":
    os.system("cls")
    while True:
        print("\nType your question or type 'exit' to exit")
        question = input("\nEnter your question: ")
        if question != "exit":
            print('\n')
            question = f"howdoi {question}"
            os.system(question)
            continue
        break

