from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('create', views.create_restaurant, name='create_restaurant'),
    path('add', views.add_restaurant, name='add_restaurant'),
    path('review/<int:id>', views.add_review, name='add_review'),
    path('jtest',views.jtest, name='jtest'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)