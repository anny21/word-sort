from os.path import exists
"""The find function takes in two parameters:
 The word path and the paragraph path: and returns the words found in DICT Type
  and the number of occurrence from the most occurred to least found"""


def find(words_path, paragraph_path):
    """Opens the files  """

    with open(words_path, "r", encoding='utf8') as word_lists:
        word_content = word_lists.read().lower().split(", ")
    with open(paragraph_path, "r", encoding='utf8') as paragraphs:
        paragraphs_content = paragraphs.read().lower().replace(",", "")\
            .replace("\n", " ").split(" ")
    found = {}
    print(paragraphs_content)

    for word in word_content:
        if word in paragraphs_content:
            found[word] = paragraphs_content.count(word)

    print(found.items())
    result = dict(sorted(found.items(), key=lambda item: item[1], reverse=True))

    print(result)

    return result


input_word_path = input("Please type in your word path\n")
input_paragraph_path = input("Please type in your paragraph path\n")


def check_file(words_path, paragraph_path):

    if exists(words_path) and exists(paragraph_path):
        find(words_path, paragraph_path)
    else:
        print("please enter a valid file path")
        return "Invalid file"


check_file(input_word_path, input_paragraph_path)