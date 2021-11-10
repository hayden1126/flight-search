from query_date import convert_query_date_to_list
import requests
# from urllib.request import urlopen, Request
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

"""
query_range = "dateStart - dateEnd month year
1-5 09 2021
06 09 2021
"""


global API_URL
API_URL = ["https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1&date=", "&lang=", "&cargo=", '&arrival=']

global resList 
resList =[]

query_range = "9-11 09 2021"

def query_HKIA_API(date, lang, isCargo, isArrival):
    """
    example API
    https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1&date=2021-09-10&lang=en&cargo=false&arrival=true
    
    date: String (format: YYYY-MM-DD)
    lang: String
    isCargo: string
    isArrival: string 

    """

    def check_isCargo_state(isCargo):
        if isCargo:
            return "true"
        else:
            return "false"

    def check_isArrival_state(isArrival):
        if isArrival:
            return "true"
        else:
            return "false"


    URL_to_query = API_URL[0] + \
            date + \
            API_URL[1] + \
            lang + \
            API_URL[2] + \
            check_isCargo_state(isCargo) + \
            API_URL[3] + \
            check_isArrival_state(isArrival)


    print(URL_to_query)

    # res = requests.get(URL_to_query)

    return requests.get(URL_to_query).json()



    # print(type(res.text))



def main():
    for date in convert_query_date_to_list(query_range):
        resList.append(query_HKIA_API(date, "en", False, False))

    cleaned_resList = []
        
    #exact data from the query date, eliminate data from other date
    for k in resList:
        if len(k) < 2:
            # print(k[0]["date"])
            cleaned_resList.append(k[0])
        elif len(k) > 1 and len(k) < 3:
            # print(k[-1]["date"])
            cleaned_resList.append(k[-1])
        elif len(k) > 2 and len(k) < 4:
            # print(k[1]["date"])
            cleaned_resList.append(k[1])

    for d in cleaned_resList:
        # print(d[0]["list"][0]["flight"][0]["airline"])
        # print(d["list"][0]["flight"][0]["airline"])
        counter = 0
        for f in d["list"]:
            if f["destination"][-1] == "NYC":
                # print(f["flight"][0]["airline"])
                counter = counter + 1
        print(counter)






if __name__ == "__main__":
    main()

sum = 0

# for date in query_date_list:
#     context = ssl._create_unverified_context()

#     ssl._create_default_https_context = ssl._create_unverified_context

#     url = "https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1&date=" + date + "&lang=en&cargo=false&arrival=false"

#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
#     # reg_url = url
#     # req = Request(url=reg_url, headers=headers) 
    
#     # page = urlopen(url, context=context).read()


#     req = urllib.request.Request(url)
#     req.add_header("User-Agent", "Mozilla/5.0")
#     print(urllib.request.urlopen(req).read().decode('UTF-8'))


#     # print("hayden's code here {}".format(page))
