def loadCodings(TableCodingsFile):
    # Open the file containing the codings and remove '\ufeff' character.
    with open(TableCodingsFile, encoding="UTF-8") as f:
        content = f.read().split("\n")
        list_content = list(content)[1:]
        codings = [i.split("\t") for i in list_content]
    inc = [i[0] for i in codings]
    c = [i[1] for i in codings]
    return inc, c


def CorrectCodingInLine(line, incorrect, correct):
    # Correct the codings.
    normalized_line = ""
    for i in range(len(line)):
        if line[i] in incorrect:
            ind = incorrect.index(line[i])
            normalized_line += correct[ind]
        else:
            normalized_line += line[i]
    return normalized_line


def CorrectCodingInFile(Path, InTextFilename, TableCodingsFile):
    ''' Returns the text with correct, unified coding.
    Input: InTextFilename(str), TableCodings(str)
    Output: normalized_text (str)
    '''
    incorrect, correct = loadCodings(TableCodingsFile)
    #Open the file to be corrected.
    for line in open(Path+InTextFilename, encoding="UTF-8"):
        normalized_line = CorrectCodingInLine(line, incorrect, correct)
        #Write the result to a file.
        with open(Path + "CorpusAllCodings.txt", "a+", encoding = "UTF8") as g:
            g.write(normalized_line)

    return
