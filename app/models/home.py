import urllib2
import datetime
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

        pizzas = [
            {
                'day': 'Monday',
                'sliver': sliver_pizzas[0].strip('.'),
                'cheeseboard': 'Closed'
            },
            {
                'day': 'Tuesday',
                'sliver': sliver_pizzas[1].strip('.'),
                'cheeseboard': cheeseboard_pizzas[0].strip('.')
            },
            {
                'day': 'Wednesday',
                'sliver': sliver_pizzas[2].strip('.'),
                'cheeseboard': cheeseboard_pizzas[1].strip('.')
            },
            {
                'day': 'Thursday',
                'sliver': sliver_pizzas[3].strip('.'),
                'cheeseboard': cheeseboard_pizzas[2].strip('.')
            },
            {
                'day': 'Friday',
                'sliver': sliver_pizzas[4].strip('.'),
                'cheeseboard': cheeseboard_pizzas[3].strip('.')
            },
            {
                'day': 'Saturday',
                'sliver': sliver_pizzas[5].strip('.'),
                'cheeseboard': cheeseboard_pizzas[4].strip('.')
            },
            {
                'day': 'Sunday',
                'sliver': 'Closed',
                'cheeseboard': 'Closed'
            }
        ]

        reorderedPizzas = []

        currentDay = datetime.datetime.now().strftime('%A')

        startingIndex = -1
        for index, pizza in enumerate(pizzas):
            if (pizza['day'] == currentDay):
                startingIndex = index
            if (startingIndex > -1):
                reorderedPizzas.append(pizza)

        for index, pizza in enumerate(pizzas):
            if (index < startingIndex):
                reorderedPizzas.append(pizza)
            else:
                break


        return reorderedPizzas