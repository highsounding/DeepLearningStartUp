import re
from collections import Counter

def countPhrase(file_name, number):
	with open(file_name,'r',encoding="UTF-8") as f:
		total_string = f.read()
	#将整篇文章拆分为句子
	total_list = re.split("，|。|？|！|；|：|、|“|”|’|‘|―|\n|\u3000",total_string)

	phrase_list = []
	#分别将每个非空且至少含有两个词的句子拆分为词
	for l in total_list:
		if len(l) >= 1:
			word_list = l.strip().split()
			length = len(word_list)
			#将每个句子中的相邻词组合为词组，并判断是否为二元词组，是的话加入列表
			for i in range(length-1):
				if((len(word_list[i]) == 2) and (len(word_list[i+1]) == 2)):
					phrase_list.append(word_list[i] + word_list[i+1])

	#对词组列表进行计数，选出词频最高的前若干位
	result = Counter(phrase_list).most_common(number)

	print("文章中二元词组出现频率最高的前%d位如下：\n" % number)
	for n in result:
		print("%-10s\t%d" % (n[0], n[1]))


if __name__ == '__main__':
	countPhrase(r"E:\Workspace\happiness_seg.txt", 10)