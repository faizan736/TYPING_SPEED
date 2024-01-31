from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except :
            error = error+1

    return error
def speed_time(time_start,time_end,userinput):
    time_del=time_end-time_start
    time_R=round(time_del,2)
    speed=len(userinput)/time_R
    return round(speed)


test=["Elon Musk says Twitter is losing cash because advertising is still down sharply and the social media company is carrying heavy debt"
      ,"Meta is poised to launch a new app that appears to mimic Twitter, marking a direct challenge to the social media platform owned by billionaire Elon Musk"
       ,
      "Apple is now the first publicly traded company to close a trading day with a $3 trillion market value, marking another milestone for a technology juggernaut that has reshaped society with a line-up of products that churn out eye-popping profits"]
test1=r.choice(test)
print("*****Typing speed*****")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter :")
time_2=time()
print('speed :',speed_time(time_1,time_2,testinput),"w/sec")
print("Error : ",mistake(test1,testinput))
