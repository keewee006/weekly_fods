def count_file_stats(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

# test
count_file_stats("test.txt")
