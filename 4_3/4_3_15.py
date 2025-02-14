class Wordplay:
    def __init__(self, words=[]):
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [item for item in self.words if len(item) == n]

    def only(self, *args):
        return [item for item in self.words if set(item).issubset(args)]

    def avoid(self, *args):
        return [item for item in self.words if set(item).intersection(args) == set()]



wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))
