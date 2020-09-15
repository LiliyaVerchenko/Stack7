class Stack :
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


str = Stack()
# str.push('1')
# str.push('2')
# str.push('3')
# str.push('4')
# str.push('5')
print(str.is_empty())
print(str.size())

