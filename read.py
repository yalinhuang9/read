data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

comment = []
with open('reviews.txt', 'r') as f:
	for line in f:
		comment.append(line)
sum_len = 0
for c in comment:
	sum_len = sum_len + len(c)

print('每筆留言的平均長度為', sum_len / len(data))


new = []
for c in comment:
	if len(c) < 100:
		new.append(c)
print('共有', len(new), '筆留言長度小於100')
print(new[0])
print('_____')
print(new[1])
print('_____')
print(new[2])
	
