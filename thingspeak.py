


try:
    from urllib import request
    from urllib.request import urlopen
    import threading                    # import threadding
    import json                         # import json
    import random                       # import random
    import requests                     # import requests
    import ssl
except:
    print("No Library Found")


class Thingspeak(object):

    def __init__(self, write_key=None, timer=10, read_api_key=None):

        """

        :param write_key:  takes a string of write api key
        :param timer: can take integer values
        """

        self.url = 'https://api.thingspeak.com/update?api_key='
        self.write_key = write_key
        self.timer = timer
        self.read_api_key = read_api_key
        self.read_url = 'https://api.thingspeak.com/channels/557500/feeds.json?api_key='
        self.feild1 = []
        self.feild2 = []


    def post_cloud(self, value1, value2):

        """

        :param value1: can be interger or float
        :param value2: can be interger or float
        :return: updated to cloud storage
        """

        threading.Timer(interval= self.timer,
                        function= self.post_cloud,args=[value1,value2]).start()
        Timer = self.timer
        URL = self.url
        KEY = self.write_key
        HEADER = '&field1={}&field2={}'.format(str(value1), str(value2))

        NEW_URL = str(URL) + str(KEY) + str(HEADER)
        print(NEW_URL)

        context = ssl._create_unverified_context()

        data = request.urlopen(NEW_URL,context=context)
        print(data)


    def read_cloud(self, result=2):
        """

        :param result: how many data you want to fetch accept interger
        :return: Two List which contains Sensor data
        """

        URL_R = self.read_url
        read_key = self.read_api_key
        header_r ='&results={}'.format(result)

        new_read_url = URL_R + read_key + header_r

        data = requests.get(new_read_url).json()

        field1 = data['feeds']

        for x in field1:
            self.feild1.append(x['field1'])
            self.feild2.append(x['field2'])

        return self.feild1,self.feild2

