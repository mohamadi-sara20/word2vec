
def ReplaceOOV(Path, Corpus, Lexicon, oovPhrase, oovCorpusFileName):
    print("Replace OOV")
    with open(Path + Lexicon, encoding="UTF8") as f:
        Lexicon = f.read().split("\n")

    vocab = {}
    for word in Lexicon:
        vocab[word] = 1

    NoOOV = open(Path + oovCorpusFileName, "w+", encoding="UTF8")
    c = 0
    for Line in open(Path + Corpus, encoding="UTF8"):
        Line = Line.split()
        LineNoOOV = ""
        for word in Line:
            if word in vocab:
                LineNoOOV += word + " "

            else:
                LineNoOOV += oovPhrase + " "

        LineNoOOV = LineNoOOV.strip()
        NoOOV.write(LineNoOOV + "\n")
        c += 1
        if c % 100000 == 0:
            print("Replace OOV Progress: ", c)

    return


