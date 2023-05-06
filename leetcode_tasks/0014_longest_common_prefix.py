class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        minLen = min(map(len, strs))
        idx, ans = 0, ''
        flag = True
        while idx < minLen:
            cur = strs[-1][idx]
            for st in strs[:-1]:
                if st[idx] != cur:
                    flag = False
                    break
                    
            if flag:
                ans += cur
                idx += 1
            else:
                break

        return ans