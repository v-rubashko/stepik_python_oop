class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words += text.split()

    def get_shortest_words(self):
        return list(filter(lambda w: len(w) == min(list(map(len, self.words))), self.words))

    def get_longest_words(self):
        return list(filter(lambda w: len(w) == max(list(map(len, self.words))), self.words))

    def result(self):
        return self.words

texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())