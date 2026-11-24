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

def top_words(counts, n=10):
    pairs = list(counts.items())
    sorted_pairs = sorted(pairs, key=lambda pair:pair[1], reverse=True)
    return  sorted_pairs[:n]

def longest_word(words):
    longest = max( words,key= len)
    return longest


def count_sentences(text):
    count = 0
    for mark in ".!?":
      count += text.count(mark)
        
    return count

text = read_file("sample.txt")
words = clean_text(text)

print("Total words:", len(words))
print("Sentences:", count_sentences(text))
print("Longest word:", longest_word(words))