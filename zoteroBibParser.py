import bibtexparser
import string
from urllib import parse

#Open the bib file and parse using bibtextparser library
with open('Bibs2018.bib') as bibtexFile:
    bibString=bibtexFile.read()
bibDB = bibtexparser.loads(bibString)

#create a standard python dictionary from bibtexparser object
bibEntries=bibDB.entries
titles={}


#clean up the entries so there are not weird {,},\'s in them
for x in bibEntries:
    for y in x.keys():
        x[y]=parse.unquote(x[y]).replace('{','').replace('}','').replace('\\','').replace('’','\'').replace('-','–').replace('&#039;','\'').strip().lower()

#pull out the titles and count how often they occur
for x in bibEntries:
    #Check to see if we have seen the title yet and if we have add 1 to the count
    if x['title'] in titles.keys():
        titles[x['title']]+=1
    #Title's first appearance so add the title to the dictionary with a count of 1
    else:
        titles[x['title']]=1

#create a list of all the counts in descending order
tValuesSort=sorted(list(set(titles.values())), reverse=True)

sortedTitles=[]
#iterate through all of the counts starting with the highest
for y in tValuesSort:
    #Append the titles to sortedTitles list if they have a count equal to the current one we are iterating through
    for x in titles:
        if titles[x] == y:
            sortedTitles.append(x)

journals={}
#pull out the titles and count how often they occur
for x in bibEntries:
    #Check to see if we have seen the title yet and if we have add 1 to the count
    if 'journal' in x.keys():
        if x['journal'] in journals.keys():
            titleList=journals[x['journal']]['titles']
            titleList.append(x['title'])
            journals[x['journal']]['titles']=titleList

        # Title's first appearance so add the title to the dictionary with a count of 1
        else:
            journals[x['journal']] = {}
            if x['title']==None:
                journals[x['journal']]['titles'] = ['']
            else:
                journals[x['journal']]['titles']=[x['title']]

for x in journals:
    for y in journals[x]['titles']:
        if y in journals[x].keys():
            journals[x][y] += 1
        # Title's first appearance so add the title to the dictionary with a count of 1
        else:
            journals[x][y] = 1

journalsOnly={}
for x in journals:
    journalsOnly[x]=0
    for y in journals[x].keys():
        if y!='titles':
            journalsOnly[x]+=journals[x][y]





#create a list of all the counts in descending order
jValuesSort=sorted(list(set(journalsOnly.values())), reverse=True)

sortedJournals=[]
#iterate through all of the counts starting with the highest
for y in jValuesSort:
    #Append the titles to sortedTitles list if they have a count equal to the current one we are iterating through
    for x in journalsOnly:
        if journalsOnly[x] == y:
            sortedJournals.append(x)

authors={}
#pull out the titles and count how often they occur
for x in bibEntries:
    #Check to see if we have seen the title yet and if we have add 1 to the count
    if 'author' in x.keys():
        authorList=x['author'].split('and')
        d=0
        while d<len(authorList):
            authorList[d]=authorList[d].strip()
            d+=1
        for y in authorList:
            if y in authors.keys():
                titleList = authors[y]['titles']
                titleList.append(x['title'])
                authors[y]['titles'] = titleList

            # Title's first appearance so add the title to the dictionary with a count of 1
            else:
                authors[y] = {}
                if x['title'] == None:
                    authors[y]['titles'] = ['']
                else:
                    authors[y]['titles'] = [x['title']]



for x in authors:
    for y in authors[x]['titles']:
        j=0
        for z in authors[x].keys():
            if y==z:
                authors[x][z] += 1
                j=1
                break
        # Title's first appearance so add the title to the dictionary with a count of 1
        if j==0:
            authors[x][y] = 1

authorCount={}

for x in authors:
    count=0
    for y in authors[x]:
        if y!='titles':
            count=count+authors[x][y]
    authorCount[x]=count


# create a list of all the counts in descending order
aCValuesSort = sorted(list(set(authorCount.values())), reverse=True)

sortedAuthorsCount = []
# iterate through all of the counts starting with the highest
for y in aCValuesSort:
    # Append the titles to sortedTitles list if they have a count equal to the current one we are iterating through
    for x in authorCount:
        if authorCount[x] == y:
            sortedAuthorsCount.append(x)

# for x in authors:
#     print(x,end=': ')
#     for y in authors[x]:
#         if y!='titles':
#             print(y,end='-')
#             print(authors[x][y])

# for x in sortedAuthorsCount:
#     print(x, end=': ')
#     print(authorCount[x])
#     print('  Number of titles written by author in bibliography: ',end='')
#     print(len(authors[x].keys())-1)
#     print('     Titles: ')
#     for y in authors[x].keys():
#         if y!='titles':
#             print('         ',end='')
#             print(y, end=': ')
#             print(authors[x][y])

# for x in sortedTitles:
#     print(x, end=': ')
#     print(titles[x])

for x in sortedJournals:
    print(x,end=': ')
    print(journalsOnly[x])
    print('  Number of titles from in bibliography: ',end='')
    print(len(journals[x].keys())-1)
    print('     Titles: ')
    for y in journals[x].keys():
        if y!='titles':
            print('         ',end='')
            print(y, end=': ')
            print(journals[x][y])

# # print('Illusionary Order: Online Databases, Optical Character Recognition, and Canadian History, 1997–2010'=='Illusionary Order: Online Databases, Optical Character Recognition, and Canadian History, 1997-2010')
# x='Illusionary Order: Online Databases, Optical Character Recognition, and Canadian History, 1997–2010'
# y='Illusionary Order: Online Databases, Optical Character Recognition, and Canadian History, 1997-2010'
# z=0
# while z<len(x):
#     if x[z]!=y[z]:
#         print(x[z])
#         print(y[z])
#     z+=1
