a = 10
b = 5

b = a+b
a = a+b
b = a-b
a = a-b-b

print a, b

str1 = 'first'
str2 = 'second'

str2 = str1+str2
str1 = str2[len(str1):]
str2 = str2[:len(str2)-len(str1)]
print str1,str2