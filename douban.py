import requests
from bs4 import BeautifulSoup
import json

usrID = ''

def crawl(url):
	session = requests.Session()
	req = session.get(url, timeout=60)
	bsObj = BeautifulSoup(req.content, 'html5lib')
	return bsObj

def getMovieInfo(movieUrl):
	bsObj = crawl(movieUrl)
	try:
		movieScore = bsObj.find('div', {'class': 'rating_self clearfix'}). \
				find('strong').get_text()
		movieTypesBs = bsObj.findAll('span', {'property': 'v:genre'})
		movieTypes = [movieType.get_text() for movieType in movieTypesBs]
	except:
		movieID = movieUrl.split('/')[-2]
		apiUrl = 'https://api.douban.com/v2/movie/' + movieID
		apiBsObj = crawl(apiUrl)
		jsonObj = json.loads(apiBsObj.get_text())
		movieScore = jsonObj.get('rating').get('average')
		movieTypes = jsonObj.get('attrs').get('movie_type')
	return movieScore, movieTypes

movieList = []
num = 0

try:
	while True:
		url = 'https://movie.douban.com/people/'+usrID+'/collect?start=%d'%num
		bsObj = crawl(url)
		movies = bsObj.find('div', {'class': 'grid-view'}). \
			findAll('div', {'class': 'item'})
		if len(movies) == 0:
			break
		else:
			for movie in movies:
				movieUrl = movie.find('a')['href']
				myScore = movie.find('li', {'class': 'intro'}). \
					next_sibling.next_sibling.span['class'][0][6]
				movieScore, movieTypes = getMovieInfo(movieUrl)
				movieInfoStr = movieUrl + '\t' + myScore + '\t' + movieScore \
					+ '\t' + '\t'.join(movieTypes)
				print(movieInfoStr)
				movieList.append(movieInfoStr)
			num += 15
except Exception as e:
	print(e)
finally:
	print('共获取%d条电影信息' % len(movieList))
	with open('movieInfo.txt', 'w') as f:
		for movieInfo in movieList:
			f.write(movieInfo + '\n')