class Palindrome:

    @staticmethod
    def is_palindrome(word):
#just setting all characters to lower case for simplicity
        word=word.lower() 
        l=len(word)
        for letter in word:
            if letter!=word[l-1]:
                return False
            l=l-1
        return True

print(Palindrome.is_palindrome('Deleveled'))