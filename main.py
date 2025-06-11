def main():
    # uses the get_book_text function
    book_path = "/home/padro/workspace/github.com/08vdub/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words =  word_count(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    #this opens up the book and saves it as "f"
    with open(path) as f:
        return f.read()
        

 
def word_count(text):
    words =  text.split()
    return len(words)

main() 