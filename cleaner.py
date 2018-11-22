
import re
import string

translator = str.maketrans('', '', string.punctuation.replace("'", "").replace("-",""))
quote = str.maketrans("'-", '  ')

with open("SentenceAligned.v2.txt", "r") as corpus, open("English_Parsed.txt", "w") as engl, open("Inuktitut_Parsed.txt", "w") as inuk, open("exclude.txt", "w") as ex:
    text = corpus.read()
    text = text.split("*************** ")
    i_ct = 0
    for pair in text:
        p = pair.split("-----")
        if len(p) != 2:
            continue
        else:
            if p[1].strip() == "":
                continue
            if ("moZos3=1u vtm0Jtu#5" in p[0]):
                continue
            p[0]= re.sub(r"[0-9]{8}", "", p[0])
            engl.write(p[1].lower().strip().translate(translator).translate(quote).strip()+"\r\n")
            inuk.write(p[0].lower().strip().translate(translator).translate(quote).strip()+"\r\n")
