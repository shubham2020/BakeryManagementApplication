from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST FRAMEWORK URLS
    path('api/account/', include('account.api.urls', 'account-api')),
    path('api/bakery/', include('bakery.api.urls', 'bakery-api')),
]
