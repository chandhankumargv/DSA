class Solution(object):
    def buildArray(self, target, n):
        ans = []
        tp = 0
        st = 1
        while(tp <len(target)):
            ans.append("Push")
            if target[tp]==st :
                tp +=1
            else:
                ans.append("Pop")
            st += 1
        return ans

        