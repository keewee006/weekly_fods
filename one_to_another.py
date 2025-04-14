def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())
    print(f"Copied content from {source} to {destination}")

# test
copy_file("source.txt", "destination.txt")
