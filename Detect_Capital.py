class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower(): #checks if entire word is captial 
            return True
        else:
            for i in range(len(word)): #accesses each item by index
                if i == 0: 
                    if word[i].islower(): #if index 0 is lowercase, return false
                        return False
                else:
                    if word[i].isupper(): #if any other letter is a capital, return false
                        return False
            return True
            
                