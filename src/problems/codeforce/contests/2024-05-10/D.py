
t = int(input())

res = []

def cut(s):
    start, count = 0, 1
    chunks = []
    if len(s) == 1:
        return count
    for i, c in enumerate(s):
        if c == "1" and i < len(s)-1 and s[i+1] == "0":
            count += 1
            chunks.append(s[start:i+1])
            start = i+1
    # if start < len(s)-1:
    chunks.append(s[start:])
    
    print(chunks)

    slice = []
    found = 0
    for chunk in chunks:
        if chunk.startswith("0") and chunk.endswith("1"):
            found += 1
            if found > 1:
                count += 1
                slice.append(chunk[:chunk.find("1")])
                slice.append(chunk[chunk.find("1"):])
        else:
            slice.append(chunk)

    print(slice)

    return count

for _ in range(t):
    s = input().strip()
    res.append(cut(s))

for count in res:
    print(count)