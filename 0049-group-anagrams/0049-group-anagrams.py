class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for x in strs:
            letters = [0] * 26
            for let in x:
                letters[ord(let) - ord('a')] += 1
            if tuple(letters) in anagrams:
                anagrams[tuple(letters)].append(x)
            else:
                anagrams[tuple(letters)] = [x]
        return list(anagrams.values())




        