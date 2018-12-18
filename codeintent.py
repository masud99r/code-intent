import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
def wordscore(taglistpath):
    #stackoverflow tag list
    tagscore = {}
    extendedTags = {}
    with open(taglistpath) as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            tag, count = line.split("\t")
            count = float(count)
            #extract single word tag
            tagwords = str(tag).split("-") #updated
            for singletag in tagwords:
                if is_number(singletag) == False:  # exclude only number as tag
                    if singletag in extendedTags:
                        countval = extendedTags[singletag]
                        extendedTags[singletag] = countval + count #added with compound tag count
                    else:
                        extendedTags[singletag] = count
    for tag in extendedTags:
        count = extendedTags[tag]
        codeScore = 1.0 + (math.log(count, 2))  # log2(count)
        if tag not in tagscore:
            tagscore[tag] = codeScore
    #print tagscore
    return tagscore
def normalization(str1):
    nstr = str(str1).lower()
    nstr = nstr.strip()
    return nstr
def codeness(docstr):
    docstr = normalization(docstr)
    so_taglistpath = "single_occurance_taglist.txt"
    stackTagScore = wordscore(so_taglistpath)
    words = docstr.split(" ")
    codescore_SO = 0.0
    for word in words:
        if word in stackTagScore:
            word_score = stackTagScore[word]
            codescore_SO += word_score
    # add other form of score here
    # normalized with the doc len?
    # contains API keyword?
    # language keyword?
    codenessScore = codescore_SO #add up all types of score
    return codenessScore
def codeness_norm(docstr):
    docstr = normalization(docstr)
    so_taglistpath = "single_occurance_taglist.txt"
    stackTagScore = wordscore(so_taglistpath)
    words = docstr.split(" ")
    codescore_SO = 0.0
    for word in words:
        if word in stackTagScore:
            word_score = stackTagScore[word] #word_
            codescore_SO += word_score
    # add other form of score here
    # contains API keyword?
    # language keyword?
    codenessScore = codescore_SO / len(words) # assuming non-zero length sentence, normalizing by doc length
    return codenessScore
def samplecodeness():
    q1 = "javascript mp3 play time"
    codescore = codeness(q1)
    print (q1+"\t"+str(codescore))

    q1 = "javascript get track length from meta data"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "how to perform xml serialization for parameterless constructor in c#"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "elasticsearch.net & nest installed post nuget source control stop notification"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))


    q1 = "acer e700 review"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "houston luxury suv rental"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "messi curly goal"
    codescore = codeness(q1)
    print (q1 + "\t" + str(codescore))
def samplecodeness_norm():
    q1 = "javascript mp3 play time"
    codescore = codeness_norm(q1)
    print (q1+"\t"+str(codescore))

    q1 = "javascript get track length from meta data"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "how to perform xml serialization for parameterless constructor in c#"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "elasticsearch.net & nest installed post nuget source control stop notification"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))


    q1 = "acer e700 review"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "houston luxury suv rental"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))

    q1 = "messi curly goal"
    codescore = codeness_norm(q1)
    print (q1 + "\t" + str(codescore))

if __name__ == '__main__':
	samplecodeness()
	#samplecodeness_norm()