from stats import word_count
from stats import indiv_char_count
from stats import character_count
from stats import get_book_text
from stats import sorting

def main():

    #num_words = str(word_count('./books/frankenstein.txt'))
    #output = num_words + " words found in the document"
    #print(output)
    #content = get_book_text('./books/frankenstein.txt')


#    num_words = str(word_count('./books/frankenstein.txt'))
#    print(str(num_words))

 #   num_char = str(character_count('./books/frankenstein.txt'))
 #   print(str(num_char))

    indiv_num_char = str(indiv_char_count('./books/frankenstein.txt'))
    print(sorting(indiv_num_char))


main()