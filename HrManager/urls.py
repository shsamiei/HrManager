from django.contrib import admin
from django.urls import path, include
# import debug_toolbar

admin.site.site_header = 'Sotoon Human Resource Manager'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('manager.urls')),
    path('auth/', include('djoser.urls')),
    path('user/', include('core.urls')),

    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('__debug__/', include(debug_toolbar.urls)),
]
