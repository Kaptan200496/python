import re
#1
userStr = "Зв'яжіться з нами: +380961112233 або за резервним 0961112233. Старий номер 380931234567 також працює."
match = re.findall(r'(?:\+380|380|0)[0-9]{9}', userStr)
print(match)
#2
userStr2 = "test.user@gmail.com , invalid..mail@site , user_23@ukr.net , .start@fail.com, admin@site., test@localhost, valid-email@company.org."
match2 = re.findall(r"[a-zA-Z0-9]+[-|.|_]{1}[a-zA-Z0-9]+@(?:gmail.com|ukr.net){1}", userStr2)
print(match2)
