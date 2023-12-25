"""
Words Concatenation (Substring with Concatenation of All Words)

Problem Statement:

    You are given a string s and an array of strings words of the same length. 
    Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
    You can return the answer in any order.

Example 1:

    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

Example 2:

    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []

Example 3:

    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]

Constraints:

    1 <= s.length <= 104
    s consists of lower-case English letters.
    1 <= words.length <= 5000
    1 <= words[i].length <= 30

words[i] consists of lower-case English letters.
"""
def words_concatenation(s:str,words:list[str])->list[int]:
    if len(words)==0 or len(words[0])==0: return []
    output = []
    words_dict:dict[str,int] = {}
    words_seen :dict[str,int] = {}
    for word in words: words_dict[word] = words_dict.get(word,0)+1
    #all words are of equal le  ngth so words[0] is considered for total length
    len_s,words_count,word_len = len(s),len(words),len(words[0])
    #max value of window_start will be len(s)-total words count
    for window_start in range((len_s-words_count*word_len)+1):
        j=0
        while j<words_count:
            words_start_idx = window_start+j*word_len
            word = s[words_start_idx:words_start_idx+word_len]
            if word not in words_dict:
                #because we don't need this word to be considered (increment window_start)
                break
            words_seen[word] = words_seen.get(word,0)+1
            if words_seen[word]>words_dict[word]:
                #more word occurances are seen than in words dict so no need to process
                break
            j+=1
        #after while loop if j is words_cnt then entire while loop executed without break statements
        if j==words_count:
            output.append(window_start)
        words_seen.clear()
    return output

if __name__=="__main__":
    print(words_concatenation(s = "barfoothefoobarman", words = ["foo","bar"]))
    print(words_concatenation(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
    print(words_concatenation(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
    print(words_concatenation(s="aaa",words=["a","a"]))#[0,1]