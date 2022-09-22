def sentenceAnalyzer(sentence2):
    letters = set()
    sentence = sentence2.lower()
    #hogy ne tegye kulon a nagy es kisbetuket

    for letter in sentence:
        letters.add(letter)

    counter = 0
    numberOfLetters = dict()

    for letter in letters:
        for i in sentence:
            if i == letter:
                counter += 1
        if letter.isalpha():
            # hogy ne vegye szamitasba a szokozt és a szamokat
            numberOfLetters[letter] = counter
        counter = 0

    print("The frequency of the letters: ", end=" ")

    print(numberOfLetters)

    print("In reversed: ", end=" ")
    print(sentence[::-1])

    words = sentence.split(' ')

    print("The words arranged in a list:", end=" ")
    print(words)

if __name__ == "__main__":
    inputSentence = input("Enter a sentence! ")
    sentenceAnalyzer(inputSentence)
