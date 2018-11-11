import CountWordsFile
import SelectLexicon
import ReplaceOOV
import prepare_data
import w2v
import os

#Unify the codings.
tweetsPath = "/Users/sara/Documents/Zana_Tweets/"
tweetsOutFile = "TweeterNormalized.txt"
hamshahriPath = "/Users/sara/Documents/Hamshahri/result/"
hamshahriOutFile = "HamshahriNormalized.txt"
corpusPath = "/Users/sara/Documents/Corpora/"
corpusFileName = "CorpusNormalized.txt"
frequencyFileName = "Frequencies.txt"
lexiconFileName = "Lexicon.txt"
oovCorpusFileName = "CorpusNoOOV.txt"
modelFileName = "Model.w2v"
wordVectorFileName = "WordVectors.txt"

prepare_data.prepareHamshahri(hamshahriPath, corpusPath, hamshahriOutFile)
prepare_data.prepareZanaTweets(tweetsPath, corpusPath, tweetsOutFile)

#combine files
print("Combining Corpora")
os.system("cat {} {} > {}".format(corpusPath+tweetsOutFile, corpusPath+hamshahriOutFile, corpusPath+corpusFileName))

#Get word frequencies.
CountWordsFile.CountWordsFile(corpusPath, corpusFileName, frequencyFileName)

#Extract the lexicon.
SelectLexicon.SelectLexicon(corpusPath, frequencyFileName, lexiconFileName)

#Replace out of vocabulary words.
ReplaceOOV.ReplaceOOV(corpusPath, corpusFileName, lexiconFileName, "خاو", oovCorpusFileName)

#Train Network
w2v.TrainAndSaveModel(corpusPath, oovCorpusFileName, modelFileName, wordVectorFileName)
