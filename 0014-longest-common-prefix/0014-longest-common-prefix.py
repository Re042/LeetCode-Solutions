class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        pref = ""
        let = 0
        while True:
            if len(strs[0]) <= let:
                return pref
            tmp = strs[0][let]
            for i in range(1, len(strs)):
                if len(strs[i]) <= let or strs[i][let] != tmp:
                    return pref
            pref += tmp
            let += 1



            