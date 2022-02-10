from fnmatch import translate
from uzwords import words
from difflib import get_close_matches
from transliterate import to_cyrillic, to_latin 



def checkword(word, words=words):
    word = word.lower()
    if word.isascii():
        word = to_cyrillic(word)
        match_list = set(get_close_matches(word, words))
        availible = False
        word = to_latin(word)
        matches = []
        for m in match_list:
            m = to_latin(m)
            matches.append(m)

        if word in matches:
            availible = True
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'x')
            matches = matches.update(get_close_matches(word, words))
        elif 'x' in word:
            word = word.replace('x', 'ҳ')
            matches = matches.update(get_close_matches(word, words))


    else:
        matches = set(get_close_matches(word, words))
        availible = False

        if word in matches:
            availible = True
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'x')
            matches.update(get_close_matches(word, words))
        elif 'x' in word:
            word = word.replace('x', 'ҳ')
            matches.update(get_close_matches(word, words))



    return {'availible': availible, 'matches':matches}

