class Runner:
    def __init__(self, who):
        print(f'Getting ready to go for a run with {who}')
        self.who = who


    def __enter__(self):
        print(f"Putting {self.who}'s shoes on.")
        return self.who


    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Taking {self.who}'s shoes off")


with Runner(who='Nike') as shoe:
    print(f'running with {shoe}')

