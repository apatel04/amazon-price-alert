import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.com/Polaroid-Wireless-Printer-Compatible-Bluetooth/dp/B00TE8XKIS'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def price_checker():
    page = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(page.content, 'lxml')
    
    title = soup.find(id='productTitle').getText(strip=True)
    print(title)
    
    price = soup.find(id='priceblock_ourprice').getText()
    float_price = float(price.replace('$',''))
    print(float_price)
    
    if(float_price <= 71.00):
        send_email()
        
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('patel.archa@gmail.com','xagshqqrdvwyqduc')
    
    email_subject = 'Price drop alert for Polaroid Zip Camera'
    email_body = url
    email = f'Subject: {email_subject}\n\n{email_body}'
    
    server.sendmail('patel.archa@gmail.com','starwarsash@gmail.com', email)
    print('Alert was sent')
    
    server.quit()

while(True):
    price_checker()
    time.sleep(86400)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




