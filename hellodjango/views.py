from django.http import HttpResponse
import urllib2
from BeautifulSoup import BeautifulSoup as bs

def home(request):
  html = get_pizzas()
  return HttpResponse(html)

def get_pizzas():
  cheeseboard_page = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
  sliver_page = urllib2.urlopen("http://sliverpizzeria.com/home/")
  cheeseboard_soup = bs(cheeseboard_page)
  sliver_soup = bs(sliver_page)

  cheeseboard_pizzas = cheeseboard_soup.findAll("div",attrs={"class":"column"})

  sliver_pizzas = sliver_soup.findAll("div",attrs={"class":"panel menu"})
  
  html_string = "<html><body>"

  html_string += "<h2>SLIVER</h2>"

  html_string += str(sliver_pizzas[0])[148:]
  html_string += "<h2>CHEESEBOARD</h2>"
  html_string += str(cheeseboard_pizzas[0])[0:1111]

  html_string += "</body></html>"
  return html_string

if __name__ == "__main__":
  print(get_pizzas())
