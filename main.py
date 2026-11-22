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

text = read_file("sample.txt")
words = clean_text(text)
print(words)