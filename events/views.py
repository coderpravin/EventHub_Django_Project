from django.shortcuts import render,get_object_or_404
from .models import Event, Reservation
from .serializers import EventSerializer, ReservationSerializer


# ============================================================
# New APPROACH: Class-Based Views (CBV)
# ============================================================

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
class EventViewSet(viewsets.ModelViewSet):
    # queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        status_data = self.request.query_params.get('status')
        venue_data = self.request.query_params.get('venue')

        if status_data:
            queryset = queryset.filter(status = status_data)

        if venue_data:
            queryset = queryset.filter(venue= venue_data)
        return queryset

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()    
        event_id = self.request.query_params.get('event_id')

        if event_id:
            queryset = queryset.filter(event_id= event_id)

        return queryset

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        reservation = self.get_object()
        if reservation.status == "cancelled":
            return Response({"message" : "Already cancelled"},
                            status=status.HTTP_400_BAD_REQUEST)

        reservation.event.availiable_seats += reservation.seat_reserved
        reservation.event.save()
        
        reservation.status = "cancelled"
        reservation.save()

        return Response({
            "message" : "resevation cancelled"},
            status = status.HTTP_200_OK
        )

# Create your views here
# ============================================================
# OLD APPROACH: Function-Based Views (FBV)
# ============================================================

'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
@api_view(["GET"])
def listEvent(request):
    event_id = request.query_params.get('id')

    if event_id:
        try:
            event = get_object_or_404(Event, id=event_id)
        except Event.DoesNotExist:
            return Response(
                {'error':'Event not found'}
            )
        serializer = EventSerializer(event)
        return Response(serializer.data)
        
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def createEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)  


@api_view(["PUT"])
def updateEvent(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"error":"Event Not present"})

    serializer = EventSerializer(event, data= request.data)
    if serializer.is_valid():
        event.title = serializer.validated_data["title"]
        event.venue = serializer.validated_data["venue"]
        event.date = serializer.validated_data["date"]
        event.total_seats = serializer.validated_data["total_seats"]
        event.availiable_seats = serializer.validated_data["availiable_seats"]
        event.status = serializer.validated_data["status"]

        event.save()
        return Response(EventSerializer(event).data)
    return Response(serializer.errors) 


@api_view(["DELETE"])
def deleteEvent(request, id):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return Response({"message":"Event deleted successfully"})
    except Event.DoesNotExist:
        return Response({'message': "Event not found"})

'''
