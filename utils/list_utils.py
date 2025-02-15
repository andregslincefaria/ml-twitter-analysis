import itertools,operator

def accumulate(l):
    it = itertools.groupby(sorted(l), operator.itemgetter(0))
    for key, subiter in it:
       yield key, sum(item[1] for item in subiter)

def get_max(l):
    mx = max(l, key=operator.itemgetter(1))
    return mx

def get_features_prediction(x_input, features):
    if len(x_input[0]) == len(features):
        nonzero = [i for i, e in enumerate(x_input[0]) if e != 0]
        f_tmp = []
        for i in range(0,len(features)):
            if i in nonzero:
                f_tmp.append(i)
        tmp = zip([int(x_input[0][i]) for i in nonzero],[features[i] for i in f_tmp])
        return sorted(tmp,key=lambda x: x[0],reverse=True)
    else:
        raise ValueError("lists not equal")

def discardLowestOnEven(l,scores):
    l.pop(scores.index(min(scores)))
    scores.pop(scores.index(min(scores)))
    res = accumulate(zip(l, scores))
    if scores[1:] != scores[:-1]:
        mx = get_max(res)
        return mx[0]
    else:
        return l[scores.index(max(scores))]

if __name__ == '__main__':
    labels = ['PS','BE','PSP','CDS']
    scores = [0.6,0.3,0.4,0.4]
    #res = get_features_prediction([[1,3,0.0,0,2]],['k','k','nok','nok','g'])
    res = discardLowestOnEven(labels,scores)
    print(res)