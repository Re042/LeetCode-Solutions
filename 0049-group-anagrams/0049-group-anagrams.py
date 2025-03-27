class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for x in strs:
            letters = [0] * 26
            for let in x:
                letters[ord(let) - ord('a')] += 1
            anagrams[tuple(letters)] = [x] + anagrams.get(tuple(letters), [])
        return list(anagrams.values())




        