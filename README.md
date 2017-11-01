# moviePreference
## Introduction
In the website of [DOUBAN MOVIE](https://movie.douban.com), one can determin whether he/she prefers certain types of movies, according to the score given by him/her, the total score of the movie, and the type of the movie. 

## 介绍
在[豆瓣电影](https://movie.douban.com)中，根据用户看过电影的评分和该电影的总评分，以及该电影所属类型，判断用户是否存在对某类型电影的偏好或偏恶。

## 获取已看过电影
在[豆瓣](https://www.douban.com)的个人主页，可以获得用户ID。将其输入[douban.py](/douban.py/)中，运行，可以获得所有已看过电影的url、个人评分、总评分、和电影类型。这些信息均存入[movieInfo.txt](/movieInfo.txt/)中。

## 假设检验
运行[count.py](/count.py/)统计用户所看不同类型电影的数量，评分差的平均值和样本方差(注意分母是n-1)，进行单样本的双边t假设检验。原假设为用户没有偏好或偏恶，取置信概率为95%。当原假设不成立时，若评分差为正，则说明用户对该类型电影具有偏好，ans=1；若评分差为负，则说明用户对该类型电影具有偏恶，ans=-1；否则不能判断用户对该类型电影的态度，ans=0。