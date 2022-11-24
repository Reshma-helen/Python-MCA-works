'''word1=input("enter")
char=word1[0]
word=word1.replace(char,'$')
word=char+word[1:]
print("before" ,word1)
print("after", word)'''


'''def change_char(str1):

    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]

    return str1


word=input("Enter any word")
print("Before replacement: ",word)
print("After replacement: ",change_char(word))'''

word_1=input("Enter any word :")

word=list(word_1)
word[0],word[-1]=word[-1],word[0]
word_2="".join([str(elem) for elem in word])

print(word_2)



