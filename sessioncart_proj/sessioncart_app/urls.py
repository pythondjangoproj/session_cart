# from django.contrib import admin
from django.urls import path
from . import views
app_name='sessioncart_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.add_item_view, name='add_item_view'),
    path('display/',views.display_item, name='display_item'),
]
