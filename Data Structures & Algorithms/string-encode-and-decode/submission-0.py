class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs:
            sizes = []
            res = ""
            for string in strs:
                sizes.append(len(string))
            for i in range(len(strs)):
                res += str(sizes[i])
                res += ','
            res += '#' 
            for string in strs:
                res += str(string)
                
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
                 

            



