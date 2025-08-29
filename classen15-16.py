# #1
# text1 = "Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат."
# strLen = len(text)
# count = 0
# for i in range(0,strLen):
#     if(text[i]=="."):
#         count+=1
# print(count)
# #2
# word = input('enter your word')
# if(word.lower().replace(" ","") == word[::-1].lower().replace(" ","")):
#     print(word[::-1])
# # 3
# text3 = input('enter text:')
# text3 = "Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат."
# arrayOfWords = ['деякий','цьому','кількість']
# arrayLength = len(arrayOfWords)
# textLength = len(text3)
# #можно так
# for i in range(0,arrayLength):
#     indexWord = text3.find(arrayOfWords[i])
#     if(indexWord != False):
#       text3 = text3[0:indexWord]+text3[indexWord].upper()+text3[indexWord+1:textLength]
# print(text3)
#
#
# #а можно так
# for i in range(0,arrayLength):
#     text3 = text3.replace(arrayOfWords[i],arrayOfWords[i].capitalize())
# print(text3)
#
# #4
#
# text4 = "Є деякий текст. Порахуйте, в цьому тексті - кількість речень і виведіть на екран отриманий результат."
# firstSymbol = '.'
# secondSymbol = '-'
# firstSymbolIndex = text4.find('.')
# secondSymbolIndex = text4.find('-')
# bufferText = text4[firstSymbolIndex:secondSymbolIndex]
# print(len(bufferText))
# bufferTextNew = bufferText
# for i in range(0,(secondSymbolIndex-firstSymbolIndex)):
#     if not bufferText[i].isalnum():
#         if bufferText[i] != " ":
#             bufferTextNew = bufferTextNew.replace(bufferText[i],'')
# text4 = text4[0:firstSymbolIndex]+bufferTextNew+text4[secondSymbolIndex+1:len(text4)]
# print(text4)
#
# #5
# text5 = input('enter text:')
# arOfText5 = text5.split()
# symbols = input('enter symblos spaced:')
# arrayOfSymbols = symbols.split()
# for i in arOfText5:
#     for j in arrayOfSymbols:
#         if j in i:
#             arOfText5.remove(i)
# print(arOfText5)

#6
text6 = input('enter your text:')
arOfText6 = text6.split()
reversedRow = ''
for i in range(len(arOfText6)-1,-1,-1):
    reversedRow += arOfText6[i]+' '

print(reversedRow)