class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        wordslist = text.split()
        for word in wordslist:
            if not any(i in brokenLetters for i in word):
                count += 1
        return count