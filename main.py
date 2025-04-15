#main.py

from stats import word_count
from stats import indiv_char_count
#from stats import character_count
#from stats import get_book_text

def main():

    print("============ BOOKBOT ============")
    num_words = str(word_count('./books/frankenstein.txt'))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")

 #  num_char = str(character_count('./books/frankenstein.txt'))
 #  print(str(num_char))

#   indiv_num_char = str(indiv_char_count('./books/frankenstein.txt'))
#   print(indiv_num_char)

    indiv_num_char = indiv_char_count('./books/frankenstein.txt')
#   print(indiv_num_char)
    print("--------- Character Count -------")
    sorted_list = sorted(indiv_num_char.items(), key=lambda item: item[1], reverse=True)
    #print(sorted_chars)
    #print(dict(sorted_chars))
    sorted_dict = dict(sorted_list)
    for k, v in sorted_dict.items():
        print( '%s: %i' % (k, v) )
    print("============= END ===============")


main()