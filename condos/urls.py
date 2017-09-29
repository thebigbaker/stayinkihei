from django.conf.urls import url
from condos import views

urlpatterns = [
    url(r'^condos/$', views.CondosView.as_view(), name='condos'),
    url(r'^condos/kihei-kai-nani/$', views.KiheiKaiNaniView.as_view(), name='kkn'),
    url(r'^condos/pacific-shores/$', views.PacificShoresView.as_view(), name='pacific_shores'),
    url(r'^beaches/$', views.BeachesView.as_view(), name='beaches'),
    url(r'^beaches/south-maui/$', views.SouthMauiView.as_view(), name='south_maui'),
    url(r'^beaches/south-maui/kamaole-beaches/$', views.KamaoleBeachesView.as_view(), name='kamaole_beaches'),
    url(r'^beaches/south-maui/kalama-park/$', views.KalamaParkView.as_view(), name='kalama_park'),
    url(r'^beaches/south-maui/keawakapu-beach/$', views.KeawakapuView.as_view(), name='keawakapu'),
    url(r'^beaches/south-maui/ulua-beach/$', views.UluaView.as_view(), name='ulua'),
    url(r'^beaches/south-maui/wailea-beach/$', views.WaileaView.as_view(), name='wailea'),
    url(r'^beaches/south-maui/palauea-beach/$', views.PalaueaView.as_view(), name='palauea'),
    url(r'^beaches/south-maui/poolenalena-beach/$', views.PoolenalenaView.as_view(), name='poolenalena'),
    url(r'^beaches/south-maui/la-perouse-bay/$', views.LaPerouseBayView.as_view(), name='la_perouse_bay'),

]
