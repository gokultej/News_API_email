import requests
from send_email import send_email


topic ="tesla"

api_key="e77c8b88d9f14977b733519602dcacd9"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "from=2023-07-06&" \
      "sortBy=publishedAt&" \
      "apiKey=e77c8b88d9f14977b733519602dcacd9"

#Make Request
request =requests.get(url)

#get a dictionary with data
content = request.json()

#Access the article titles and description
body =""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject:Today's NEWS"+"\n"+ body + article["title"] +"\n"+\
               article["description"]\
               + "\n" +ariticle["url"] +2*"\n"
body = body.encode("utf-8")
send_email(body)
