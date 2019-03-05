import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.fedex.com/apps/fedextrack/?tracknumbers=285079912032828')

soup = BeautifulSoup(response.text, 'html.parser')

exceptions = soup.find(class_='tracking_main_container')

with open('exceptions.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['deliveryExceptions']
    csv_writer.writerow(headers)

    for exception in exceptions:
        deliveryExceptions = exception.find(class_='redesignTravelHistory tank-thlist__status-details').get_text()
        csv_writer.writerow([deliveryExceptions])