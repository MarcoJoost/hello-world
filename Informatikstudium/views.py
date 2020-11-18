from django.views.generic import TemplateView

class Willkommen(TemplateView):
    template_name = 'willkommen_page.html'

class Anmelden(TemplateView):
    template_name = 'anmeldeseite.html'
