

with open("Inuktitut_Parsed.txt", "r") as inuk, open("English_Parsed.txt", "r") as engl, open("tune.in", "w") as itune, open("tune.en", "w") as etune, open("test.in", "w") as itest, open("test.en", "w") as etest:
    ct = 1
    for iline in inuk:
        if ((ct >= 100000) & (ct < 106000)):
            itune.write(iline)
        elif ((ct >=106000) & (ct < 112000)):
            itest.write(iline)
        else:
            if (ct >= 112000):
                continue
        ct += 1
    ct = 1
    for eline in engl:
        if ((ct > 100000) & (ct < 106000)):
            etune.write(eline)
        elif ((ct >=106000) & (ct < 112000)):
            etest.write(eline)
        else:
            if (ct >= 112000):
                continue
        ct += 1

with open("Underlying_Morpheme.txt", "r") as inuk, open("morphtune.in", "w") as itune, open("morphtest.in", "w") as itest:
    ct = 1
    for iline in inuk:
        if ((ct >= 100000) & (ct < 106000)):
            itune.write(iline)
        elif ((ct >=106000) & (ct < 112000)):
            itest.write(iline)
        else:
            if (ct >= 112000):
                continue
        ct += 1
