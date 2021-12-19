import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

plen = int(input("\x1b[38;2;233;229;10mEnter password length: \x1b[m"))

s= []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z','!','@','#','$','&','1','2','3','4','5','6','7','8','9','0']

print("\x1b[38;2;13;199;206m Your password: \x1b[m",end=" ")
print(" ".join(random.sample(s, plen)))
