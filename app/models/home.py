import urllib2
from BeautifulSoup import BeautifulSoup as bs
from django.db import models

class HomeModel(models.Model):
    def get_pizzas_data(self):
        cheeseboard_html = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
        sliver_html = urllib2.urlopen("http://sliverpizzeria.com/")

        parseHtml = bs
        parsed_cheeseboard = parseHtml(cheeseboard_html)
        parsed_sliver = parseHtml(sliver_html)

        cheeseboard_pizzas_html = parsed_cheeseboard.findAll("div",attrs={"class":"column"})
        sliver_pizzas_html = parsed_sliver.findAll("div",attrs={"class":"home-excerpt"})

        cheeseboard_pizzas = [pizza.text for pizza in cheeseboard_pizzas_html[0].findAll('p')]
        sliver_pizzas = [pizza.text for pizza in sliver_pizzas_html[0].findAll('p')]

        pizzas = {
            "sliver": sliver_pizzas,
            "cheeseboard": cheeseboard_pizzas
        }

        return pizzas