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

class KeawakapuView(TemplateView):
    template_name = 'beaches/south_maui/keawakapu.html'

class UluaView(TemplateView):
    template_name = 'beaches/south_maui/ulua.html'

class WaileaView(TemplateView):
    template_name = 'beaches/south_maui/wailea.html'

class PalaueaView(TemplateView):
    template_name = 'beaches/south_maui/palauea.html'

class PoolenalenaView(TemplateView):
    template_name = 'beaches/south_maui/poolenalena.html'

class LaPerouseBayView(TemplateView):
    template_name = 'beaches/south_maui/la_perouse_bay.html'
