import serial
import time

ser = serial.Serial('COM4', 9600) # stavi na kojem COM-u je arduino

data = []

while True:
    b = ser.readline()         
    string_n = b.decode()  
    string = string_n.rstrip() 
    if string == "": # tu cemo sam stavit neki string kao zaustavni uvjet
        break
    data.append(string)          
    time.sleep(0.1)  # stavi otprilike koliko sekundi treba za jedno očitanje
    

ser.close()
f = open("objFile.obj", "w")

for line in data:
    print(line)
    # ako ovo do sad radi
    f.write(line)
    
f.close()
