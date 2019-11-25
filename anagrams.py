#Input a list of strings and return a list 
#where the anagrams are grouped together

def groupAnagrams(words):
    result = []
    index_added = set()

    for i in range(len(words)):
        if(i not in index_added):
            index_added.add(i)
            check_against = words[i]
            inter_result = [check_against]
            for j in range(i, len(words)):
                if(j not in index_added):
                    if(check_if_anagram(check_against, words[j])):
                        inter_result.append(words[j])
                        index_added.add(j)
            result.append(inter_result)

    return result

def check_if_anagram(word1, word2):
    if(process(word1) == process(word2)):
        return True
    else:
        return False
    
def process(word):
    freq = {}
    for char in word:
        if(char in freq):
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(groupAnagrams(["yo", "oy", "aaa", "aaa", "rai", "iar", "lol", "llo"]))