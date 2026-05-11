class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # Mapping sorted char to list of Anagarams

        for word in strs:
            key = ''.join(sorted(word))

            hashmap[tuple(key)].append(word)


        return list(hashmap.values())