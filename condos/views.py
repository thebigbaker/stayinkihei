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
    template_name= 'beaches/south_maui_beaches/south_maui_beaches.html'

class KamaoleBeachesView(TemplateView):
    template_name = 'beaches/south_maui_beaches/kamaole_beaches.html'

class KalamaParkView(TemplateView):
    template_name = 'beaches/south_maui_beacheskalama_park.html'

class KeawakapuView(TemplateView):
    template_name = 'beaches/south_maui_beaches/keawakapu.html'

class UluaView(TemplateView):
    template_name = 'beaches/south_maui_beaches/ulua.html'

class WaileaView(TemplateView):
    template_name = 'beaches/south_maui_beaches/wailea.html'

class PalaueaView(TemplateView):
    template_name = 'beaches/south_maui_beaches/palauea.html'

class PoolenalenaView(TemplateView):
    template_name = 'beaches/south_maui_beaches/poolenalena.html'

class LaPerouseBayView(TemplateView):
    template_name = 'beaches/south_maui_beaches/la_perouse_bay.html'

class WestMauiBeachesView(TemplateView):
    template_name = 'beaches/west_maui_beaches/west_maui_beaches.html'

class KaanapaliBeachView(TemplateView):
    template_name = 'beaches/west_maui_beaches/kaanapali_beach.html'

class NapiliBayView(TemplateView):
    template_name = 'beaches/west_maui_beaches/napili_bay.html'

class KapaluaBayView(TemplateView):
    template_name = 'beaches/west_maui_beaches/kapalua_bay.html'

class HonoluaBayView(TemplateView):
    template_name = 'beaches/west_maui_beaches/honolua_bay.html'
