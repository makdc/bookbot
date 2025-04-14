from stats import word_count

def main():

    num_words = str(word_count('./books/frankenstein.txt'))
    output = num_words + " words found in the document"
    print(output)

main()