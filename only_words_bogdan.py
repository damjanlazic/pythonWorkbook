"""
Removing any punctuation signs from the given sentance.
"""

PUNCTUATION_MARKS = [',', '.', '!', "'"]
THE_SENTANCE = "Who is this man, so wise in his words and deeds that's standing here before me. \
                Dark times have come, for I wasn't prepared for this, no..."

def mark_remover(word):
    for i in PUNCTUATION_MARKS:
        word = word.strip(i)
    return word

def word_iterator(sentance):
    split_sentance = sentance.split()
    sorted_sentance = []
    for word in split_sentance:
        new_word = mark_remover(word)
        sorted_sentance.append(new_word)
    return sorted_sentance

print(word_iterator(sentance=THE_SENTANCE))