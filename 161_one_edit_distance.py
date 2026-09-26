class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        if ls == lt:
            diff = 0
            for i, v in enumerate(s):
                if s[i] != t[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        elif abs(ls - lt) == 1:
            diff = 0
            ps, pt = 0, 0
            if ls > lt:
                s, t = t, s
                ls, lt = lt, ls
            while ps < ls and pt < lt:
                if s[ps] == t[pt]:
                    ps += 1
                    pt += 1
                    continue
                if s[ps] != t[pt]:
                    pt += 1
                    diff += 1
                if diff > 1:
                    return False
            return True

        else:
            return False

        # same length, if only one differece, continue, othervise false

        # different length, if len(s) == len(t)-1, if not == first time, move the right pointer of t

        # different lenght, if len(s) == len(t) +1, if not == first time, move the left pointer of s
# 这里有注意的一个优化点就是，最后2种情况其实是一样的，通过把字符串做交换，就可以少写代码。
# 然后同时需要注意的是，如果两者长度相同的情况下，是一定需要diff == 1的情况的，因为是exact one diff, 否则就没有变化了