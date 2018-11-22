## load the corpora
import random
import string

#translator = str.maketrans('', '', string.punctuation.replace("'", "").replace("-",""))
#quote = str.maketrans("'-", '  ')
def load_parallel_corpora(file1, file2):
    '''
    Load the two datasets
    and split into train, test sets
    '''
    random.seed(1)
    par = {}
    line_ID = 0
    with open(file1, "r") as engl, open(file2, "r") as inuk:
        for e_line, i_line in zip(engl, inuk):
            if (e_line.strip() =="") or (i_line.strip()==""):
                continue
            e_line = e_line.strip().lower()#.translate(translator).translate(quote)
            i_line = i_line.strip().lower()#.translate(translator).translate(quote)
            par[line_ID] = (e_line, i_line)
            line_ID += 1
    print(line_ID)
    #test_keys = set(random.sample(range(1, line_ID+1), 50000))
    test_keys = set(range(1, 100))
    train = {}
    test = {}
    for k in par:
        if k in test_keys:
            test[k] = par[k]
        else:
            train[k] = par[k]
    return (train, test)



train, test = load_parallel_corpora("English_Parsed.txt", "Inuktitut_Parsed.txt")
#print(train[1])
print(test)
