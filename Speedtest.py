#STP 1.0 Speedtest-program
#Program-tester of dl and ul speed of local machine

#importing libraries
import speedtest
import time
from time import sleep
import stun
#Set first point of timer
tic = time.perf_counter()
#set ASCII code color of text
color = "\033[032m"
#Start informing user
print(color)
print("Test is starting")
#Get web-ip of local pc
print(f"Your IP is:{stun.get_ip_info()}")
# Delay between replies in seconds
sleep(5)
print("Approximate execution time is ~90 seconds")
sleep(5)
print("Start download test...")
sleep(35)
print("Download test done")
sleep(5)
print("Start upload test...")
sleep(5)
print("Wait ~40 sec")
#Engine of program
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
#Geting MB/s info
dl = ((download/1024)/1024)/8
ul = ((upload/1024)/1024)/8
#Finish result
print(f"Test done.\nSpeed: {round(dl,2)} MB/s \nUpload speed: {round(ul,2)} MB/s")
tac = time.perf_counter()
_time = tic-tac
print(f"Test finished in {round(_time,2)} seconds")

"""Development by Puma"""