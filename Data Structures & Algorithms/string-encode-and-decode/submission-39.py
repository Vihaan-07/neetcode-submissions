class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        output = []
        while s != '':
            index = int(s[0:s.index("#")])
            s = s[s.index("#")+1:]
            output.append(s[:index])
            s = s[index:]
        return output
        