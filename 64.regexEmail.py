import re

str1 = 'woshilisheng@gmail.com, 770-595-0465, 125 cornerstone pl, 549143834@qq.net, tianyaxiaoqiangshou123@hao123.com.cn'
emailRegex = re.compile(r'''([A-Za-z0-9\.]+@[A-Za-z0-9]+\.[a-zA-Z]+(\.[a-zA-Z]+)?)''')
mo = emailRegex.findall(str1)

print [email[0] for email in mo]