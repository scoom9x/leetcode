class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        if len(strs) == 1:
            return prefix

        for word in strs[1:]:
            if len(word) < len(prefix):
                prefix = prefix[: len(word)]

            cut = len(prefix)
            while prefix[:cut] != word[:cut]:
                cut -= 1
            prefix = prefix[:cut]
        return prefix
