# Cipers Assignemnt
print("hello")
import os
import requests

print ("Hello, and Welcome to My Ciper Program. Below you will see instructions for how to continue.")
print ("Start thinking about what you want your ciper to be and what information you migth input. Next we'll set up our starting alphabet.")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabet)

user_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("enter a number 1-10")
user_input = {}
if user_input is 1:
    print ("b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a")



# Tip from prof
some_string = "here is a sentence"
print(some_string[5])
for char in some_string:
    print(char)
   


# From scratch 

# n = spaces moving to encrypt

def encrypt_text(normaltext,n):
    ans = " "
    # getting the english/normal text
    for i in range(len(normaltext)):
        ch = normaltext[i]

        # adding a space if there isn't one
        if ch==" ":
            ans+=" "
        
        elif (ch.upper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

normaltext = input("Enter a text")          
# normaltext = "Ciper test text"
n = 8
print("Normal Text is: " + normaltext)
print("Shifting : " + str(n))
print("Ciper Text is: " + encrypt_text(normaltext,n))
    
# Questions for OH 
    # How to run program from the command line
    # How to work github / confusion around that
    
ord("a")
ord("A")