def get_book_text(path_to_book):
    with open(path_to_book) as f:
        reading_file = f.read()
        return reading_file
    
def count_each_character(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def sort_char_count(char_count_dict):
    sorted_char_count = []
    for char in char_count_dict:
            sorted_char_count.append({"char": char, "num": char_count_dict[char]})
    sorted_char_count.sort(key=sort_on, reverse=True)
    
    return sorted_char_count

   

