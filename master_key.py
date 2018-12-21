from bs4 import BeautifulSoup as bs
import requests


def master_key_info(cd):
    url="http://www.master-key.co.kr/booking/booking_list_new"
    response=requests.post(url, { "date" : "2018-12-22", "store" : cd, "room" : "" }).text
    document = bs(response, "html.parser")
    ul = document.select(".reserve .escape_view")
    theme_list = []
    for li in ul:
        title = li.select('p')[0].text
        info=''
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        theme = {
            "title" : title,
            "info" : info
        }
        theme_list.append(theme)
        
    return theme_list

def master_key_list():
    url="http://www.master-key.co.kr/home/office"
    response=requests.get(url).text
    
    document=bs(response, "html.parser")
    lis=document.select(".escape_list .escape_view")
    
    cafe_list=[]
    for li in lis:
        cafe={
            'title' : li.select_one('p').text.replace('NEW',''), #python how to eliminate substring from string
            'tel' : li.select('dd')[1].text,
            'address' : li.select('dd')[0].text,
            'link' : "http://www.master-key.co.kr"+li.select_one('a')['href'] # 크롤링한 태그에서 속성값 가져오기
        }
        cafe_list.append(cafe)
        
    return cafe_list


