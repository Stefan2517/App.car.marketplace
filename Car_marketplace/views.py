from django.shortcuts import render
from django.views import generic
from .models import Item, CAR_BRAND
from django.views.generic.base import TemplateView

# puteam clase sau functii, dar clasele au cod mai putin si e mai clean

class PaginaPrincipala(generic.ListView):  # reprezinta pagina cu toate masinile adica cea principala
    queryset = Item.objects.order_by('-data_crearii') # minusul inverseaza ordinea
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masini'] = CAR_BRAND
        return context


class MasinaDetalii(generic.DetailView):
    model = Item
    template_name = 'masina_detalii.html'

class About(TemplateView):

    template_name = 'about.html'