from tkinter import *
import random
import time
from urllib.request import urlopen
import sys
import feedparser

news = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml#')
othernews = feedparser.parse('http://feeds.bbci.co.uk/news/uk/rss.xml')

window = Tk()
window.configure(bg='white')
window.attributes("-fullscreen",True)
window.title("Random Fact")

delay = 60 #Update delay

frame= Frame(bg='white')
frame.place(in_=window, anchor="c", relx=.50, rely=.50)

newshead = Label(frame,text="Latest Technology News:",font=("Ariel",80),bg='white').grid(column=0,row=0,columnspan=2,sticky=N+E+W)


class newsRow:
    
    def __init__(self,window,startRow):
        headsize = 20
        dessize = 15
        self.hl = Label(frame,bg='white',font=("Ariel",headsize),wrap='900')
        self.hl.grid(row=startRow,column=0,sticky=W+E+N)
        self.hr = Label(frame,bg='white',font=("Ariel",headsize),wrap='900')
        self.hr.grid(row=startRow,column=1,sticky=W+E+N)

        self.dl = Label(frame,bg='white',font=("Ariel",dessize),wrap='900')
        self.dl.grid(row=startRow+1,column=0,sticky=W+E+N,padx=15,pady=15)
        self.dr = Label(frame,bg='white',font=("Ariel",dessize),wrap='900')
        self.dr.grid(row=startRow+1,column=1,sticky=W+E+N,padx=15,pady=15)

    def update(self,startNews):
        news = feedparser.parse('http://feeds.bbci.co.uk/news/technology/rss.xml#')
        self.hl.config(text=news['entries'][int(startNews)]['title'])
        self.hr.config(text=news['entries'][int(startNews)+1]['title'])
        self.dl.config(text=news['entries'][int(startNews)]['description'])
        self.dr.config(text=news['entries'][int(startNews)+1]['description'])

    
othernewstitle=Label(frame,text="In Other News:",font=("Ariel",50),bg='white').grid(column=0,row=7,columnspan=2,sticky=N+E+W)


class otherNews:
    def __init__(self,frame,startRow):
        headsize = 20
        dessize = 15

        self.ohl = Label(frame,bg='white',font=("Ariel",headsize),wrap='900')
        self.ohr = Label(frame,bg='white',font=("Ariel",headsize),wrap='900')
        self.odl = Label(frame,bg='white',font=("Ariel",dessize),wrap='900')
        self.odr  = Label(frame,bg='white',font=("Ariel",dessize),wrap='900')

        self.ohl.grid(row=startRow,column=0,sticky=W+E+N)
        self.ohr.grid(row=startRow,column=1,sticky=W+E+N)
        self.odl.grid(row=startRow+1,column=0,sticky=W+E+N)
        self.odr.grid(row=startRow+1,column=1,sticky=W+E+N)

    def update(self,startNews):
        othernews = feedparser.parse('http://feeds.bbci.co.uk/news/uk/rss.xml')
        self.ohl.config(text=othernews['entries'][int(startNews)]['title'])
        self.ohr.config(text=othernews['entries'][int(startNews)+1]['title'])
        self.odl.config(text=othernews['entries'][int(startNews)]['description'])
        self.odr.config(text=othernews['entries'][int(startNews)+1]['description'])

num=1


class facts:
    def __init__(self,frame,startRow):
        frame.grid_rowconfigure(startRow,pad=(40))
        self.t = Label(frame,bg='white',font=('Ariel',20))
        self.t.grid(row=startRow,column=0,columnspan=2)
        self.f=Label(frame, wrap='1500',bg='white',font=('Ariel',12))
        self.f.grid(row=startRow+1,column=0,columnspan=2,sticky=S)
    def newFact(self,frame):
        global num
        facts=[]
        with urlopen("http://www.jamietuplin.com/facts.txt") as factfile:
            for line in factfile:
                line = line.decode('latin1')
                line = line.strip('\n')
                facts.append(line)

                
        self.t.config(text='Random Fact (number '+str(num)+' since program start):')
        self.f.config(text=random.choice(facts))
        num+=1

class info:
    def __init__(self,startRow):
        frame.grid_rowconfigure(startRow,pad=(40))
        self.developer = Label(frame, text="Program developed by Jamie Tuplin")
        self.developer.grid(row=startRow)
        self.lastU = Label(frame)
        self.lastU.grid(row=startRow,column=1)
    def update(self):
        self.ctime = time.strftime("%D at %H:%M:%S")
        self.lastU.config(text="Information last updated on: "+self.ctime)

        
up = newsRow(frame,1)
up.update(0)
mid = newsRow(frame,3)
mid.update(2)
low = newsRow(frame,5)
low.update(4)
onews = otherNews(frame,8)
onews.update(0)
fact = facts(frame,10)
fact.newFact(frame)
info = info(12)
info.update()


print(num)

def update():
    up.update(0)
    mid.update(2)
    low.update(4)
    onews.update(0)
    fact.newFact(frame)
    info.update()
    
    window.after(delay*1000,update)
    

window.after(delay*1000,update)

window.mainloop()
