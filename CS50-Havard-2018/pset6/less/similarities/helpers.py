from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    a_list = a.splitlines()
    b_list = b. splitlines()
    a_set = set(a_list)
    b_set = set(b_list)
    common_set = a_set.intersection(b_set)
    common_list = list(common_set)
    return common_list


def sentences(a, b):
    """Return sentences in both a and b"""
    a_list = sent_tokenize(a)
    b_list = sent_tokenize(b)
    simlist = set(a_list) & set(b_list)
    return set(simlist)


def helper_list_substr(s, n):
    ret = []
    for i in range(len(s) - n + 1):  # since not including n
        ret.append(s[i:i + n])
    return ret


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    return set(helper_list_substr(a, n)) & set(helper_list_substr(b, n))