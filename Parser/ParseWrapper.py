import os
import sys

class Parser:
    """
    Takes an Inuktitut string and returns possible morphologocal parses.
    """
    def MorphologicalParse(self, word):
        return os.popen("java -cp .:Uqailaut.jar:junit.jar MorphologicalParseWrapper \"{}\"".format(word)).read()

    """
    Takes a morphological parse and returns the meaning parse.
    """
    def MeaningParse(self, MParse):
        return os.popen("java -cp .:Uqailaut.jar:junit.jar MeaningParseWrapper \"{}\"".format(MParse)).read()

if __name__ == "__main__":
    p = Parser()
    morph = p.MorphologicalParse(sys.argv[1])
    morph = morph.split("\n")[0]
    print("First Morphogical Parse: {}".format(morph))
    meaning = p.MeaningParse(morph)
    print("Meaning Parse: {}".format(meaning))
