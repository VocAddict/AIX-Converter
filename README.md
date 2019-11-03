# AIX-Converter
A converter that generates IPA and X-SAMPA output from English text

* A - Alphabet (to)
* I - IPA (and)
* X - X-SAMPA

This program is used to convert English text into IPA and X-SAMPA as the output. 
It uses the English-to-IPA library from mphilli: https://github.com/mphilli/English-to-IPA

# Prerequisites

1. Python 3 must be used with SQL addons enabled for usage of the IPA converter (most binaries should come with this enabled by default)
2. This library must also be installed for this program to work: https://github.com/mphilli/English-to-IPA
    Installation of this package can be done with the command: 
        python3 setup.py install

# Usage

1. Place the words you want to convert into the "source.txt" file, they must be line by line
2. Run the command:
    python3 converter.py
    
Three files would be created:
* dictionary.csv (dictionary with source, ipa, and xs files separated by a delimiter)
* ipa.txt (IPA conversion)
* xs.txt (X-SAMPA conversion)
