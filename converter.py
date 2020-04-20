#!/usr/bin/python3

import re
import sqlite3
import subprocess
#import "..\externals\English-to-IPA\setup"
import eng_to_ipa as ipa
from itertools import zip_longest

print('Welcome to the Alphabet to X-SAMPA Converter for the English Language, henceforth referred to as AIX.')
print('AIX is used to convert any word in the English language and converts it IPA and X-SAMPA.')
print()
yn_start = input('Would you like to continue with this program or would you like to exit? (y or n): ').lower()

if yn_start == 'y':
    
    print()
    print('AIX is used to convert any word in the English language and converts it IPA and X-SAMPA. The steps are detailed below:')
    print('1) Read the corpus given in source.txt in the directory of this program.')
    print('2) Converts the corpus into IPA, which is stored in ipa.txt.')
    print('3) Converts IPA to X-SAMPA, which is stored in xs.txt.')
    print('4) Joins all three files one file, separated by a delimited ";", dictionary.csv.')
    input('Press "ENTER" to continue...')
    print()

    word_count = 0

    #open file containing words for conversion
    print('Step 1')
    print('Reading the word file...')
    print()
    with open('source.txt','r') as word_source:
        for line in word_source:
            if line.strip():
                word_count += 1
            else:
                print()
    
    print('Number of words to be converted: %d' % word_count)
    input('Press "ENTER" to continue...')
    print()
    
    #open  file to contain the middle stage (IPA conversion)

    conver_ipa = 0
    
    print('Step 2')
    print('Converting words to IPA...')
    print()
    
    with open('source.txt','r') as word_source:
        with open('ipa.txt','w') as ipa_output:
            for line in word_source:
                print(ipa.convert(line, True, True, "both"), file=ipa_output)
                conver_ipa += 1
                print('Converting to IPA: %d/%d' % (conver_ipa, word_count))
            
    conver_ipa = 0
    print()
    
    with open('ipa.txt','r') as ipa_output:
        for line in ipa_output:
            if line.strip():
                conver_ipa += 1
            else:
                print()
            
    print('Number of words converted to IPA: %d' % conver_ipa)
    input('Press "ENTER" to continue...')
    print()
    
    #open file to contain the final stage (X-SAMPA conversion)
    conver_xs = 0
    
    print('Step 3')
    print('Converting words to X-SAMPA...')
    
    #exec(open('xs_convert.py').read())
        #from xs_convert.py
        
    #ipa_list = ['p', 'b', 't', 'd', 'ʧ', 'ʤ', 'k', 'g', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'h', 'm', 'n', 'ŋ', 'l', 'r', 'w', 'j', 'æ', 'ɑ', 'ɒ', 'ɔ', 'ə', 'ɪ', 'i', 'e', 'ɛ', 'ər', 'ɜr', 'ʌ', 'ʊ', 'u', 'eɪ', 'aɪ', 'ɔɪ', 'oʊ', 'aʊ', 'ɑr', 'ɪr', 'ɛr', 'ɔr', 'ʊr']
    #xsampa_list = ['p', 'b', 't', 'd', 'tS', 'dZ', 'k', 'g', 'f', 'v', 'T', 'D', 's', 'z', 'S', 'Z', 'h', 'm', 'n', 'N', 'l', 'r', 'w', 'j', '{', 'A', 'Q', 'O', '@', 'I', 'i', 'e', 'E', '@`', '3`', 'V', 'U', 'u', 'eI', 'aI', 'OI', 'oU', 'aU', 'A`', 'I`', 'E`', 'O`', 'U`']

    with open('ipa.txt', 'r') as ipa_xs :
        filedata = ipa_xs.read()

    #stress
    filedata = filedata.replace('ˈ', '')
    filedata = filedata.replace('"', '')
    filedata = filedata.replace('ˌ', '')
    filedata = filedata.replace("'", '')
    filedata = filedata.replace('[', '')
    filedata = filedata.replace(']', '')

    #consonants
    filedata = filedata.replace('p', 'p')
    filedata = filedata.replace('b', 'b')
    filedata = filedata.replace('t', 't')
    filedata = filedata.replace('d', 'd')
    filedata = filedata.replace('ʧ', 'tS')
    filedata = filedata.replace('ʤ', 'dZ')
    filedata = filedata.replace('k', 'k')
    filedata = filedata.replace('g', 'g')
    filedata = filedata.replace('f', 'f')
    filedata = filedata.replace('v', 'v')
    filedata = filedata.replace('θ', 'T')
    filedata = filedata.replace('ð', 'D')
    filedata = filedata.replace('s', 'z')
    filedata = filedata.replace('z', 'z')
    filedata = filedata.replace('ʃ', 'S')
    filedata = filedata.replace('ʒ', 'Z')
    filedata = filedata.replace('h', 'h')
    filedata = filedata.replace('m', 'm')
    filedata = filedata.replace('n', 'n')
    filedata = filedata.replace('ŋ', 'N')
    filedata = filedata.replace('l', 'l')
    filedata = filedata.replace('r', 'r')
    filedata = filedata.replace('w', 'w')
    filedata = filedata.replace('j', 'j')

    #diphthongs
    #filedata = filedata.replace('eɪ', 'eI')
    #filedata = filedata.replace('aɪ', 'aI')
    #filedata = filedata.replace('ɔɪ', 'OI')
    #filedata = filedata.replace('oʊ', 'oU')
    #filedata = filedata.replace('aʊ', 'aU')

    #rhotics
    #filedata = filedata.replace('ɑr', 'A`')
    #filedata = filedata.replace('ɪr', 'I`')
    #filedata = filedata.replace('ɛr', 'E`')
    #filedata = filedata.replace('ɔr', 'O`')
    #filedata = filedata.replace('ʊr', 'U`')
    #filedata = filedata.replace('ər', '@`')
    #filedata = filedata.replace('ɜr', '3`')

    #vowels
    filedata = filedata.replace('æ', '{')
    filedata = filedata.replace('ɒ', 'Q')
    filedata = filedata.replace('ʌ', 'V')
    filedata = filedata.replace('u', 'u')
    filedata = filedata.replace('ɑ', 'A')
    filedata = filedata.replace('ɪ', 'I')
    filedata = filedata.replace('ɛ', 'E')
    filedata = filedata.replace('ɔ', 'O')
    filedata = filedata.replace('ʊ', 'U')
    filedata = filedata.replace('ə', '@')
    filedata = filedata.replace('e', 'e')
    filedata = filedata.replace('a', 'a')
    filedata = filedata.replace('ɜ', '3')

    with open('xs.txt', 'w') as xs_output:
        xs_output.write(filedata)
    
    with open('xs.txt','r') as xs_output:
        for line in xs_output:
            if line.strip():
                conver_xs += 1
            else:
                print()
   
    print('Number of words converted to X-SAMPA: %d' % conver_xs)
    input('Press "ENTER" to continue...')
    print()

    #merging of files into final.dict
    merge_number = 0
    
    print('Step 4')
    print('Merging files...')
    print()
    
    with open('dictionary.csv','w') as diction, open('source.txt','r') as word_source, open('ipa.txt','r') as ipa_output, open('xs.txt','r') as xs_output:
        for word_source, ipa_output, xs_output in zip_longest(word_source, ipa_output, xs_output, fillvalue=''):
            diction.write('{};{};{}\n'.format(word_source.strip(), ipa_output.strip(), xs_output.strip()))
        
    with open('dictionary.csv','r') as diction:
        for line in diction:
            if line.strip():
                merge_number += 1
            else:
                print()
                
    print('Number of lines in dictionary: %d' % merge_number)
    input('Press "ENTER" to continue...')
    print()    
    
    #final comments
    print('%d words have been converted.' % merge_number)
    print('The final compilation of data can be found in "dictionary.csv". This file is structured in a way where the word, with its supplementary conversions are available side by side, line by line.')
    print()
    input('Press "ENTER" to exit the program.')
    
elif yn_start == "n":    
        print()
        print('Thank you for using AIX!')

else:
        print()
        print('Please try again later...')
        input('Press "Enter" to continue')
        print()
	
exit()
