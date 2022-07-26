import requests
from bs4 import BeautifulSoup

def parsing(file_name, html):
    #print(html)
    link=[]
    dict_links={}
    soup=BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    for tag in tags:
        secondary_file_names=tag.get('href', None)
        link.append(secondary_file_names)
        #print(secondary_file_names)

    #print(link)

    #dict_links[file_name]=link
    return (file_name, link)



#file_name_list=[con_3U_prod_desc.dita]
file_name='ref_3U_kc_summarychanges.html'
url='https://www.ibm.com/docs/en/STAKKZ/ts4300_kc/'+file_name
response=requests.get(url)
html=response.text

x=parsing(file_name, html)
#print(x)
(file, lst)=x
dict_file[file]=lst
