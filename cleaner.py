


# with open("SentenceAligned.v2.txt", "r") as corpus, open("English_Parsed.txt", "w") as engl, open("Inuktitut_Parsed.txt", "w") as inuk, open("exclude.txt", "w") as ex:
#     line_index = 0
#     for line in corpus:
#         line_index += 1
#         if line_index % 4 == 0:
#             engl.write(line+"\r\n")
#         elif line_index % 2 == 0:
#             inuk.write(line+"\r\n")
#         else:
#             ex.write(line)
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
            engl.write(p[1]+"\r\n")
            inuk.write(p[0]+"\r\n")
