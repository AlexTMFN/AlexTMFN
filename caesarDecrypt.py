def decrypt(text, step):

    result = ""
    for i in range(len(text)):
        decryptedChar = ((ord(text[i]) - 97 - step) % 26) + 97
        result = result + chr(decryptedChar)
    return result

text = "wklvzdvxvhgwrghfubswdfwiiurpslfrFWI"
print({decrypt(text, 3)})

