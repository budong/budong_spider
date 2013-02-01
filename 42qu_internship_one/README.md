说明：
一：这是抓取 http://huati.weibo.com/ 页面，全国热点24小时内的所有话题的爬虫。
二：用谷歌浏览器打开网页右键审查元素发现，对应的区域使用了ajax，对应的数据使用Json传输。
三：进一步分析 获取 json数据的项为big，对应的url为 
http://huati.weibo.com/aj_topiclist/big?ctg1=99&ctg2=0&prov=0&sort=time&p=1
，其中最后面的p代表翻页，因此可以取到所有的话题。

关于本程序：
一：请求使用的是requests这个库，pip install requests。
二：解析response使用的是BeautifulSoup这个库，pip install BeautifulSoup。
三：如果请求的状态码不等于200，则最大重试3次。

