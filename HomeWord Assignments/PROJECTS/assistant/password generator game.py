
import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase  # lowercase letters
    s2 = string.ascii_uppercase  # uppercase letters
    s3 = string.digits  # digits
    s4 = string.punctuation  # punctuation symbols
    
    plen = int(input("Enter the length of password: "))  # Length of password to be generated

    # Combine all the character sets into one list
    s = []
    s.extend(list(s1))  # add lowercase letters
    s.extend(list(s2))  # add uppercase letters
    s.extend(list(s3))  # add digits
    s.extend(list(s4))  # add punctuation

    # Shuffle the list of characters to ensure randomness
    random.shuffle(s)

    # Generate the password by selecting 'plen' number of characters from the shuffled list
    password = "".join(random.sample(s, plen))

    # Print the generated password
    print("Your password is:", password)











# import string
# import random

# if __name__ == "__main__":
#  s1 = string.ascii_lowercase
# # print(s1)
# s2 = string. ascii_uppercase
# # print(s2)
# s3 = string.digits
# # print(s3)
# s4 = string.punctuation
# # print(s4)
# plen = int(input("Enter the length of password\n")) # Todo1 :handle gibbersish
# s=[]
# s = s.extent(list(s1))
# s = s.extent(list(s2))
# s = s.extent(list(s3))
# s = s.extent(list(s4))
# # print(s)
# random.shuffle(s)
# # print(s)
# print ("Your password is :")
# # print (" ".join(s[0:plen]))
# password =(" " .join(random.sample(s,plen)))
# print("Your password is:", password)