import operator

def CountWordsFile(Path, corpusFilename, frequencyFileName):

    ''' Returns the number of words in a text.
    Input : name of the file (str) It's the address.
    Output : number of all words, all unique words and the repetition of each unique word (int)
    '''
    #with open(TextFilename,"r", encoding="utf-8") as file:
        #text = file.read()
    print("Count Words in Files")
    freq = {}

    c = 0
    for line in open(Path+corpusFilename, encoding="UTF8"):
        line = line.strip()
        for word in line.split(' '):
            freq[word] = freq.get(word, 0) + 1
        c+=1
        if c % 1000000 == 0:
            print("Count word in progress ", c)

    print("Sort Started")
    sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
    sorted_freq.reverse()
    print("Sort Ended")

    f =  open(Path + frequencyFileName, "w+", encoding="UTF8")

    for word, frequency in sorted_freq:
        if frequency < 3:
            break
        else:
            f.write(word + "\t" + str(frequency)+"\n")

    return sorted_freq

