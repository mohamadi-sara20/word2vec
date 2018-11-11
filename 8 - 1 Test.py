from gensim.models import Word2Vec
import numpy as np
import scipy

path1 = "/Users/sara/Documents/Corpora/Model1/Model.w2v"
path2= "/Users/sara/Documents/Corpora/Model2/Model.w2v"
model = Word2Vec.load(path1)
def OpenFile(Filename):
    '''Opens a file and stores each line as a list in another list'''
    with open(Filename, encoding="UTF8") as f:
        content = f.read().split("\n")
        content.pop(-1)
    words = []
    for line in content:
        line = line.split("\t")
        words.append(line)
    return words


def CompareWords(Filename):
    '''Compares pairs of words in a file. '''
    content = OpenFile(Filename)
    d = open("WordDistances.txt", "a+")
    for word in content:
        dist = model.wv.distance(word[0], word[1])
        sdist = "{:.3f}".format(dist)
        d.write(word[0] + "\t" + word[1] + "\t" + sdist + "\n")



def CompareMTUs(Filename):
    '''Compares MTUs with their separate forms.'''
    content = OpenFile(Filename)
    MTU = open("MTUsDistances.txt", "w+")
    for line in content:
        vsum = np.zeros(200, )
        words = ""
        for i in range(1, len(line)):
            vsum += model.wv[line[i]]
            words += line[i] + "\t"
        dist = scipy.spatial.distance.cosine(model.wv[line[0]], vsum)
        MTU.write(line[0] +"\t" + words + str(dist) + "\n")
    return




def ComputeAnalogyAccuracy(Filename):
    '''Compares word analogies. '''
    results = open("AnalogyResults.txt", "w+")
    global model
    res = model.wv.accuracy(Filename)
    total_correct = 0
    total = 0
    for item in res:
        total_correct = len(item['correct'])
        total = len(item['correct']) + len(item['incorrect'])
        print(item['section'] + " Accuracy: {0:.3f}".format(total_correct/total))
        results.write(item['section'].capitalize() + " Accuracy: {0:.3f}".format(total_correct/total) + "\n")
    return


ComputeAnalogyAccuracy("TestSet.txt")
CompareWords("TestFiles/adv.txt")
CompareWords("TestFiles/formal-informal.txt")
CompareWords("TestFiles/repetitiveChars.txt")
CompareMTUs("TestFiles/MTUs.txt")
