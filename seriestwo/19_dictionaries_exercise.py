##Exercise
# phone = input('Phone:')

# digits_mapping={
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
#     "8":"Eight",
#     "9":"Nine"
# }


# output=''

# for ch in phone:
#     output += digits_mapping.get(ch, "!") + ""
    
# print(output)


message = input(">")

def emoji_converter(words):
    words=message.split(" ")
    emojis ={
        ":)":"SMILE",
        ":(":"SAD"
    }

    output =""

    for word in words:
        output += emojis.get(word,word) + " "

    return output

converted_words=emoji_converter(message)

print(converted_words)