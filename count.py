from scipy.stats import t

alpha = 0.05

movieList = []
with open('movieInfo.txt', 'r') as f:
	for line in f.readlines():
		movieList.append(line.strip())

dataDict = {}
for movieInfoStr in movieList:
	movieInfo = movieInfoStr.split('\t')
	myScore = movieInfo[1]
	movieScore = movieInfo[2]
	error = float(myScore)*2 - float(movieScore)
	for type in movieInfo[3:]:
		if type in dataDict:
			dataDict[type].append(error)
		else:
			dataDict[type] = [error]

typeDict = {}
for movieType in dataDict:
	data = dataDict[movieType]
	num = len(data)
	average = sum(data) / num
	if num == 1:
		s = 'inf'
	else:
		s = sum([(d-average)**2 for d in data]) / (num-1)
	typeDict[movieType] = [num, average, s]

ansDict = {}
for movieType in typeDict:
	sta = typeDict[movieType]
	if sta[2] == 'inf':
		ans = 0
	else:
		struct = sta[0]**0.5 * sta[1] / sta[2]
		if abs(struct) > - t.ppf(alpha/2, sta[0]-1):
			if struct > 0:
				ans = 1
			else:
				ans = -1
		else:
			ans = 0
	ansDict[movieType] = ans
print(ansDict)