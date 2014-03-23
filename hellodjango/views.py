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

  cheeseboard_pizzas = cheeseboard_soup.findAll('p')[0:5]
  cheeseboard_dates = cheeseboard_soup.findAll('h4')[1:6]

  sliver_pizzas = sliver_soup.findAll('p')[0:6]
  sliver_dates = sliver_soup.findAll('h2')[0:6]
  
  html_string = "<html><body>"

  for i in range(len(sliver_pizzas)):
    html_string += str(sliver_dates[i])
    html_string += str(sliver_pizzas[i])
  
  for j in range(len(cheeseboard_pizzas)):
    html_string += str(cheeseboard_dates[j])
    html_string += str(cheeseboard_pizzas[j])
  
  html_string += "</body></html>"
  return html_string
