
import random
temp = random.randrange(24,36)
humid = random.randrange(40,80)
print(temp,humid)

if(temp>30):
    if(humid>60):
        print("Alert Detected")
    else:
        print("High temperature detected")
elif(temp==30):
    print("Temperature reaches the high comfortable value")
else:
    print("Comfortable condition")
