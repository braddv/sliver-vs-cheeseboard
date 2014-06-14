from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib2
from BeautifulSoup import BeautifulSoup as bs
import re

def home(request):
  pizza_data = get_pizzas_data()
  template_file = 'templates/home.html'
  response = render_to_response(template_file, pizza_data)
  return response

def get_pizzas_data():
  cheeseboard_page = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
  sliver_page = urllib2.urlopen("http://sliverpizzeria.com/")
  cheeseboard_soup = bs(cheeseboard_page)
  sliver_soup = bs(sliver_page)

  cheeseboard_pizzas = cheeseboard_soup.findAll("div",attrs={"class":"column"})
  sliver_pizzas = sliver_soup.findAll("div",attrs={"class":"home-excerpt"})

  cheeseboard_pizzas = [pizza.text for pizza in cheeseboard_pizzas[0].findAll('p')]
  sliver_pizzas = [pizza.text for pizza in sliver_pizzas[0].findAll('p')]

  pizzas = {
    "sliver": sliver_pizzas,
    "cheeseboard": cheeseboard_pizzas
  }

  return pizzas

if __name__ == "__main__":
  print(get_pizzas())
