from bs4 import BeautifulSoup
import requests 

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoesproject.settings")

import django
django.setup()

from shoes.models import Shoes




def lesmore_crawling():
    req=requests.get('https://www.lesmore.com/ASP/Product/ProductList.asp?SCode1=09')
    html=req.text
    bs=BeautifulSoup(html,'html.parser')
    shoes=bs.find('div',attrs={'class':'row-list'}).findAll('li')
    size_list=[]
    shoes_info=[]
    data={}
    for i in range(len(shoes)):
        shoes_title=shoes[i].find('p',attrs={'class':'t1'})
        shoes_image="http://www.lesmore.com"+shoes[i].find('div',attrs={'class':'img'}).find('img').attrs['src']
        
        shoes_detail=shoes[i].find('div',attrs={'class':'img'}).find('img').attrs['src'][27:33]
        
        detail_url='https://www.lesmore.com/ASP/Product/ProductDetail.asp?ProductCode='+shoes_detail
        
        req=requests.get(detail_url)
        html=req.text
        bs=BeautifulSoup(html,'html.parser')
        
        shoes_bodys=bs.find('div',attrs={'class':'selection'}).findAll('li',attrs={'class':'none'})
        
        for size in shoes_bodys:
            size_list.append(size.text)
        
        #print(shoes_title.text,shoes_image,size_list)
        title='lesmore-'+shoes_title.text
        shoes_info.append(title)
        shoes_info.append(shoes_image)
        shoes_info.append(size_list)
        data[shoes_detail]=shoes_info
        size_list=[]
        shoes_info=[]
        

    return data
    
        
if __name__=='__main__':
    shoes_data_dict = lesmore_crawling()
    for t, l in shoes_data_dict.items():
        Shoes(shoes_title=l[0], shoes_image=l[1],shoes_body=l[2]).save()