# 1). Parse them into 2 dictionaries
# 2). Morphologically decompose Inuktitut sentences
#     2b. maybe later we decompose English let's see how it goes
# 3).
import string
translator = string.maketrans(string.punctuation, ' '*(len(string.punctuation))) #map punctuation to space

with open("SentenceAligned.v2.txt", "r") as corpus:
    with open("English_Parsed.txt", "w") as engl:
        with open("Inuktitut_Parsed.txt", "w") as inuk:
            i_line = True
            for line in corpus:
                if any(c.isalpha() for c in line):
                    clean_line = line.translate(translator)
                    if i_line:
                        inuk.write(clean_line)
                    else:
                        engl.write(clean_line)
                    i_line = not i_line
