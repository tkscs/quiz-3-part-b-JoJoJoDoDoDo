import random
import string
import subprocess


def check_palindrome(word):
    if len(word) > 1:
        if word[0] == word[-1]:
            if len(word) > 2:
                word[1] == word[-2]
                if len(word) > 3:
                    word[2] == word[-3]
                    if len(word) > 4:
                        word[3] == word[-4]
                        if len(word) > 5:
                            word[4] == word[-5]
                            if len(word) > 6:
                                word[5] == word[-6]
                                if len(word) > 7:
                                        word[6] == word[-7]
                                        print("True")
                                    
                                else:
                                  print("False")
                            else:
                                print("False")
                        else:
                         print("False")
                    else:
                       print("False")
                else:
                    print("False")                             
            else:
             print("False")
        else:
            print("False")
    else:
        print("False")



check_palindrome("abba")