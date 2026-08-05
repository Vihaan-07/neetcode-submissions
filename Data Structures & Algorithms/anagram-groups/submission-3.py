class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create an empty dictionary
        # iterate through strs' elements
        # create a sorted list of chars for each element
        # eg. cats becomes ['c', 'a', 't', 's'].sort()
        # this list becomes a key in our dict and then the corresponding value will be all strings with the same char list
        # finally, we return the items list

        anagram_dict = {}
        for s in strs:
            key = str(sorted(list(s)))
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]
        
        return list(anagram_dict.values())

        