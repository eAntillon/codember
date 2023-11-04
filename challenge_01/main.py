
messageData = open("message_01.txt", "r").read()
repitedWords = {}
repitedWordsOrder = []

for word in messageData.split():
    if word in repitedWords:
        repitedWords[word] += 1
    else:
        repitedWords[word] = 1
        repitedWordsOrder.append(word)


text = ""
for word in repitedWordsOrder:
    text += word + str(repitedWords[word])

print(text)