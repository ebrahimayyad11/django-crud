from django.urls import path
from .views import SnackCreateView, SnackDetail, SnackList, SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns=[
    path('',SnackList.as_view(), name='snacklist'),
    path('<int:pk>', SnackDetail.as_view(), name='snackdetail'),
    path('create/', SnackCreateView.as_view(), name='snackcreate'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snackupdate'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snackdelete'),
]