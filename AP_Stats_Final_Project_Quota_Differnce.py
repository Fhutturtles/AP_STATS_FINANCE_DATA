#Most of these calls to different repositories are overkill but since optimization isnt the name of the game then just leave em there - Brian
from cgi import print_form
from pickle import FALSE
from sre_parse import SPECIAL_CHARS
from tracemalloc import start
import json
from turtle import down
import requests
import sched, time 
import math
import numpy as np
import random
import seaborn as sns
import scipy.stats as stats
import tkinter #this controls graph dont touch
import pandas as pd
import matplotlib
import yfinance as yahooFinance
matplotlib.use("TkAgg") #this controls the graph Especially dont touch this BRIAN
import matplotlib.pyplot as plt#this controls graph dont touch
s = sched.scheduler(time.time, time.sleep)#this is the timer function that executes a market sweep every deffined times

#SP_current_percentage = 0
#NSDQ_percentage = 0
store_SP = []
store_NSDQ = []
store_random_SP = []
store_random_NSDQ = []
def Quote_indexs():
    try:
        print("Securities are being quoted")
        get_sp_info = yahooFinance.Ticker("^GSPC")
        print(get_sp_info.info)
        print("````````````````````````````````````````")
        print("````````````````````````````````````````")
        print("````````````````````````````````````````")
        get_sp_info = yahooFinance.Ticker("^IXIC")
        print(get_sp_info.info)
    except:
        print("Securities cannot be quoted please look at possible error sections")
def get_history():
        try:
          print("This is the Stock Data")
          #SNPH = yahooFinance.Ticker('^GSPC')
          #print(SNPH.history(start="2021-05-14", end="2022-05-14", interval="1d"))
          download_data = yahooFinance.download('^GSPC', start="2018-05-14", end="2022-05-13", group_by="ticker")
          #print(download_data)
          a = 0
          while (a < len(download_data)):
              sold =  download_data.Open[a]
              close = download_data.Close[a]
              percent = ((sold-close)/close)*100
              print("S&P 500 fund -- Array Location Index: "+ str(a) + " percent: "+str(percent))
              store_SP.append(percent)
              a += 1

           #Chelsie was here (╯ ͡• ₃ ͡•)╯┻━┻
          download_dataNSDQ = yahooFinance.download('^IXIC', start="2018-05-14", end="2022-05-13", group_by="ticker")
          a = 0
          while (a < len(download_dataNSDQ)):
              sold =  download_dataNSDQ.Open[a]
              close = download_dataNSDQ.Close[a]
              percent = ((close-sold)/sold)*100
              print("NASDAQ Composite fund -- Array Location Index: "+ str(a) + " percent: "+str(percent))
              store_NSDQ.append(percent)
              a += 1

          a = 0
          while( a < 201):
              rs = random.randint(0, len(store_SP)-1)
              store_random_SP.append(store_SP[rs])
              print(store_random_SP[a])
              a += 1
          print("THIS IS A BREAK IN THE LINES OF THE DATA ARRAYS ----------------------------------- THIS IS A BREAK IN THE LINES OF THE DATA ARRAYS")      
          a = 0
          while( a < 201):
              rq = random.randint(0, len(store_NSDQ)-1)
              store_random_NSDQ.append(store_NSDQ[rq])
              print(store_random_NSDQ[a])
              a += 1
          
        except:
            print("could not print out data")


#ok this section is essentially what makes a random interval of the data (it only grabs 200 and puts the data into a new array the array is what is output into google sheets)      
#Quote_indexs()
get_history()
#Good luck on the project - (Chelsie & Brian)