data = open("./files_quarantine.txt", "r").readlines()

real_files = 1
for line in data:
    string, checksum = line.split("-")
    stack = []
    for char in string:
        if char not in stack:
            if checksum.count(char) == 1:
                stack.append(char)
        else:
            stack.remove(char)
    if "".join(stack) == checksum.strip():
        print(f"REAL FILE: {real_files} - {checksum.strip()} - {''.join(stack)}")
        real_files += 1
