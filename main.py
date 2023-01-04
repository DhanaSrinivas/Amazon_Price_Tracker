import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
my_email = "okanek69@gmail.com"
password = "zncnubcebwtvxiom"

url = "https://www.amazon.in/Atomic-Habits-James-Clear/dp/1847941834/ref=pd_rhf_d_ee_s_pd_crcd_sccl_1_1/262-5628988-8741217?pd_rd_w=wtYdE&content-id=amzn1.sym.dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_p=dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_r=RRCTFRM3WJNKK8QH9TTT&pd_rd_wg=yHXaw&pd_rd_r=136fc231-4b22-4ae4-9fc7-d58b3de6f82b&pd_rd_i=1847941834&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,te-IN;q=0.8,te;q=0.7,en-US;q=0.6"
}

# Finding price of the book
response = requests.get(url=url, headers=headers)
file = response.text

soup = BeautifulSoup(file, "lxml")
price_tag = soup.select_one(selector=".a-offscreen")
price = float(price_tag.string.replace("₹",""))
title = soup.find(id="productTitle")


# IF THE PRICE IS LESS THAN THE DESIRED PRICE, YOU'LL RECEIVE AN EMAIL

if price <= 450:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="dhanasubscribes@gmail.com", msg=f"Subject: Amazon Price Alert!\n\n{title.string} is now available at Rs.{price}\nClick here to order:\n {url}")
    connection.close()