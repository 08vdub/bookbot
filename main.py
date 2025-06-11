def main():
    get_book_text()

def get_book_text():
    #this opens up the book and saves it as "f"
    with open("/home/padro/workspace/github.com/08vdub/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)



main()