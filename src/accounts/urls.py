from django.urls import path
from accounts.views import (
    Login, Logout, Signup
)

app_name = 'accounts'


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup')
]
