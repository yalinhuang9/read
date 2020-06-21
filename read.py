# 讀取檔案
data = []
with open('food.rtf', 'r') as f:
	for line in f:#一行一行讀取f
		data.append(line.strip())#把換行符號與多於空格去掉
print(data)