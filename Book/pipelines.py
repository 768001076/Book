# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):

    file = object
    num = 1

    def __init__(self):
        print("打开文件")
        self.file = open("F:\\Book\\无敌剑域.txt","a+",encoding="utf-8")

    def process_item(self, item, spider):
        title = '第' + self.getNum(str(self.num)) + '章  ' + item["title"]
        contents = item["content"]
        self.file.write(title + '\n\n')
        print(title)
        for content in contents:
            self.file.write(content.strip()+"\n")
        self.file.write("\n\n-------------------\n\n\n")
        self.num+=1
        return item

    def getNum(self,digital):
        unit = ['', '十', '百', '千', '万']
        val = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        result = ""
        x = len(digital)
        for i in range(x):
            x -= 1
            v = int(digital[i])
            if v == 0:
                if x == 0 or i == 0:
                    continue
                else:
                    result += val[v]
            else:
                result += val[v] + unit[x]
        return result
