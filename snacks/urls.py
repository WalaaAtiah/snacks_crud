from django.urls import path
from .views import SnackListView ,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView
urlpatterns = [
    path('', SnackListView .as_view(), name='Snack_List'),
    path('<int:pk>/', SnackDetailView.as_view(), name='Snack_Detail'),
    path('create/', SnackCreateView.as_view(), name='Snack_Create'),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name='Snack_Update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name='Snack_Delete')
    

]
