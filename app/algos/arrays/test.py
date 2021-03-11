from ArrayStack import ArrayStack


with open("info.md", "r") as file:
    inverse_file = ArrayStack()
    for l in file.readlines():
        inverse_file.push(l.strip("\n"))

while not inverse_file.is_empty():
    print(inverse_file.pop())

