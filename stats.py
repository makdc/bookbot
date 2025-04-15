def word_count(f):
    word_list = get_book_text(f).split()
    w_count = len(word_list)
    return w_count

def character_count(f):
    char_list = list(get_book_text(f))
    c_count = len(char_list)
    return c_count

def indiv_char_count(f):
    #c_count = character_count(f)
    dict_count = {}
    char_list = list(get_book_text(f).lower())
    
    for char in char_list:
        dict_count[char] = dict_count.get(char,0)+1
    #print(dict_count)
    return dict_count


def sorted_indiv_char_count(f):
    #c_count = character_count(f)
    dict_count = {}
    char_list = list(get_book_text(f).lower())
    
    for char in char_list:
        dict_count[char] = dict_count.get(char,0)+1
    #print(dict_count)
    new_dict = dict(sorted(dict_count.items(), key=lambda char: char[1]))
    return new_dict


#def sort_on(dict):
#    return dict["count"]   

#def sorting(dict):  
#    #dict.sort(reverse=True, key=sort_on)
#
#    dict.sort(reverse=True, key=sort_on)
#    print(dict)


def char_present(char):
    is_char_present = char in characters
    return is_char_present 

def get_book_text(f):
    with open(f) as f:
        # do something with f (the file) here
        file_contents = f.read()
        return file_contents

#def split_by_char(text, chunksize):
#    return [text[i:(i+chunksize)] for i in range(len(text)-chunksize+1)]


