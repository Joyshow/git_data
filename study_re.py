import re
b='<a dataid="DvfMl5JPzMhexx1dndzBRIOLTQ7Aj0fLHAfZWceMxw5QAgnHiFECBY%3D" onclick="noIn(this)" target="_blank">招标公告：建筑装饰—2021年度集采—办公家具（\
长春区域）采购招标</a>'
b=str(b)

a='xxIxxjshdx3x6lovexxsffaxxpythonxx'
infos = re.findall('xx(.*?)xx',a)
info1 = re.search('1d(.*)OL',b)
#search查找匹配第一个
info2=re.search('\d+',a)
print(info2)
info2=info2.group()
print(info2)
#findall查找匹配所有
info3 = re.findall('\d+',a)
print(info3)

#用于替换
phone = '123-4567-1234'
new_phone = re.sub('\D','',phone)
print(new_phone)