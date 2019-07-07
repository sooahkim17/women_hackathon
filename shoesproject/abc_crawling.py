from bs4 import BeautifulSoup
import requests 

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoesproject.settings")

import django
django.setup()

from shoes.models import Shoes

def abc_crawling():
    req=requests.get('http://www.abcmart.co.kr/abc/search/smartSearch?smartSearchYN=Y&kind=shoes&searchTerm=&brandName=&largeCategory=%EC%9A%B4%EB%8F%99%ED%99%94%5E%EC%8A%A4%ED%8F%AC%EC%B8%A0.%EB%A0%88%EC%A0%80&middleCategory=%EC%BB%A8%EB%B2%84%EC%8A%A4%ED%99%94%5E%EC%8A%AC%EB%A6%BD%EC%98%A8%5E%EC%8A%A4%EB%8B%88%EC%BB%A4%EC%A6%88%5E%EB%9F%B0%EB%8B%9D%ED%99%94%5E%EB%93%B1%EC%82%B0%ED%99%94%5E%EC%95%84%EC%BF%A0%EC%95%84%EC%8A%88%EC%A6%88%5E%EA%B3%A8%ED%94%84%ED%99%94&thema=&minPrice=&maxPrice=&size=&minSize=100&maxSize=320&detailColor=&sort=ENTRY_DT&listSize=40&page=10&viewType=01&imgColor=&initMinPrice=&initMaxPrice=&isReSearech=true')
    html=req.text
    bs=BeautifulSoup(html,'html.parser')
    shoes_list=bs.findAll('ul',attrs={'class':'gallery_basic gallery_box_type1 w150'})
    #print(len(shoes_list))
    size_list=[]
    shoes_info=[]
    data={}
    for i in range(len(shoes_list)):
        shoes=shoes_list[i].findAll('a',attrs={'class':'model_box'})
        for j in range(len(shoes)):         
            shoes_detail="http://www.abcmart.co.kr"+shoes[j].attrs['href']
            req=requests.get(shoes_detail)
            html=req.text
            bs=BeautifulSoup(html,'html.parser')

            shoes_title=bs.find('h2',attrs={'class':'tit_type1'})
            #print(shoes_title.text)

            shoes_codes=bs.find('ul',attrs={'class':'tit_type3'}).findAll('li')
            shoes_code_li=shoes_codes[1]
            shoes_code=str(shoes_code_li)[11:18]
            
            #print(shoes_code)

            shoes_image=bs.find('div',attrs={'class':'img_area'}).find('img').attrs['src']
            #print(shoes_image)

            shoes_size=bs.findAll('li',attrs={'class':'disable add_restock'})
            for i in range(len(shoes_size)):
                size=shoes_size[i].text[71:74]
                size_list.append(size)
            
            title='ABCmart-'+shoes_title.text
            shoes_info.append(title)
            shoes_info.append(shoes_image)
            shoes_info.append(size_list)
            data[shoes_code]=shoes_info
            size_list=[]
            shoes_info=[]
                
    return data   

if __name__=='__main__':
    shoes_data_dict = abc_crawling()
    for t, l in shoes_data_dict.items():
        Shoes(shoes_title=l[0], shoes_image=l[1],shoes_body=l[2]).save()
           
            