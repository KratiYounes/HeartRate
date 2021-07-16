print("Please enter your heart rate")
heart_rate = input()

too_low = heart_rate < 60
too_high = heart_rate > 100
if(too_low == False and too_high == False):
    print("Your heart rate is normal")
elif(too_low == True):
    print("Your heart rate is low")
elif(too_high == True):
    print("Your heart rate is high")