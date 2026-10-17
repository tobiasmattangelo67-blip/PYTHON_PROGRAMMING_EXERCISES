
def writeToFile(fileName, text):
    with open(f"D:/{fileName}", "w") as file:
        file.write(text)

def appendToFile(fileName, text):
    with open(f"D:/{fileName}", "a") as file:
        file.write(text)

def readFromFile(fileName):
    with open(f"D:/{fileName}", "r") as file:
        return file.read()

writeToFile('greet.txt', 'Hello!\n') 
appendToFile('greet.txt', 'Goodbye!\n') 
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
print(readFromFile('greet.txt'))