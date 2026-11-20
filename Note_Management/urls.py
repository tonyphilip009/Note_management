from django.contrib import admin
from django.urls import path
from Notes_app.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",RegistrationView.as_view()),
    path("login/",obtain_auth_token),
    path("notes/",ListNotes.as_view()),
    path("logout/",LogOut.as_view()),
    path("notes/<int:note_id>/", NoteRetriveUpdateDelete.as_view()),
    path("jwt_login/",TokenObtainPairView.as_view()),
    path("task/",TaskListCreate.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
    path('task/<int:pk>/', RetriveUpdateDelete.as_view()),
    path("jwt_logout/",jwt_logout.as_view())
]
