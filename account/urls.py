from django.urls import path
from . import views
from .views import AccountSuspendedView

urlpatterns = [
    path('reision/delete', views.revisiondelete, name="rev_delete"),
    path('user/lockedout/', AccountSuspendedView.as_view(), name='accountSuspended'),
]
