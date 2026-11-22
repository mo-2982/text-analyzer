def read_file(path):
    with open(path,encoding="utf-8") as f:
        content = f.read()
    return content

text = read_file("sample.txt")
print(text)