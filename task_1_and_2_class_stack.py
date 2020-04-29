class Stack:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements) - 1]

    def size(self):
        return len(self.elements)

    def __getitem__(self, idx):
        return self.elements[idx]

    def __str__(self):
        return print(self.elements)


def is_balanced(brackets, pattern="()[]{}"):
    try:
        open_brackets, closed_brackets = pattern[::2], pattern[1::2]
        stack = Stack()
        for element in brackets:
            if element in open_brackets:
                stack.push(open_brackets.index(element))
            elif element in closed_brackets:
                if stack and stack[-1] == closed_brackets.index(element):
                    stack.pop()
                else:
                    return print("Неcбалансированно")
        return print("Сбалансированно")
    except IndexError:
        print("Неcбалансированно")


print("Task 1 and 2:")
is_balanced(brackets="(((([{}]))))")
is_balanced(brackets="[([])((([[[]]])))]{()}")
is_balanced(brackets="{{[()]}}")
is_balanced(brackets="}{}")
is_balanced(brackets="{{[(])]}}")
is_balanced(brackets="[[{())}]")
