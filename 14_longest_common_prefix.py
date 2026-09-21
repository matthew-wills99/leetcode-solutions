class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pfx = ""
        sizeOfShortest = 201

        for str in strs:
            if len(str) < sizeOfShortest: sizeOfShortest = len(str)

        breakAll = False
        for i in range(sizeOfShortest):
            cur = strs[0][i]
            for str in strs:
                if str[i] != cur: 
                    breakAll = True
                    break

            if breakAll: break
            pfx += cur

        return pfx