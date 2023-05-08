HELP 
https://codeforces.com/problemset/problem/71/A?locale=en

n = int(input())# Подскажжите как решить задачу, непонял задания  ?


w = 'word'
l = 'localization'
i = 'internationalization'
p = 'pneumonoultramicroscopicsilicovolcanoconiosis'

if n % 2==0 and len(w)<10:
    print('word')
if n % 2==0 and len(l)>10:
    l = 'l10n'
    print(l)
if n % 2 ==0 and len(i)>10:
    i = 'i18n'
    print(i)
if n % 2 == len(p)>10:
    i = 'p43s'
    print(i)
