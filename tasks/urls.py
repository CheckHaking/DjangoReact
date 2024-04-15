from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from tasks import views



#Api routing
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    #path('nombre_dela_url/', )
    path('api/v1/', include(router.urls)),
    #aniadimos una nueva ruta con el modulo de coreapi
    path('docs/', include_docs_urls(title="Task API"))
]

#todo este codigo genera las rutas GET, PUT, POST, DELETE
