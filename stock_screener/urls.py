"""stock_screener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from momentum_app.views import ListDJ30, DetailDJ30, ListEtf, ListDivs, ListNotes, ListSP500, DetailEtf, UpdateNotes, Updatedj30, Updatesp500, Updatedivs, Updateetf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj30/', ListDJ30.as_view()),
    path('dj30/<symbol>', DetailDJ30.as_view()),
    path('etf/', ListEtf.as_view()),
    path('etf/<name>', DetailEtf.as_view()),
    path('divs/', ListDivs.as_view()),
    path('notes/', ListNotes.as_view()),
    path('notes/<id>', UpdateNotes.as_view()),
    path('sp500/', ListSP500.as_view()),
    path('update/dj30/', Updatedj30.as_view()),
    path('update/sp500/', Updatesp500.as_view()),
    path('update/divs/', Updatedivs.as_view()),
    path('update/etf/', Updateetf.as_view()),
]
