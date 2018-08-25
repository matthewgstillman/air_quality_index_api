from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^forecast$', views.forecast, name="forecast"),
    url(r'^heatmap$', views.heatmap, name="heatmap"),
    url(r'^$', views.index, name="index"),
    url(r'^result$', views.result, name="result"),
]