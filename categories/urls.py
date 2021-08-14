from django.urls import path
from .views import (
    CategoriesDiscoveryView, CategoriesEmpowermentView, 
    CategoriesFoundationView, CategoriesTrainingView, 
    CategoriesUpliftmentView
)

urlpatterns = [
    path('purpose-discovery/', CategoriesDiscoveryView.as_view(), name='discovery'),
    path('youth-empowerment/', CategoriesEmpowermentView.as_view(), name='empowerment'),
    path('tm-foundation/', CategoriesFoundationView.as_view(), name='foundation'),
    path('training-school/', CategoriesTrainingView.as_view(), name='training'),
    path('spiritual-upliftment/', CategoriesUpliftmentView.as_view(), name='upliftment')
]
