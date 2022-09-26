import random
temp = random.randrange(24, 38)
hmdty = random.randrange(30, 80)
print(temp, hmdty)
if(temp>30):
    if(hmdty>60):
        print("Alert")
    else:
        print("High temperature detected")
elif(temp==30):
    print("Temperature reaches the threshold value")
else:
    print("Comfortable condition")
        

