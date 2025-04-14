def word_intersection():
    w1 = input("Enter first word: ").lower()
    w2 = input("Enter second word: ").lower()
    common = set(w1) & set(w2)
    print("Common letters:", common)

word_intersection()
