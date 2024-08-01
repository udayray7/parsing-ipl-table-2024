from requests_html import HTMLSession
import json
session = HTMLSession()

r = session.get('https://livemint.com/sports/cricket-news/ipl-points-table')

table1 = r.html.find('table')[0]
table2 = r.html.find('table')[1]
tabledata1 = [[c.text for c in row.find('td')] for row in table1.find('tr')[1:]]
print(tabledata1)
tableheader1 = [[c.text for c in row.find('th')] for row in table1.find('tr')][0]
tableheader2 = [[c.text for c in row.find('th')] for row in table2.find('tr')][0]
tabledata2 = [[d.text for d in row.find('td')] for row in table2.find('tr')[1:]]
# print(len(tabledata2))
# print(len(tableheader2))
print('----------------------------------------------')
print(tableheader1)
print('----------------------------------------------')
print(tabledata2)
print('---------------------------------------------------------')
print(tableheader2)
print('---------------------------------------------------------')
#res1 = [dict(zip(tableheader1, t1) for t1 in tabledata1)]
l1=[]
for t1 in tabledata1:
    res1 = dict(zip(tableheader1, t1))
    l1.append(res1)
print(l1)
print('---------------------------------------------------------')
#res2 = dict(zip(tableheader2,t2) for t2 in tabledata2)
l2=[]
for t2 in tabledata2:
    res2 = dict(zip(tableheader2, t2))
    l2.append(res2)
print(l2)
print('--------------------------------------------------')
mainheader = tableheader1 + tableheader2
print(mainheader)
print('------------------------------------------------------')

combined_list = [tabledata1 + tabledata2 for tabledata1, tabledata2 in zip(tabledata1, tabledata2)]
maindata=[]
for i in combined_list:
    maindata.append(i)
print(maindata)
print('======================================================================')

finaldata=[]
for md in maindata:
    res3 = dict(zip(mainheader, md))
    finaldata.append(res3)
print(finaldata)

with open('ipltable.json','w') as f:
    json.dump(finaldata,f)