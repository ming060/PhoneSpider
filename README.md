# PhoneSpider
## Why
The website [DeviceSpecifications](https://www.devicespecifications.com/en) is a very useful tool when you want to check phone specs. You can input model name to search the phone spec with its search box.


For example, I want to seach Samsung Galaxy A5 (2017). I know the model alias is A520, so I cant find it by the alias name.


![](resources/specs_success.gif)


But, sometimes it doesn't work!!! If I just know the alias name is 520 (Sometimes they just don't put the whole name on the back of the phone), then I would fail to search the correct phone.


![](resources/specs_fail.gif)


I'm not sure how the website implement the search function. But in this case, I have to enter the model name or model alias from the beginning to make the searching success.


## How
The simplest way come to my mind is to crawl all phone model name and their alias name, then use our own way to search. 


Then I chose Scrapy to crawl the website and store the specs in a json file.


The next step is to implement the search function. The fisrt idea of course is to put those data into a database. But in that case, I still need a lot of work to build maybe a GUI or something to access those data.


So I decided to use more easy way to handle this, just put them into a excel file. Even though I still want to put those data into database (maybe play mysql with python or put them online with firebase) and build a GUI (a website or app).


## What


