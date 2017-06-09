def pigtransWord(word):
    input = list(word)
    input[0] = ''
    last = word[0]+ "ay"
    newstr = str(input) + last
    return "".join(input) + last
def pigtransSentece(sentence):
    words = sentence.split(" ")
    results = ""
    for x in words:
        results += pigtransWord(x) + " "
    print results
def game():
    type = raw_input("Would you like to translate 1.word or 2. sentence")
    type = int(type)
    if type == 1:
        word = raw_input("Write your word and type enter")
        if len(word)!=0:
            print pigtransWord(word)
        else:
            print "Write a non empty word"
    elif type ==2:
        sentence = raw_input("Write your sentence and type enter")
        if len(sentence)!=0:
            print pigtransSentece(sentence)
        else:
            print "Write a non empty sentence"
    else:
        print "Error input"
        game()



game()
