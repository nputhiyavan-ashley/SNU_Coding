
def main():
    sample_1 = "abcabcbb"
    sample_2 = "abcdef"

    # Custom cases, edge cases.
    sample_3 = "" # empty string
    sample_4 = "12 2 1 a A   "  # letters, digits, spaces, special characters

    print(findLongestSubstr(sample_1))
    print(findLongestSubstr(sample_2))
    print(findLongestSubstr(sample_3), "-1 specifies that the no starting index") 
    print(findLongestSubstr(sample_4))
    # output:
    # (3, 0)
    # (6, 0)
    # (0, -1) -1 specifies that the no starting index
    # (3, 0)
    

def findLongestSubstr(sample):
    mp = {}
    l = 0
    r = 0
    ans = ""
    start = -1
    for i in range(len(sample)): 
        if sample[i] not in mp:
            mp[sample[i]] = i
        else:
            if r - l > len(ans):
                ans = ""
                for i in range(l,r):
                    ans += sample[i]
                start = l   
            l = r
            mp[sample[r]] = i
        r+= 1
    if r - l > len(ans):
        ans = ""
        for i in range(l,r):
            ans += sample[i]
        start = l
    return len(ans), start
    
if __name__ == "__main__":
    main()

