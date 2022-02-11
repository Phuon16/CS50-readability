from cs50 import get_string


def main():
    # Prompt user for a string of text
    text = get_string("Text: ")

    letter = count_letter(text)
    word = count_word(text)
    sentence = count_sentence(text)

    # Grade for the text
    L = letter * 100 / word
    S = sentence * 100 / word
    # Plugged into the Coleman-Liau formula
    index = round(0.0588 * L - 0.296 * S - 15.8)
    if (index < 1):
        print("Before Grade 1")
    elif (index >= 16):
        print("Grade 16+")
    else:
        print("Grade", index)


# Count numbers of letter of any uppercase or lowercase alphabetic characters, but shouldn’t include any punctuation, digits, or other symbols
def count_letter(text):
    letter = 0
    for i in range(len(text)):
        if (ord(text[i]) > 64 and ord(text[i]) < 91) | (ord(text[i]) > 96 and ord(text[i]) < 123):
            letter += 1
    return letter


# Count numbers of words
def count_word(text):
    space = 1
    for i in range(len(text)):
        if (text[i] == " "):
            space += 1
    return space


# Count numbers of a . or a ! or a ?
def count_sentence(text):
    end = 0
    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
            end += 1
    return end


main()
