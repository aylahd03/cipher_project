import os
import requests

print ("Hello, and welcome to my Ciper Program.")

normaltext = input("Enter the text that you want encrypted")          
n = int(input("Enter the shift"))
print("Normal Text is: " + normaltext)
print("Shifting : " + str(n))

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

print("Encrypted Text is: " + encrypt_text(normaltext,n))
    

    