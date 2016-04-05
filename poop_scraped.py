'''
another try at using Beautiful soup to get data
from the sf311 system on poop


'''
from bs4 import BeautifulSoup
import urllib2
import re
import string


url_base = 'http://mobile311.sfgov.org/'
url_ext = '?external=false&service_id=518d5892601827e3880000c5' # street and sidewalk cleaning
url= 'http://mobile311.sfgov.org/?external=true&service_id=55e8409a45ff461f92000006&status=open'
url= url_base+url_ext+'&status=open'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'lxml')


#print soup.table.tbody.tr

print ("------------")
#print soup.table.tbody.tr.span

#reports = soup.table('span',class_="activity-timestamp")

reports = soup.table('span',"activity-timestamp")
#reports = soup.table.find('span',"activity-timestamp").get_text()

for line in reports:
        line=str(line)
        x=line.find("#")+1
        y=x+7
        z=line[x:y]
        print z
        url_goal = url_base+"reports/"+z
        print url_goal
        page2 = urllib2.urlopen(url_goal)
        real_soup = BeautifulSoup(page2.read())
        blockquote = real_soup('blockquote')
        for line in blockquote:
                request_type = line.find_next_sibling('p')

                print request_type
