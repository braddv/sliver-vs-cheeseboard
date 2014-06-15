from django.shortcuts import render_to_response
from django.views.generic import View
from app.models.home import HomeModel

class HomeView(View):

    def __init__(self):
        self.model = HomeModel()

    def get(self, request, *args):
        pizza_data = {
            'pizzas': self.model.get_pizzas_data()
        }

        template_name = 'home.html'
        response = render_to_response(template_name, pizza_data)

        return response