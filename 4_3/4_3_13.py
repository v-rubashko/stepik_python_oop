class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, n):
        return [t[0] for t in self.things if t[1] == n]

    def get_low_priority(self):
        return [t[0] for t in self.things if t[1] == min(map(lambda x: x[1], self.things))]

    def get_high_priority(self):
        return [t[0] for t in self.things if t[1] == max(map(lambda x: x[1], self.things))]

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))