from django.urls import path, include
from .import views

# ============================================================
# New APPROACH: URL Configuration Using Class-Based Views
# ============================================================

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls))
]

'''
# ============================================================
# OLD APPROACH: URL Configuration Using Function-Based Views
# ============================================================

urlpatterns = [
    path('events/', views.listEvent), #api/events/ ----> for Get request
    path('events/create/', views.createEvent), #api/events/ ----> for Post request
    path('events/<int:id>/update/', views.updateEvent), #api/events/ ----> for Put request
    path('events/<int:id>/delete/', views.deleteEvent), #api/events/ ----> for Delete request
            
]
'''

