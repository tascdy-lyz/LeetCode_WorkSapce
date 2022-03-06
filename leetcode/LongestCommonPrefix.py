

'''
    最长公共前缀
'''


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))