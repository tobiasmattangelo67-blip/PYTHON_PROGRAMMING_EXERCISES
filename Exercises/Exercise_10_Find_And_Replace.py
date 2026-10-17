
# def findAndReplace(text, oldText, newText):
#     replaceText = text
#     i = 0
#     while i < len(text):
#         if text[i:len(oldText) + i] == oldText:
#             replaceText = text.replace(text[i:len(oldText) + i], newText)
#         i += 1
#     return replaceText

def findAndReplace(text, oldText, newText):
    replaceText = ''
    i = 0
    while i < len(text):
        if text[i:len(oldText) + i] == oldText:
            replaceText += newText
            i += len(oldText)
        else:
            replaceText += text[i]
            i += 1
        
    return replaceText

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog' 
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog' 
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog' 
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

# text = 'the fox'
# oldText = 'fox'
# newText = 'dog'

# i = 0
# while i < len(text):
#     if text[i:len(oldText) + i] == oldText:
#         text = text.replace(text[i:len(oldText) + i], newText)
#     i += 1

# print(text)