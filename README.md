# sendIT
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

[![Build Status](https://travis-ci.org/kyakusahmed/sendIT.svg?branch=apv1)](https://travis-ci.org/kyakusahmed/sendIT)
[![Coverage Status](https://coveralls.io/repos/github/kyakusahmed/sendIT/badge.svg)](https://coveralls.io/github/kyakusahmed/sendIT)

[gh-pages](https://kyakusahmed.github.io/sendIT/UI/)
### How to run the app


Make sure that python 3.4/3.5/3.6/3.7 is installed on your computer

Clone the repo
```
git clone https://github.com/kyakusahmed/fast-foods.git
```
Change to the app directory
```
$ cd sendIT
```
Create a virtual enviroment
```
virtualenv (name)
```
Activate the virtualenv
```
For Windows:
	$ (virtualenv name)\scripts\activate, and  	
For Linux: 
 	$source(virtualenv name)/bin/activate
```
Install the required modules from the requirements.txt file 
```
$ pip install -r requirements.txt
```
Run the app
```
$ python run.py
```

### Heroku link


| tasks               |    URLS                |  METHOD  |         PARAMS              | 
| ------------------- | -----------------------|----------|-----------------------------|
| get all orders      | api/v1/orders          |  GET     |   ---------------           |
| get aspecific order | api/v1/orders/id       |  GET     |   ---------------           |
| post an order       | api/v1/orders          |  POST    | foodid, userid, date, status| 
| update the status   | api/v1/orders/id       |  PUT     | status                      |
|                     |                        |          |                             |
	
### How to run the Tests:

 open the terminal,activate virtual enviroment in the sendIT directory  and enter:
 ```
 $ pytest
```
 using nosetest  in open the terminal,activate virtual enviroment in the sendIT directory and enter:
 ```
 $ nosetests --with-coverage --cover-tests
 ```
 

