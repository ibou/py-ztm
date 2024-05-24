import requests, json
from bs4 import BeautifulSoup  
from JPGtoPNGconverter import main

response = requests.get("https://news.ycombinator.com/news")
response2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response2.text, "html.parser")

links = soup.select(".titleline")
links2 = soup2.select(".titleline")
subtext = soup.select(".score")
subtext2 = soup2.select(".score")

mega_links = links + links2
mega_subtext = subtext + subtext2

def sorted_hits(hn):
    return sorted(hn, key=lambda k: k["votes"], reverse=True)

def create_custom_hn(links, subtext):

    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find("a")["href"] if links[idx].find("a") else None
        vote = int(subtext[idx].getText().split()[0]) if idx < len(subtext) else 0
        hn.append({"title": title, "votes": vote, "href": href})
    return hn

def main():
  lis = create_custom_hn(mega_links, mega_subtext)
  lis = sorted_hits(lis)
  print(json.dumps(lis, indent=4, sort_keys=True), len(lis)) 


if __name__ == "__main__":
  main()
