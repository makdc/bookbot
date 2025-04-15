#main.py
import sys
from stats import word_count
from stats import indiv_char_count
#from stats import character_count
#from stats import get_book_text

def main():
    
    curr_file = sys.argv[1] #.lower()

    num_words = str(word_count(curr_file))

 #  num_char = str(character_count('./books/frankenstein.txt'))
 #  print(str(num_char))

#   indiv_num_char = str(indiv_char_count('./books/frankenstein.txt'))
#   print(indiv_num_char)
#   './books/frankenstein.txt'
    #curr_file = sys.argv[1]
    indiv_num_char = indiv_char_count(curr_file)
#   print(indiv_num_char)

    sorted_list = sorted(indiv_num_char.items(), key=lambda item: item[1], reverse=True)
    #print(sorted_chars)
    #print(dict(sorted_chars))
    sorted_dict = dict(sorted_list)

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    for k, v in sorted_dict.items():
        print( '%s: %i' % (k, v) )
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


try:
    main()

except FileNotFoundError:
    print("File not found. Please check filepath and try again - Thank you!")

except Exception as e:
    print(f"The following erro occurred: {e}")    