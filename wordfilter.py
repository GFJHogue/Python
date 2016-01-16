# 2015-12-20
# * A short script that parses WhatsApp chat .txt files.
# * Removes all text that was not written by chat users.
# * Produces word.txt which can be used to analyse word-usage statistics or generate word-clouds.

# filterLine(line) filters line from unwanted text
# Str -> [listof Str]

def filterLine(line):
    lst = unicode(line, "utf-8")[:(len(line)-3)].split(" ")[3:]
    for i in range(len(lst) + 1):
        if (i == len(lst)):
            lst = []
        elif (":" in lst[i]):
            lst = lst[i+1:]
            break

    for i in range(len(lst)-1,-1,-1):
        if ("omitted>" in lst[i]):
            lst.pop(i)
            lst.pop(i-1)
            break
        
    return(lst)


# extractText(chatid) processes the WhatsApp chat with chatid
# Nat -> [listof Str]

def extractText(chatid):
    chatFile = file("chat" + str(chatid) + ".txt", "r")
    line = chatFile.readline()
    words = []
    i=0

    while line:
        words.extend(filterLine(line))   
        line = chatFile.readline()
    
    return(words)


# extractFiles(n) processes n WhatsApp chats named chat1.txt, chat2.txt, ...,
#     chatn.txt
# Nat -> [listofStr]

def extractFiles(n):
    words = []
    
    for i in range(1,n+1):
        print("chat" + str(i) + ".txt")
        words.extend(extractText(i))

    return(words)

    
# getWordsToFile(n) gets words from n WhatsApp chats named chat1.txt, chat2.txt, ...,
#     chatn.txt
# Nat -> Void

def getWordsToFile(n):
    outFile = file("words.txt", "w")
    words = extractFiles(n)

    for word in words:
        outFile.write(word.encode(encoding='UTF-8',errors='strict') + " ")

    print "Done"

getWordsToFile(3)
    
