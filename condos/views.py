from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class CondosView(TemplateView):
    template_name = 'condos/condos.html'

class KiheiKaiNaniView(TemplateView):
    template_name = 'condos/kkn.html'

class PacificShoresView(TemplateView):
    template_name = 'condos/ps.html'

class BeachesView(TemplateView):
    template_name = 'beaches/beaches.html'

class SouthMauiView(TemplateView):
    template_name= 'beaches/south_maui/south_maui.html'

class KamaoleBeachesView(TemplateView):
    template_name = 'beaches/south_maui/kamaole_beaches.html'

class KalamaParkView(TemplateView):
    template_name = 'beaches/south_maui/kalama_park.html'

#class KeawakapuView(TemplateView):
#    template_name = 'beaches/south_maui/keawakapu.html'
