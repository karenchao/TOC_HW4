# -*- coding: utf-8 -*-
####學號:F74002052, 姓名:趙珮雯
####將最多筆成交量的路段印出來，印出最大成交價和最小成交價
####(若成交時間同年同月算一筆)
####給一個參數 : 網址

import urllib
import json
import sys      #for argc, argv
import re       #for regular espression

if len(sys.argv) < 2:
  print "error"
  sys.exit(0)

#url = 'http://www.datagarage.io/api/538447a07122e8a77dfe2d86'
url = sys.argv[1]
page = urllib.urlopen(url).read()
#print page
data = json.loads(page)

list = dict()		#list{"XX路" : [10301, 10302], "OO街" : [10201]}
max_money = dict()
min_money = dict()

for item in data :
	old_road = item[u'土地區段位置或建物區門牌']
	#若符合 '路' or '街' or '巷' or '大道' 就是要處理的資料
	if re.search(ur"路", old_road) or re.search(ur"街", old_road) or re.search(ur"巷", old_road) or re.search(ur"大道", old_road):
		if re.search(ur"路", old_road):
			road = old_road.split(u'路')[0]
			road = road + u'路'
		elif re.search(ur"街", old_road):
			road = old_road.split(u'街')[0]
			road = road + u'街'
		elif re.search(ur"大道", old_road):
			road = old_road.split(u'大道')[0]
			road = road + u'大道'
		elif re.search(ur"巷", old_road):
			road = old_road.split(u'巷')[0]
			road = road + u'巷'
			
		if list.has_key(road) == False: #if dict 裡沒有這個key
			list[road] = []
		if list[road].count(item[u'交易年月']) == 0: #增加近list裡
			list[road].append(item[u'交易年月'])
		
		money = item[u'總價元']
		if max_money.has_key(road) == False: #if dict 裡沒有這個key
			max_money[road] = money
		if min_money.has_key(road) == False: #if dict 裡沒有這個key
			min_money[road] = money
		#更新max_money and min_money
		if max_money[road] < money:
			max_money[road] = money
		if min_money[road] > money:
			min_money[road] = money

#find max_count
max_count = 0
for item in list:
	count = len(list[item])
	#print item
	if max_count < count:
		max_count = count

ans = ""
for key in list.keys():
	if len(list[key]) == max_count:
		ans += u"{}, 最高成交價: {}, 最低成交價: {}\n".format(key, max_money[key], min_money[key])
		#print u"{}, 最高成交價: {}, 最低成交價: {}".format(key, max_money[key], min_money[key])

print ans
			
			