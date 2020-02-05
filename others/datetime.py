from datetime import datetime

datetime_1 = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
datetime_2 = datetime.strptime('[2020/01/29 00:03:09,669]', '[%Y/%m/%d %H:%M:%S,%f]')