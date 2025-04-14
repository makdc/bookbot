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

def ignore_this_one___indiv_char_count(f):
    c_count = character_count(f)
    #char_list = list(get_book_text(f))
    dict_counts = {'char','count'}
    char_list = list(get_book_text(f))
    #c_count = len(char_list)
    i = 0
    for i in range(c_count):
        char_value = char_list[i]
        print(char_value)
        is_char_present = char_value in dict_counts 
        print(is_char_present)

        if char_value not in dict_counts:
            dict_counts[char_value] = 1 
        
            #is_char_present == False:
            #dict_counts[char_value] = 1
            #print(dict_counts)
        #i += 1

    print(dict_counts)
    return char_list

def sorting(dict):
    new_dict = {}
    new_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    return new_dict


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


