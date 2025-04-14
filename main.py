def main():

    num_words = str(word_count('./books/frankenstein.txt'))
    output = num_words + " words found in the document"
    print(output)


def get_book_text(f):
    f = open(f)
    file_contents = f.read()
    return file_contents


def word_count(f):
    word_list = get_book_text(f).split()
    w_count = len(word_list)
    return w_count
    

main()