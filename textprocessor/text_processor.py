import re
import random


def scramble_word(word: str) -> str:
    """
    Scramble the middle characters of a word while keeping first and last characters in place.

    Words with less than 4 characters are returned unchanged.

    Args:
        word: The word to scramble.

    Returns:
        The scrambled word with first and last characters preserved.

    Examples:
        >>> scramble_word("hello")
        "hlelo"  # middle characters shuffled
        >>> scramble_word("hi")
        "hi"  # too short, unchanged
    """

    if len(word) < 4:
        return word

    first = word[0]
    middle = word[1:-1]
    last = word[-1]

    middle_chars = list(middle)
    random.shuffle(middle_chars)
    scrambled_middle = "".join(middle_chars)

    return first + scrambled_middle + last


def process_text(text: str) -> str:
    """
    Process text by scrambling the middle characters of each word.

    The function preserves the first and last character of each word (4+ characters),
    while randomly shuffling the middle characters. Whitespace, punctuation, and
    formatting are preserved.

    Args:
        text: The text to process.

    Returns:
        The processed text with scrambled words.

    Raises:
        TypeError: If text is not a string.
    """

    regex_token = r'(\w+)|(\W+)'
    result = []

    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    for token in re.findall(regex_token, text):
        if token[0]:
            result.append(scramble_word(token[0]))
        else:
            result.append(token[1])

    return "".join(result)


if __name__ == '__main__':
    text = input("Enter text to process: ")
    print(process_text(text))
