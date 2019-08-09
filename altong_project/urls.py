from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import altong.views
import daily.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', altong.views.home, name="home"),
    path('account/', include("account.urls")),
    path('daily/', include("daily.urls")),
]
