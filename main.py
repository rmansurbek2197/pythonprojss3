class FileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, filename, content):
        self.files[filename] = content

    def read_file(self, filename):
        return self.files.get(filename)

    def write_file(self, filename, content):
        self.files[filename] = content

    def update_file(self, filename, new_content):
        if filename in self.files:
            self.files[filename] = new_content


def main():
    fs = FileSystem()
    while True:
        print("1. Fayl yaratish")
        print("2. Fayl o'qish")
        print("3. Fayl yozish")
        print("4. Fayl yangilash")
        print("5. Chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            filename = input("Fayl nomi: ")
            content = input("Fayl matni: ")
            fs.create_file(filename, content)
        elif choice == "2":
            filename = input("Fayl nomi: ")
            print(fs.read_file(filename))
        elif choice == "3":
            filename = input("Fayl nomi: ")
            content = input("Fayl matni: ")
            fs.write_file(filename, content)
        elif choice == "4":
            filename = input("Fayl nomi: ")
            new_content = input("Fayl yangi matni: ")
            fs.update_file(filename, new_content)
        elif choice == "5":
            break
        else:
            print("Noto'g'ri tanlov")


if __name__ == "__main__":
    main()