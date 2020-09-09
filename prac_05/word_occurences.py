"""
CP5632 Practical 5

Program to count word occurences in a string provided by the user
"""


def main():
    word_counts = {}

    text_input = input("Text: ").lower()
    word_list = text_input.split()
    for word in word_list:
        if word not in word_counts:
            word_count = word_list.count(word)
            word_counts[word] = word_count
    word_list = list(word_counts.keys())
    word_list.sort()

    for word in word_list:
        print("{:{}} : {}".format(word, len(max(word_list, key=len)), word_counts[word]))


main()
