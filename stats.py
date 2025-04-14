def word_count(f):
    word_list = get_book_text(f).split()
    w_count = len(word_list)
    return w_count

def get_book_text(f):
    f = open(f)
    file_contents = f.read()
    return file_contents