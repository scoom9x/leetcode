def groupAnagrams(strs):
    lis = []
    used = set()
    for a, b in enumerate(strs):
        lis2 = []
        lis2.append(b)

        if a in used:
            continue

        for d in range(a + 1, len(strs)):
            if isAnagram(b, strs[d]) and d not in used:
                lis2.append(strs[d])
                used.add(d)

        lis.append(lis2)
    return lis


def isAnagram(word, target):
    if len(word) != len(target):
        return False
    count = [0] * 26

    for i in range(len(word)):
        count[ord(word[i]) - ord("a")] += 1
        count[ord(target[i]) - ord("a")] -= 1

    for val in count:
        if val != 0:
            return False

    return True


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
