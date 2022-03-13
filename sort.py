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
    print(dict(sorted(found.items(), key=lambda item: item[1], reverse=True)))


find("words.txt", "paragraph.txt")
