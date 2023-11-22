passwords = open("encryption_policies.txt", "r")

wrong_passwords = 0
for line in passwords:
    times, letter, word = line.split(" ")
    min, max = times.split("-")
    letter = letter[0]
    count = word.count(letter)
    if count < int(min) or count > int(max):
        wrong_passwords+=1

    if wrong_passwords == 42:
        print(word)
        break 
    

