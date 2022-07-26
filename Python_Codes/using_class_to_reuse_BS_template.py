from bs4 import BeautifulSoup

class Bs():

    def __int__(self):
        self.soup=None

    def parse(self, path):
        self.path=path


        fh=open(self.path, 'r')
        data=fh.read()
        soup=BeautifulSoup(data, 'lxml-xml')
        self.soup=soup
        return soup

class xyz():
    def Tag(self, tag_name, soup):
        self.soup=soup

        tags_lst=self.soup(tag_name)
        print(tags_lst)



    #def tagging(self):


class Strt():
    abc = Bs()
    def1 = xyz()

    soup1=abc.parse('C:/Users/manis/Downloads/3U_kc.ditamap')
    cool=def1.Tag('topicref', soup1)



a=Strt()
a.cool









#abc.Tag('topicref')






