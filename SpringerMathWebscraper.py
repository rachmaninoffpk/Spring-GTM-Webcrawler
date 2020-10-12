from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

def getLinks(urlGiven):
    bookList = []
    page = requests.get(urlGiven)
    bsObj = BeautifulSoup(page.content,'html.parser')
    rows = bsObj.findAll(class_='listItemBooks')

    for row in rows:
        price = row.find(class_='priceNew').text 
        floatBox = row.find(class_= 'floatBox')
        title = floatBox.find('h2').text
        authorTemp = row.findAll(class_='displayBlock')
        if len(authorTemp) == 2:
            title = title + ': ' + authorTemp[0].text 
            author = authorTemp[1].text 
        else:
            author = authorTemp[0].text
        year = int(row.find(class_='displayblock renditionDescription').text[:4])
        volumeList = floatBox.findAll('p')
        for item in volumeList:
            if 'Vol' in item.text:
                volume = item.text 
                break
        volume = int(volume[volume.index('Vol')+5:])
        tempDict = {'title':title,
        'author': author,
        'year': year,
        'volume': volume,
        'price':price[:-2]}
        bookList.append(tempDict)


    return bookList

def main(n):
    bookList = []
    i = 0
    while(i <= n):
        url = 'https://www.springer.com/new+&+forthcoming+titles+%28default%29?SGWID=5-40356-404-653425-136&originalID=173621337&sortOrder=pubdateSortdesc&searchType=BYSERIES&searchScope=editions&resultStart=' + str(i) + '1'
        temp = getLinks(url)
        if len(temp) == 0:
            break
        bookList.extend(temp)
        i += 1
    return bookList
