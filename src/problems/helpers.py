""""
Python for Competitive Programming
"""

mode = 2

i = lambda: list(map(int, input(": ").split()))
s = lambda: list(input(":").split())

# 0: User input
if mode == 0:
    size = int(input("Size: "))
    for i in range(size):
        a, b = i()
        print("= ", a * b)

# 1: String manipulation
if mode == 1:
    # prefix and suffix
    text = "Crewmate"
    print(text.startswith("Crew"))
    print(text.endswith("mate"))

# 2: ASCII
if mode == 2:
    letter = input("Enter letter: ").strip()[:1]
    in_ascii = ord(letter)
    in_char = chr(in_ascii)
    print(in_ascii, in_char)

# 3: Ceasar Cypher
    