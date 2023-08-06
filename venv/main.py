import requests

api_key="e77c8b88d9f14977b733519602dcacd9"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-06&sortBy=publishedAt&apiKey=e77c8b88d9f14977b733519602dcacd9"

request =requests.get(url)
content = request.json()
#get a dictionary with data
print(content["articles"])

#Access the article titles and description
for article in content["articles"]:
    print(artilce["title"])
