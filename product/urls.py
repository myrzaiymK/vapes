from  django.urls import path
from .views import main,contact,shoes,collection,racing_boots,detail
from . import views
urlpatterns = [
    path('',main,name='index'),
    path('product/detail/<id>',detail,name='detail'),
    path('contact/',contact,name='contact'),
    path('shoes/',shoes,name='shoes'),
    path('collection/',collection,name='collection'),
    path('product/',racing_boots,name='boots'),
    # path('', views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/',
    #      views.cart_add,
    #      name='cart_add'),
    # path('remove/<int:product_id>/',
    #      views.cart_remove,
    #      name='cart_remove'),

]

