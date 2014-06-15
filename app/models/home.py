import urllib2
import datetime
from BeautifulSoup import BeautifulSoup as bs
from django.db import models

class HomeModel(models.Model):
    def __init__(self):
        self.closed_text = 'Closed'
        self.unknown_text = '???'
        self.current_year = str(datetime.datetime.now().year)
        self.current_day = datetime.datetime.now().strftime('%A')

    def get_pizzas_data(self):
        cheeseboard_html = urllib2.urlopen("http://cheeseboardcollective.coop/pizza")
        sliver_html = urllib2.urlopen("http://sliverpizzeria.com/")

        parseHtml = bs
        parsed_cheeseboard = parseHtml(cheeseboard_html)
        parsed_sliver = parseHtml(sliver_html)

        cheeseboard_pizzas_html = parsed_cheeseboard.findAll("div",attrs={"class":"column"})
        sliver_pizzas_html = parsed_sliver.findAll("div",attrs={"class":"home-excerpt"})

        cheeseboard_pizzas = [''] + [pizza.text for pizza in cheeseboard_pizzas_html[0].findAll('p')]
        cheeseboard_pizza_dates = [pizza.text for pizza in cheeseboard_pizzas_html[0].findAll('h4')]

        sliver_pizzas = [pizza.text for pizza in sliver_pizzas_html[0].findAll('p')]
        sliver_pizza_dates = [pizza.text for pizza in sliver_pizzas_html[0].findAll('h2')]

        # TODO: Compare pizza updated date to current date

        pizzas = []
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for dayIndex in range(0, 7):
            day = {
                'day': days[dayIndex]
            }

            if (days[dayIndex] == 'Sunday'):
                day['cheeseboard'] = {
                    'desc': self.closed_text
                }
                day['sliver'] = {
                    'desc': self.closed_text
                }
            elif (days[dayIndex] == 'Monday'):
                day['cheeseboard'] = {
                    'desc': self.closed_text
                }
                day['sliver'] = {
                    'desc': sliver_pizzas[dayIndex].strip('.'),
                    'date': sliver_pizza_dates[dayIndex].split(' ')[1]
                }
            else:
                day['cheeseboard'] = {
                    'desc': cheeseboard_pizzas[dayIndex].strip('.'),
                    'date': cheeseboard_pizza_dates[dayIndex].split(' ')[1]
                }
                day['sliver'] = {
                    'desc': sliver_pizzas[dayIndex].strip('.'),
                    'date': sliver_pizza_dates[dayIndex].split(' ')[1]
                }

            pizzas.append(day)

        reorderedPizzas = []
        startingIndex = -1
        for index, pizza in enumerate(pizzas):
            if (pizza['day'] == self.current_day):
                startingIndex = index
            if (startingIndex > -1):
                reorderedPizzas.append(pizza)

        for index, pizza in enumerate(pizzas):
            if (index < startingIndex):
                reorderedPizzas.append(pizza)
            else:
                break

        return reorderedPizzas