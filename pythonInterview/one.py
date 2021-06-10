
##Format word in alphabetical Order
def alphabetWord(string):
    li = sorted(list(string))
    newString=''
    for wordFormatted in li:
        newString +=wordFormatted

    return newString

word=input('PLEASE ENTER A WORD:')
print(alphabetWord(word))

