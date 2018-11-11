import os
import re
from hazm import Normalizer
import CorrectCodings

def make_directory(out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)


punctuations = ["!", "\"", "#", "(", ")", "?", "*", ",", "-", "_","/", ":", "[", "]", "«", "»", "،", "؛", "؟", "+",
                    "-", "…","$", "|", "{", "}", "٫", ";", ">", "<", "@", "\\\\", "."]
punct_str = "،#!\"#()?*,-_./:[]«» +-…$|{}٫;><@\\\\"
digits = "۰۱۳۲۴۵۶۷۸۹"
whitespace_chars = "\t\x0b\x0c\r\x1c\x1d\x1e\x1f \x85\xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000\u180e\u200b\u200c\u200d\u2060\ufeff"

normalizer = None
incorrect = None
correct = None


def prepare_line(line):
    global normalizer, incorrect, correct, unicode_redundant_chars, whitespace_chars, digits, punct_str, punctuations
    if normalizer is None:
        normalizer = Normalizer()
        incorrect, correct = CorrectCodings.loadCodings("TableCodings.txt")

    line = normalizer.normalize(line)
    line = CorrectCodings.CorrectCodingInLine(line, incorrect, correct)
    # remove prefix
    pat = re.compile(r"https?(.)*[^\s]+")
    line = re.sub(pat, r" ", line)

    pat = re.compile(r"\\n")
    line = re.sub(pat, "\n", line)
    pat = re.compile(r"([^\sا-ی۰-۹a-zA-Z\d])")
    line = re.sub(pat, r" \1 ", line)

    for p in punctuations:
        pat = re.compile(r"([" + punct_str + "])")
        line = re.sub(pat, r" \1 ", line)

    pat = re.compile(r"([" + digits + "]+)")
    line = re.sub(pat, r" \1 ", line)
    pat = re.compile(r" +")
    line = re.sub(pat, r" ", line)
    pat = re.compile(r"\n+")
    line = re.sub(pat, r" \n ", line)
    pat = re.compile("[" + whitespace_chars + "]+")
    line = re.sub(pat, r" ", line)
    line = line.strip()
    return line


def prepareZanaTweets(in_path, out_path, out_file):
    #Get tweeter data path and find its files.
    print("Preparing Tweets")
    dir_list = os.listdir(in_path)
    make_directory(out_path)
    c = 0
    pr_f = open(out_path + out_file, "w+", encoding="UTF8")
    #Normalize tweeter data.
    for filename in dir_list:
        if filename.endswith(".json"):
            print(filename)
            for line in open(in_path + filename, encoding="UTF8"):
                line = line.strip()
                if line.startswith('"content"'):
                    match = re.search(r"^\s*\"content\":\"(RT )?(@[^\s]*[ :])*(.*)\"},$", line)
                    if (match):
                        line = match.group(3)

                    line = prepare_line(line)

                    c += 1
                    if c > 12000000:
                        break
                    if c % 100000 == 0:
                        print(c, " tweets in progress")
                    if len(line) > 1:
                        pr_f.write(line+"\n")


def prepareHamshahri(in_path, out_path, out_file):
    #Get Hamshahri data path and its files.
    print("preparing Hamshahri")
    dir_list = os.listdir(in_path)
    make_directory(out_path)
    #Normalize Hamshahri data.
    c = 0
    pr_f = open(out_path +out_file, "w+", encoding="UTF8")
    for filename in dir_list:
        if filename.endswith(".txt"):
            with open(in_path+filename, encoding="UTF8") as f:
                t = f.readlines()

            ind_title = t.index('#عنوان\n')
            ind_content = t.index('#متن خبر\n')
            content = t[ind_title+2] + ". " + t[ind_content+1]

            content = prepare_line(content)

            if len(content) > 1:
                pr_f.write(content+"\n")

            c += 1
            if c%10000 == 0:
                print(c, " hamshahri in progress")
