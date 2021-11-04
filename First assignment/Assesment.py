import sys
import time
import os
import random
import datetime
from datetime import datetime

now = datetime.now()
date_time_now = datetime.now().time()

int_date_time_now = int(date_time_now.strftime("%Y%m%d%H%M%S"))

print(date_time_now)

print(int_date_time_now)

while True:
    print ("______________________________________________________")
    print ("""
    Which code should run ? 
    Code: 1 runs a seed based on the time 
    Code: 2 runs a user given seed
    Code: 3 runs a text file seed
    Option 4 will exit the programm

______________________________________________________
    """)
    ans=input("Which code should run ? ")
    print ("______________________________________________________") 
    if ans=="1":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        date_time_now = datetime.now().time()
        int_date_time_now = int(date_time_now.strftime("%H%M%S%f"))
        number_string = str(int_date_time_now)
        number_map = map(int,number_string)
        number_list = list(number_map)
        inp_list = number_list
        seed = sum(number_list)
        seed = seed
        a = 2   
        c = 1
        m = 2**2
        x1 = ((float)(a) * (float)(seed) + (float)(c))
        x1 = (x1 %m)
        print (seed)
        calc = x1 * int_date_time_now
        print (calc)

                       
    elif ans=="2":
        seed = input("Please provide a seed:     ")
        a = 22695477
        c = 1
        m = 2**32
        x1 = ((float)(a) * (float)(seed) + (float)(c))
        x1 = (x1 %m)
        print(x1)
        
    elif ans=="3":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        date_time_now = datetime.now().time()
        int_date_time_now = int(date_time_now.strftime("%H%M%S%f"))
        number_string = str(int_date_time_now)
        number_map = map(int,number_string)
        number_list = list(number_map)
        inp_list = number_list
        file = open("data.txt")
        line = file.read().replace("\n", " ")
        file.close()
        seed = 0
        seed = (str)(line)
        a = 22
        c = 1
        m = 2**2
        x1 = (a) * float(seed) + (c)
        x1 = (x1 %m)
        calc = x1 * int_date_time_now
        print (calc)

        
    elif ans=="4":
        time.sleep(3)
        print("Goodbye")
        print ("______________________________________________________")
        sys.exit()
    elif ans !="":
      print("Not Valid Choice Try again")
      print ("______________________________________________________")
      time.sleep(3)
else:
    print ("try again")


