## example code for retrieve an HTML table and write it as a csv file
import csv
from urllib.request import urlopen 
from bs4 import BeautifulSoup
# load a wiki page that has a complicated tabel
html=urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup=BeautifulSoup(html,features='lxml')
#get the table
table=soup.find_all('table',{'class':'wikitable sortable'})[0]
#print(table)
#get all the rows
rows=table.find_all('tr')
#print(rows)
#test get first row of table
#first_row=table.find_all('tr')[0]
#print(first_row)
#test get first cell of the first row
#first_row_first_cell=first_row.find_all(['td','th'])[0]
#print(first_row_first_cell)
#get the text of first_row_first_cell
#first_row_first_cell.get_text()
#strip the /n
#first_row_first_cell.get_text().rstrip('\n')

# open a csvfile,make sure to specify newline=''

with open('scrape_table.csv','wt',newline='') as csvfile:
    #create a writer object
    writer=csv.writer(csvfile)
    try:
        for row in rows:
            #for each row of table,create an empty row call csvrow
            csvrow=[]
            #for each cell within each row (either head cell or standard cell)
            for cell in row.find_all(['td','th']):
                #get the cell text, and strip the \n behind it,then append them 
                #into one row untill all cell texts are exhausted
                csvrow.append(cell.get_text().rstrip('\n'))
            #when each row is done,append a row at the bottom of the csv file
            writer.writerow(csvrow)
    finally:
        #close the file when done
        csvfile.close()