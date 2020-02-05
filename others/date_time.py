from datetime import datetime

d1 = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
d2 = datetime.strptime('[2020/01/29 00:03:09,669]', '[%Y/%m/%d %H:%M:%S,%f]')

print(d1.strftime("%Y-%m-%d %H:%M:%S.%f"))
print(d2.strftime("%Y-%m-%d %H:%M:%S.%f"))
