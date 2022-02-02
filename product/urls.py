from  django.urls import path
from .views import main,contact,shoes,collection,racing_boots
urlpatterns = [
    path('',main),
    path('contact/',contact),
    path('shoes/',shoes),
    path('collection/',collection),
    path('product/',racing_boots)
]
