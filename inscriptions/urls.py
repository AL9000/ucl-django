from django.urls import path

from inscriptions import views

app_name = "inscriptions"
urlpatterns = [
    # path("", views.home_view),
    path("", views.InscriptionRequestListView.as_view(), name="list"),
    path("<int:pk>/", views.InscriptionRequestDetailView.as_view(), name="detail"),
    path("create/", views.InscriptionRequestCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.InscriptionRequestUpdateView.as_view(), name="update"),
    path("search/", views.InscriptionRequestSearchView.as_view(), name="search"),
    # path("search_function/", views.search_inscriptions, name="search"),
]
