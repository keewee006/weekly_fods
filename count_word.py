from collections import Counter

def word_count(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        counts = Counter(words)
        for word, count in counts.items():
            print(f"{word}: {count}")

# test
word_count("example.txt")
