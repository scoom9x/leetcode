import ast

class Solution:

    def encode(self, strs: List[str]) -> str:
        word_len = []
        word = ""

        for i, n in enumerate(strs):
            word_len.append(len(n))
            if i != len(strs) - 1:
                for x in n:
                    word += str(ord(x))
                    word += ","
                continue

            for j, x in enumerate(n):
                if j != len(n) - 1:
                    word += str(ord(x))
                    word += ","
                    continue
                word += str(ord(x))
            
        return str(word_len) + word

    def converint(self, wrd):
        if wrd == "":
            return ""
        return int(wrd)

    def converchr(self, wrd):
        if wrd == "":
            return ""
        return chr(wrd)

    def decode(self, s: str) -> List[str]:
        arr = s.split("]")[0] + "]"
        arr = ast.literal_eval(arr)
        print(arr)
        words_arr_ord = list(map(self.converchr, list(map(self.converint, s.split("]")[1].split(",")))))
        word_arr = []
        idx_sum = 0

        for n in arr:
            idx_sum += n
            idx_bck = idx_sum - n
            word_arr.append("".join(words_arr_ord[idx_bck:idx_sum]))

        return word_arr
