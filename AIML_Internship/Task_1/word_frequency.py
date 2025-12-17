# Word frequency in a paragraph - Jayanth

def word_frequency(paragraph):
    words = paragraph.lower().split()
    freq = {}

    for word in words:
        word = word.strip(".,!?")
        freq[word] = freq.get(word, 0) + 1

    return freq

text = "AI is powerful and AI is the future"
print("Word Frequency:", word_frequency(text))

