# wordcombine.py - Simple program to split words at their vowels and generate random combinations of these part
import sys
import numpy as np
from numpy.core.numerictypes import maximum_sctype

def position_of_first_vowel(word):
  for index, char in enumerate(word):
    if char in 'aeiou':
      return index
  return -1

def print_list(array):
    for x in array:
        print(*x, sep=" ")

def generate_parts(word_list, num_parts):
    # 2d list, rows for each word, columns for each part
    parts_list = [["" for x in range(num_parts)]for y in range(len(word_list))]
    #keep tally of the highest number of parts seen
    max_parts=0
    for row, word in enumerate(word_list):
        seen_parts=0
        for col in range(0,num_parts):

            vowel = position_of_first_vowel(word)

            # handle the lest letter(s) after the last vowel
            if vowel==-1:
                if word=="":
                    break
                else:
                    parts_list[row][col]=word
                    word=""
                    seen_parts+=1
                    break

            else:
                # Found vowel, store substring and shorten word
                parts_list[row][col] = word[0:vowel+1]
                #print(word[0:vowel+1])
                word = word[vowel+1:]
                seen_parts+=1
                
        max_parts=max(max_parts,seen_parts)
    
    return parts_list, min(num_parts, max_parts)

def make_words(part_list, num_parts, num_words):
    for x in range(num_words):
        word = ""
        # Get a number of parts between 2 and num_parts
        for col in range(np.random.randint(2,num_parts+1)):
            part=""
            # Select each part from a random word
            while part == "":
                part = part_list[np.random.randint(len(part_list))][col]
            word+=part
        print(word)

def main():

    if len(sys.argv) < 2:
        filename = input("Input the Filename: ")
    else:
        filename= sys.argv[1]
    #Default limit to the number of parts
    num_parts = 5

    try:
        with open(filename) as example_file:
            example_list = [line.lower().rstrip('\r\n') for line in example_file]

        p_list, num_parts = generate_parts(example_list, num_parts)

        make_words(p_list, num_parts, 10)

        example_file.close()
    except:
        print("An error occured.")

if __name__ == "__main__":
    main()
