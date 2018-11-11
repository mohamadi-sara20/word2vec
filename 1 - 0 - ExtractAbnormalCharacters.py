import re

def FindAbnormalCharacters(Path):
    l = []
    pat = re.compile(r"([^\sا-ی۰-۹a-zA-Z\d])")

    for line in open(Path, encoding="UTF8"):
        match = re.findall(pat, line)
        for element in match:
            if element not in l:
                l.append(element)
        l.sort()
    return l

print(FindAbnormalCharacters("/Users/sara/Documents/Corpora/HamshahriNormalized.txt"))
print(FindAbnormalCharacters("/Users/sara/Desktop/TweeterNormalized 4.02.07 pm.txt"))
