from plyer import notification
import requests
# Parsing web data using beautifulsoup4
from bs4 import BeautifulSoup
import time





def notify_Me(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C://Users//KIIT//PycharmProjects//abhirashmiproject/PYTHON PROJECTS//Realtime CoronaVirus Outbreak Notification System//virus.ico",
        timeout=20
    )


def get_data_from_url(url):
    r=requests.get(url)
    return r.text


if __name__ == '__main__':
    while(True):
        notify_Me("Abhirashmi","let us stop the spread of corona virus together")
        my_HTML_data=get_data_from_url("https://www.mohfw.gov.in/")

        #print(my_HTML_data)
        soup=BeautifulSoup(my_HTML_data,'html.parser')
        #print(soup.prettify())
        myData_str=" "
        for tr in soup.find_all('tbody')[1].find_all('tr'): #as there are many tables present in the given url but we are intrested in table having index = 1
            myData_str = myData_str + tr.get_text()

            myData_str = myData_str[1:] ##for managing the gap in first data we have
            item_List= myData_str.split("\n\n")

            states=['Bihar','Chhattisgarh','Delhi','Haryana','Jharkhand','Odisha','Uttar Pradesh','Tripura']
            for item in item_List[0:22]:
                data_list = item.split('\n')

                if data_list[1] in states:
                    print(data_list)

                    nTitle="Cases of covid 19 "

                    nText=f" STATE : {data_list[1]} Indian :{data_list[2]} & Foreign : {data_list[3]} \nCured : {data_list[4]}\n" \
                          f"Deaths : {data_list[5]}"

                    notify_Me(nTitle,nText)
                    time.sleep(4)
            time.sleep(3600)