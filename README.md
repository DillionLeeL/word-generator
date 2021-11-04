#wordgenerator.py

Simple program to split words at their vowels and generate random combinations of these parts.
Good for creative writing, placeholder names, brainstorming.
****************************************************
Input: text file of sample words, newline delimited

output: prints generated words
****************************************************

Words are split into "parts", similar to syllables, and the vowel it is split at goes to the "left" part

ex - if max part length is 5, then "conceptualization" becomes ["co", "nce", "ptu", "a", "li"]
****************************************************

Uses the argparse module for command line arguments. Usage:

  -h, --help            show this help message and exit
  
  --file FILE           File to import samples from
  
  --c {1-100}           How many words to generate (1-100)
  
  --l {1-10}            Max part length of generated words (1-10)
  
  --no_order            Do not keep order of word parts, can make unintelligible results.
  
  --order               Keep order of word parts, more closely matches samples.
  
  --fix                 Attempt to break up long strings of consonants during generation. Will not work if samples contain them.
