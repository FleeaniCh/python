"""
    匹配除换行之外单个字符  .
"""
import re
s = """
2006年，因获得《雅虎搜星》比赛冯小刚组冠军而进入演艺圈 [2]  ；
同年，在冯小刚执导的广告片《跪族篇》中担任女主角 [3]  。2011年，
因在古装剧《新还珠格格》中饰演晴儿一角而被观众认识 [4]  。2013年，
凭借古装剧《陆贞传奇》获得更多关注。2014年10月，在第10届金鹰
电视艺术节举办的投票活动中被选为“金鹰女神” [5]  ；12月，凭借都市爱
情剧《杉杉来了》获得第5届国剧盛典内地最具人气女演员奖；同年，成立
海润传媒赵丽颖工作室,冯大刚。
"""
print(re.findall('冯.刚',s))