import os
import sys

class Parser:
    def MorphologicalParse(self, word):
        return os.popen("java -cp .:Uqailaut.jar:junit.jar MorphologicalParseWrapper \"{}\"".format(word)).read()

    def MeaningParse(self, word):
        return os.popen("java -cp .:Uqailaut.jar:junit.jar MeaningParseWrapper \"{}\"".format(word)).read()

if __name__ == "__main__":
    p = Parser()
    print(p.MeaningParse(sys.argv[1]))
