from django.conf.urls import url
from condos import views

urlpatterns = [
    url(r'^condos/$', views.CondosView.as_view(), name='condos'),
    url(r'^condos/kihei-kai-nani/$', views.KiheiKaiNaniView.as_view(), name='kkn'),
    url(r'^condos/pacific-shores/$', views.PacificShoresView.as_view(), name='pacific_shores'),
    url(r'^beaches/$', views.BeachesView.as_view(), name='beaches'),
    url(r'^beaches/south-maui/$', views.SouthMauiView.as_view(), name='south_maui_beaches'),
    url(r'^beaches/south-maui/kamaole-beaches/$', views.KamaoleBeachesView.as_view(), name='kamaole_beaches'),
    url(r'^beaches/south-maui/kalama-park/$', views.KalamaParkView.as_view(), name='kalama_park'),
    url(r'^beaches/south-maui/keawakapu-beach/$', views.KeawakapuView.as_view(), name='keawakapu'),
    url(r'^beaches/south-maui/ulua-beach/$', views.UluaView.as_view(), name='ulua'),
    url(r'^beaches/south-maui/wailea-beach/$', views.WaileaView.as_view(), name='wailea'),
    url(r'^beaches/south-maui/palauea-beach/$', views.PalaueaView.as_view(), name='palauea'),
    url(r'^beaches/south-maui/poolenalena-beach/$', views.PoolenalenaView.as_view(), name='poolenalena'),
    url(r'^beaches/south-maui/la-perouse-bay/$', views.LaPerouseBayView.as_view(), name='la_perouse_bay'),
    url(r'^beaches/west-maui/$', views.WestMauiBeachesView.as_view(), name='west_maui_beaches'),
    url(r'^beaches/west-maui/kaanapali-beach/$', views.KaanapaliBeachView.as_view(), name='kaanapali_beach'),
    url(r'^beaches/west-maui/napili-bay/$', views.NapiliBayView.as_view(), name='napili_bay'),
    url(r'^beaches/west-maui/kapalua-bay/$', views.KapaluaBayView.as_view(), name='kapalua_bay'),
    url(r'^beaches/west-maui/honolua-bay/$', views.HonoluaBayView.as_view(), name='honolua_bay'),
    url(r'^beaches/north-maui/$', views.NorthMauiBeachesView.as_view(), name='north_maui_beaches'),
    url(r'^activities/$', views.ActivitiesView.as_view(), name='activities'),
    url(r'^activities/old-lahaina-luau/$', views.OldLahainaLuauView.as_view(), name='old_lahaina_luau'),
    url(r'^activities/whale-watching/$', views.WhaleWatchingView.as_view(), name='whale_watching'),
    url(r'^activities/maui-ocean-center-and-aquarium/$', views.AquariumView.as_view(), name='aquarium'),
    url(r'^activities/haleakala/$', views.HaleakalaView.as_view(), name='haleakala'),
    url(r'^activities/snorkeling/$', views.SnorkelingView.as_view(), name='snorkeling'),
    url(r'^activities/drive-to-hana/$', views.DriveToHanaView.as_view(), name='drive_to_hana'),
    url(r'^activities/maui-friday-town-parties/$', views.MauiFridayTownPartiesView.as_view(), name='maui_friday_town_parties'),
    url(r'^activities/alii-kula-lavendar-farm/$', views.AliiKulaLavendarFarmView.as_view(), name='alii_kula_lavendar_farm'),
    


]
