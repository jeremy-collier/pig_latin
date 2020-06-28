#English to Pig Latin

print('Enter the English message you want translated to Pig Latin: ')
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] #This is a list of words in Pig pigLatin

for word in message.split():
    # Separate the non-letters at the start of this word
    prefixNonLetters = ''
    while len(word)>0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Separate non-letters at the end of a word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    #Separate the consonants at the start of word
    prefixConsonants = ''
    while len(word)>0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    #Add the Pig Latin ending to the word
    if prefixConsonants !='':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join it all together to a single string
print(' '.join(pigLatin))
