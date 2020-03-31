"""You are playing the following Bulls and Cows game with your friend:
 You write down a number and ask your friend to guess what the number is.
  Each time your friend makes a guess, you provide a hint that indicates 
  how many digits in said guess match your secret number exactly in both digit and position
   (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). 
   Your friend will use successive guesses and hints to eventually derive the secret number.
Write a function to return a hint according to the secret number and friend's guess,
 use A to indicate the bulls and B to indicate the cows. 
Please note that both secret number and friend's guess may contain duplicate digits.
"""
class Solution(object):
    def getHint(self, secret, guess):
        self.secret=secret
        self.guess=guess
        bulls=0
        cows=0
        secret=list(secret)
        guess=list(guess)
        length=len(secret)
        for i in range(length):
            
            if secret[i] ==guess[i]:
                bulls+=1
                secret[i]=None
                guess[i]=None
        for j in range(length):
            
                if secret[j] in guess and secret[j] is not None:
                    ind=guess.index(secret[j])
                    guess[ind]=None
                    cows+=1
        k=str(bulls)+"A"+str(cows)+"B"
        return k
            

        
        
        
        

        
    


