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

def write_report(path, total_words, sentences, longest, top):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Total words: {total_words}\n")
        f.write(f"sentences: {sentences}\n")
        f.write(f"longest: {longest}\n")
        f.write("Top words:\n")
        for word, count in top:
            f.write(f"{word}: {count}\n")
            
def main():
    text = read_file("sample.txt")
    words = clean_text(text)
    counts = count_words(words)

    total = len(words)
    sentences = count_sentences(text)
    longest = longest_word(words)
    top = top_words(counts, 10)

    write_report("report.txt", total, sentences, longest, top)
    print("Report saved to report.txt")


if __name__ == "__main__":
    main()