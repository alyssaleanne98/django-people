from django.urls import path
from .views import Person, PersonDetail

urlpatterns = [
    path('', Person.as_view(), name='person'),
    path('<int:pk>', PersonDetail.as_view(), name='people_detail')
]