# thingspeakpy
upload data to cloud server with 4 line of code 

Hello everyone in this I want to share how easy it is to upload sensor data on cloud server using python.
usually, when you have to upload data on cloud server you require to process data and convert it into the desired encoding 
and then upload it.

All the Hassle is over.
 The class that I have developed with just 4 lines of code you can upload data on cloud server it that's easy
 
w_key = 'YOUR KEY'
r_key = 'YOUR KEY'
x,y = sensor_value()

m = Thingspeak(write_key=None,timer=10, read_api_key=r_key)
m.post(x,y)
x = m.read_cloud()
print(x)

This will rapidly increase your productivity 
as you don't need to worry about backend focus more on application now ! 
open source license

<img width="929" alt="Screen Shot 2019-03-11 at 5 21 46 PM" src="https://user-images.githubusercontent.com/39345855/54158975-34fbba00-4422-11e9-8e15-0ec39c5a1a2a.png">

to upload data just add a function and call it and pass the param

def sensor_value():
    """

    Put your Raspberry or arduino senor code here



    :return: sensor Data
    """
    x = np.random.randint(0, 33)
    y = np.random.randint(0, 33)
    return x, y
    
   complete article can be found at
   
   https://www.linkedin.com/pulse/thingspeak-python-iot-soumil-shah/
