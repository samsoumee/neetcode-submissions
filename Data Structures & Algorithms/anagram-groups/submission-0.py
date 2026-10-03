class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {} 

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in ht:
                ht[sorted_word].append(word)
            else:
                ht[sorted_word] = [word]
        return list(ht.values())