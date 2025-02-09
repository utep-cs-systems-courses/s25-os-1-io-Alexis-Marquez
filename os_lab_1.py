import os
import sys

def read_words_from_file(filename):
    fileID = os.open(filename, os.O_RDONLY)
    buff = os.read(fileID, 1)
    words = {}
    word = ''
    while len(buff):
            letter = buff.decode()
            letter = letter.lower()
            if letter.isalnum():
                word += letter
            if not letter.isalnum():
                if word:
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                word = ''
            buff = os.read(fileID, 1)
    os.close(fileID)
    return words


def writeToFile(words, filename):
    fileID = os.open(filename, os.O_CREAT | os.O_WRONLY)
    assert fileID >= 0
    for word in words.keys():
        buff = (word + ": "+ str(words[word]) +"\n").encode()
        wc = os.write(fileID, buff)
    os.fsync(fileID)
    os.close(fileID)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input-filename> <output-filename>")
    else:
        filename = sys.argv[1]
        words = read_words_from_file(filename)
        words = dict(sorted(words.items()))
        writeToFile(words, sys.argv[2])
