vowels = set(('a', 'e', 'i', 'o', 'u'))

def reverse_vowels(sentence):
    sentence = sentence.lower()
    if (len(sentence) == 0):
        return ""
    i = 0 
    j = len(sentence) - 1
    while(i<j):
        if(sentence[i]  in vowels and sentence[j]  in vowels):
            sentence = swap(sentence, i, j)
            i+=1
            j-=1
        elif (sentence[i]  in vowels and not (sentence[j]  in vowels)):
            j -=1
        elif (not (sentence[i]  in vowels) and sentence[j]  in vowels):
            i +=1
        else:
            i+=1
            j-=1
    print(sentence)
    return sentence



def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)









def test():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("papergrid") == "pipergrad"
    assert reverse_vowels("TTT") == "ttt"
    assert reverse_vowels("AEIO") == "oiea"
    print("Test cases passed")

test()