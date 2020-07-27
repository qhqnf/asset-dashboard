from django.urls import path
from . import views
from .models import User
from .serializers import UserSerializer

urlpatterns = [
    path(
        "",
        views.UserListView.as_view(
            queryset=User.objects.all(), serializer_class=UserSerializer
        ),
    )
]


app_name = "users"
