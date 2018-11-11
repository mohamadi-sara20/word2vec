
def SelectLexicon(Path, freqFilename, lexiconFileName):
    print("SelectLexicon")
    with open(Path + freqFilename, encoding="UTF8") as f:
        Content = f.read().split("\n")
        # words = [word1\tfrequency1 \n word2\tfrequency2 \n ...]

    L = open(Path + lexiconFileName, "w+", encoding="UTF8")
    for item in Content:
        item = item.split("\t")
        L.write(item[0]+"\n")

    return
