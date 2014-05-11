from django.http import HttpResponse
import urllib2
from BeautifulSoup import BeautifulSoup as bs
import re

def home(request):
  html = get_pizzas()
  return HttpResponse(html)

def get_pizzas():
  cheeseboard_page = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
  sliver_page = urllib2.urlopen("http://sliverpizzeria.com/")
  cheeseboard_soup = bs(cheeseboard_page)
  sliver_soup = bs(sliver_page)

  cheeseboard_pizzas = cheeseboard_soup.findAll("div",attrs={"class":"column"})
  sliver_pizzas = sliver_soup.findAll("div",attrs={"class":"home-excerpt"})

  cheeseboard_pizzas = [pizza.text for pizza in cheeseboard_pizzas[0].findAll('p')]
  sliver_pizzas = [pizza.text for pizza in sliver_pizzas[0].findAll('p')] 
  
  html_string = "<html><body>"

  html_string += "<div style='width:50%;float:left'>"
  html_string += "<h2>SLIVER</h2>"
  html_string += "<h3>MONDAY</h3>"
  html_string += sliver_pizzas[0] 
  html_string += "<h3>TUESDAY</h3>"
  html_string += sliver_pizzas[1]
  html_string += "<h3>WEDNESDAY</h3>"
  html_string += sliver_pizzas[2]
  html_string += "<h3>THURSDAY</h3>"
  html_string += sliver_pizzas[3]
  html_string += "<h3>FRIDAY</h3>"
  html_string += sliver_pizzas[4]
  html_string += "<h3>SATURDAY</h3>"
  html_string += sliver_pizzas[5]
  html_string += "</div><div style='width:50%;float:left'>"
  html_string += "<h2>CHEESEBOARD</h2>"
  html_string += "<h3>MONDAY</h3>"
  html_string += "no pizza,<br>"
  html_string += "today."
  html_string += "<h3>TUESDAY</h3>"
  html_string += cheeseboard_pizzas[0]
  html_string += "<h3>WEDNESDAY</h3>"
  html_string += cheeseboard_pizzas[1]
  html_string += "<h3>THURSDAY</h3>"
  html_string += cheeseboard_pizzas[2]
  html_string += "<h3>FRIDAY</h3>"
  html_string += cheeseboard_pizzas[3]
  html_string += "<h3>SATURDAY</h3>"
  html_string += cheeseboard_pizzas[4]
  html_string += "</div>"
  html_string += "</body></html>"
  return html_string

if __name__ == "__main__":
  print(get_pizzas())
