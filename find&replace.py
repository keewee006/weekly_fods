def find_replace(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Replaced '{old_word}' with '{new_word}' in {file_path}")

# test
find_replace("sample.txt", "oldword", "newword")
