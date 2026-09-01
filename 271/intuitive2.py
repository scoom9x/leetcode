class Solution:

    def encode(self, strs: List[str]) -> str:
        st= ""
        for wrd in strs:
            st += str(len(wrd)) + "#" + wrd
        return st
            
            
    def decode(self, s: str) -> List[str]:
        wrd_lis = []
        while s.find("#") != -1:
            tag_idx = s.find("#")
            wrd_len = int(s[0:tag_idx])
            s = s[tag_idx + 1:]
            wrd_lis.append(s[0:wrd_len])
            s = s[wrd_len:]
        
        return wrd_lis