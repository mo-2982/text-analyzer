def read_file(path):
    with open(path,encoding="utf-8") as f:
        content = f.read()
    return content

def clean_text(text):
    text=text.lower()
    for mark in ".,!?":
        text = text.replace(mark, "")
    words = text.split()
    return words

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
           counts[word]+= 1
        else:
            counts[word] = 1
    return counts

text = read_file("sample.txt")
words = clean_text(text)
counts = count_words(words)
print(counts)