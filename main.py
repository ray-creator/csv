import os

from pypinyin import lazy_pinyin, pinyin
ls = []
for line in open("rawfile.txt"):
    if line[0:1].isdigit():  # 判断是否数字
        # 得到中文字符开始index
        start = (line.find("."))

        # 得到第一个字的英文
        ipinyin = ''
        zifunum=6 #取前几位中文首字母
        for iszm in range(zifunum): #取前几位中文首字母
            firstpy = lazy_pinyin(line[start + iszm+1])
            ipinyin= ipinyin+firstpy[0][0:1]
        print (ipinyin)

        # print(firstpy+line[start+1:])
        ls.append(ipinyin)  # 第一个拼音加入列表
        kk = len(ls)
        ls[kk - 1] = ls[kk - 1] + line
    else:
        kk = len(ls)
        # print(line)
        ls[kk - 1] = ls[kk - 1] + line

result = ls.sort()

for item in range(len(ls)):
    print(ls[item])
