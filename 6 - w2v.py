from gensim.models import Word2Vec
import time

epoch = 0
class MySentencesInFile(object):
    def __init__(self, file_name):
        self.fileName = file_name

    def __iter__(self):
        c = 0
        global epoch
        epoch += 1
        for line in open(self.fileName):
            c += 1
            if c % 100000 == 0:
                print("V2v In Progress epoch=", epoch, " sentence:", c)
            line = line.strip()
            yield line.split()


def TrainAndSaveModel(path, inputFilename, modelFileName, wordVectorFileName):
    print("Train Network")
    t1 = time.clock()
    sentences = MySentencesInFile(path+inputFilename)
    model = Word2Vec(sentences, size=200, window=10, min_count=3, workers=4, sg=1, negative=40,  iter=10)
    print("Save Model")
    model.save(path+ modelFileName)
    print("Save Word Vector")
    model.wv.save_word2vec_format(fname=path + wordVectorFileName, fvocab=None, binary=False)
    t2 = time.clock()
    print(t1, t2)
    print(t2 - t1)
