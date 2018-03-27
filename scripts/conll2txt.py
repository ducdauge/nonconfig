# -*- coding: utf-8 -*-
import codecs, sys, os
fname = sys.argv[1]
fin = codecs.open(fname, "r")
lemmas = []
pairs = []
cursent = []
for i, l in enumerate(fin):
    if l.strip() == "":
        for i in range(1, len(cursent)):
           pairs.append([cursent[i-1], cursent[i]])
        cursent = []
    else:
        lemma = l.split("\t")[2]
        cursent.append(lemma)
        lemmas.append(lemma)
print len(set(lemmas))
fout = codecs.open(os.path.splitext(fname)[0] + ".txt", "w")
for p in pairs:
    fout.write(p[0] + "\t" + p[1] + "\t1\n")
fout.close()
