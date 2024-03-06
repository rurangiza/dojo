"""
main file
"""

def main():
    book_path = "books/frankenstein.txt"
    content = get_content(book_path)
    word_count = count_words(content)
    letters = count_letters(content)

    new = to_list_of_dict(letters, "letter", "occurences")
    new.sort(reverse=True, key=sort_on)
    
    # for l in sorted(new, reverse=True, key=lambda x: x['occurences']):
    #     print(f"The {l['letter']} character was found {l['occurences']} times")

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for l in new:
        print(f"The {l['letter']} character was found {l['occurences']} times")
    print("--- End report ---")

def get_content(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for l in text:
        l = l.lower()
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def to_list_of_dict(dict, key, value):
    res = []
    for k, v in dict.items():
        if k.isalpha():
            res.append({
                key: k,
                value: v
            })
    return res

def sort_on(dict):
        return dict['occurences']

if __name__ == "__main__":
    main()