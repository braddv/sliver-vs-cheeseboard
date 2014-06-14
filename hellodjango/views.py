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
  cheeseboard_html = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
  sliver_html = urllib2.urlopen("http://sliverpizzeria.com/")

  parseHtml = bs
  parsed_cheeseboard = parseHtml(cheeseboard_html)
  parsed_sliver = parseHtml(sliver_html)

  cheeseboard_pizzas_html = cheeseboard_soup.findAll("div",attrs={"class":"column"})
  sliver_pizzas_html = sliver_soup.findAll("div",attrs={"class":"home-excerpt"})

  cheeseboard_pizzas = [pizza.text for pizza in cheeseboard_pizzas_html[0].findAll('p')]
  sliver_pizzas = [pizza.text for pizza in sliver_pizzas_html[0].findAll('p')]

  pizzas = {
    "sliver": sliver_pizzas,
    "cheeseboard": cheeseboard_pizzas
  }

  return pizzas

if __name__ == "__main__":
  print(get_pizzas_data())
