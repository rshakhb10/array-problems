'''Implementation of naive algorithm of checking if string is substring
If it is, returns all the occurences and indexes.'''

def find_substr(seq, subseq):
    match_inds = []
    for i in range(0, len(seq)):
        match_count = 0
        for j in range(0, len(subseq)):
            if seq[i+j] == subseq[j]:
                match_count +=1
            else:
                break

        if match_count == len(subseq):
            match_inds.append(str(i))

    return match_inds



match_inds = find_substr("dddhhsjkabcjjjkkk", "dd")
if match_inds:
    print "Match found at: ", ",".join(match_inds)
else:
    print "No match found..." 



