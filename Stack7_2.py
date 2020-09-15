class Stack :
    def __init__(self, string):
        self.string = string
        self.items = []
        self.open_list = ["[", "{", "("]
        self.close_list = ["]", "}", ")"]

    def is_empty(self):
        return (self.items == [])

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def check_balance(self):
        for element in self.string:
            if element in self.open_list:
                self.push(element)
            elif element in self.close_list:
                index = self.close_list.index(element)
                if (len(self.items) > 0) and (self.open_list[index] == self.peek()):
                    self.pop()
                else:
                    return "Неcбалансированно"
        if self.is_empty() is True:
            return "Сбалансированно"

string1 = "(((([{}]))))"
string2 = "[([])((([[[]]])))]{()}"
string3 = "{{[()]}}"
string4 = "}{}"
string5 = "{{[(])]}}"
string6 = "[[{())}]"
string_test1 = Stack(string1)
string_test2 = Stack(string2)
string_test3 = Stack(string3)
string_test4 = Stack(string4)
string_test5 = Stack(string5)
string_test6 = Stack(string6)
print(string_test1.check_balance())
print(string_test2.check_balance())
print(string_test3.check_balance())
print(string_test4.check_balance())
print(string_test5.check_balance())
print(string_test6.check_balance())

