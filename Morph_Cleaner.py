import re

regex = re.compile("(\{.*\})*")
with open("Morph_Parsed.txt", "r") as corpus, open("Morpheme_Roots.txt", "w") as out:
    text = corpus.read()
    lines = text.split("\n")
    for line in lines:
        words = line.split(" ")
        l = ""
        for word in words:
            if(re.match(regex, word)):
                w = word.replace("{", " ")
                w = w.replace("}", " ")
                morphemes = w.split(" ")
                for morpheme in morphemes:
                    if morpheme != "":
                        m = morpheme.split(":")
                        if(len(m) > 1):
                            m = m[1].split("/")
                            l += " {}".format(m[0])
                        else:
                            l += " {}".format(m[0])

            else:
                l += " {}".format(word)
        l = l.lstrip()
        out.write(l + "\n")
