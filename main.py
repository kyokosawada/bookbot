def sort_on(dict):
    return dict["num"]


def main():
    path_to_file = "books/frankenstein.txt"
    wordctr = 0
    character = {}
    merge_list = []
    c_list = []
    n_list = []

    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            wordctr += 1
            for c in range(len(word)):
                w = word[c].lower()
                if w not in character:
                    if w.isalpha():
                        character[w] = 1
                else:
                    character[w] += 1

    c_list = list(character)
    n_list = list(character.values())

    for c in range(len(character)):
        merge_list.append({"char": c_list[c], "num": n_list[c]})

    merge_list.sort(reverse=True, key=sort_on)

    # Report start --------------------
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{wordctr} words found in the document\b")
    print("")
    for found in range(len(merge_list)):
        char = merge_list[found]["char"]
        num = merge_list[found]["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")


main()
