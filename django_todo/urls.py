from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todoapp.urls')),
    path('sentry-debug/', trigger_error),
]
