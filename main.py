path_to_file = "books/frankenstein.txt"

def main():
    wordctr = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        for i in words:
            wordctr += 1
            
        print(wordctr)
main()