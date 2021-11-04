import sys
import numpy as np
import argparse

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

            # handle the last letter(s) after the last vowel
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

def make_words(part_list, num_parts, num_words, order):
    for x in range(num_words):
        word = ""
        # Get a number of parts between 2 and num_parts
        for col in range(np.random.randint(2,num_parts+1)):
            part=""
            # Select each part from a random word
            while part == "":
                if order:
                    part = part_list[np.random.randint(len(part_list))][col]
                else:
                    part = part_list[np.random.randint(len(part_list))][np.random.randint(num_parts)]
            word+=part
        print(word)

def main(args):

    # Get parameters from either the argparse args or from user input
    if args.file:
        filename = args.file
    else:
        filename = input("Input the Filename: ")
    if args.c:
        num_words = args.c
    else:
        num_words = -1
        while num_words not in range(1,101):
            num_words = int(input("Input number of words to generate (1-100): "))
    if args.l:
        num_parts = args.l
    else:
        num_parts = -1
        while num_parts not in range(1,11):
            num_parts = int(input("Input maximum length of words (1-10): "))
    if not args.no_order:
        keep_order=args.no_order
    elif args.order:
        keep_order=args.order
    else:
        user_keep = ""
        while user_keep not in ['y', 'n']:
            user_keep = input("Keep the order of word parts? y/n (select 'y' to more closely match samples) ").strip().lower()
        if user_keep == 'y':
            keep_order= True
        else:
            keep_order= False
    
    try:
        with open(filename) as example_file:
            example_list = [line.lower().rstrip('\r\n') for line in example_file]

        p_list, num_parts = generate_parts(example_list, num_parts)

        make_words(p_list, num_parts, num_words, keep_order)

        example_file.close()
    except:
        print("An error occured.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help="File to import samples from")
    parser.add_argument('--c', type=int, choices=range(1,101), help="How many words to generate (1-100)")
    parser.add_argument('--l', type=int, choices=range(1,11), help=('Enter the max part length of generated words (1-10)'))
    parser.add_argument('--no_order', action='store_false', help="Do not keep order of word parts, can make unintelligible results")
    parser.add_argument('--order', action='store_true', help="Keep order of word parts, more closely matches samples")

    args = parser.parse_args()
    main(args)
