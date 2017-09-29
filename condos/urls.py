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

]
