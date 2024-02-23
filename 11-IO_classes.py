# Define the FileManager class here


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_content(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def read_content(self):
        with open(self.filename, "r") as f:
            return f.read()


# Demonstrate using FileManager to write and read from a file

fileManager = FileManager("note_test.txt")
fileManager.write_content("Hola soy david vasquez")
content = fileManager.read_content()
print(content)
