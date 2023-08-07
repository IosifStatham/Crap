import requests
import re
from fake_headers import Headers
import bs4
import json

def list_tag (link1):
   headers = Headers(browser="firefox", os="win")
   headers_data = headers.generate()

   main_html = requests.get(link1, headers=headers_data).text
   main_soup = bs4.BeautifulSoup(main_html, "lxml")

   div_article_list_tag = main_soup.find_all('div', class_="vacancy-serp-item__layout")
   return div_article_list_tag

def city (list_tag1):
    articles_info =[]
    
    for article in list_tag1:
       tag_prof = article.find_all('a', class_="serp-item__title")
       
       for s in tag_prof:
        pattern = r"\w+"
        result = re.findall(pattern, s.text)
        
        for word in result:
         if word == 'Django' or word == 'Flask':
            tag_city =  article.find('div', class_="vacancy-serp-item__info")
            info_list =[]
            
            for q in tag_city:
               info = q.text
               info1 = info.split( )
               info_list.append(info1)
               
            sallary1 = article.find('span', class_= 'bloko-header-section-2')
            sallary = sallary1.text
            sallary2 = sallary.split( )
            sallary_f = ' '.join(sallary2)
            
            link1 = article.find('a', class_= 'serp-item__title')
            link = link1['href']
            
            articles_info.append(
        {
            "info": info_list,
            "link": link,
            "sallary": sallary_f,
        }
    )
    return articles_info        

               
def w_in_json (list):              
   with open ("DATA\data.json", "w", encoding='utf-8') as f:
       json.dump(list, f, ensure_ascii=False)             
   return "Запись успешно проведена"           
   
   
if __name__ == '__main__':
   link= "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
   
   print(w_in_json(city(list_tag(link))))
