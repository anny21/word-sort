"""Importing list of words and paragraphs and
checking if words exists in paragraphs  """


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

    print(found)


find("words.txt", "paragraph.txt")
