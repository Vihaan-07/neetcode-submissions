class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output+= str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while s != '':
            index = int(s[0:s.index("#")])
            s = s[s.index("#")+1:]
            output.append(s[:index])
            s = s[index:]
        return output
        