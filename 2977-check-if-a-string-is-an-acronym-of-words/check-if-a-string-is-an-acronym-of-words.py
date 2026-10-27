class Solution(object):
    def isAcronym(self, words, s):

        if len(words) != len(s):
          return False
        return all(word[0] == char for word, char in zip(words, s))
