
def make_test(path, filename):
    '''
    Returns the test set.
    '''
    with open(path+filename+".txt", encoding="utf8") as f:
        content = f.read().split("\n")
        content.pop(-1)
    words = []
    #Open test set file.
    f = open("TestSet.txt", "a+", encoding="UTF8")

    f.write(": " + filename+"\n")

    for line in content:
        item = line.split("\t")
        words.append(item) 
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                f.write(words[i][0] + "\t" + words[i][1] + "\t" + words[j][0] + "\t" + words[j][1])
                f.write("\n")



make_test("TestFiles/","GenderRoles")
make_test("TestFiles/", "CommonCountries")
make_test("TestFiles/", "an")
make_test("TestFiles/", "am")
make_test("TestFiles/", "mand")
make_test("TestFiles/", "om")
make_test("TestFiles/", "LocAntonyms")
make_test("TestFiles/", "GradableAntonyms")
make_test("TestFiles/", "ComplementaryAntonyms")



