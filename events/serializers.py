from rest_framework import serializers
from .models import EVENT_STATUS_CHOICES, Event, Reservation


class EventSerializer(serializers.ModelSerializer):

    reservation_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "venue", "date", "total_seats", "availiable_seats", "status", "created_at", "reservation_count"]

    def get_reservation_count(self, obj):
        return obj.reservations.filter(status= 'confirmed').count()


    def validate(self, data):
        if data.get('availiable_seats', 0) > data.get('total_seats', 0):
            raise serializers.ValidationError('Availiable Seats can not exceed than Total Seats')

        return data
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "event", "attendee_name", "attendee_email", "seat_reserved", "status", "created_at"]

    def validate_seat_reserved(self,value):
        if value<1:
            raise serializers.ValidationError("Must reserved at least 1 Seat")
        return value

    def validate(self, data):
        event = data.get('event')

        if event.status not in ("upcoming", "ongoing"):
            raise serializers.ValidationError(f"Can not reserve seat for a {event.status} event")

        if data.get('seat_reserved', 0) > event.availiable_seats:
            raise serializers.ValidationError(f"Only {event.availiable_seats} available")

        return data

    def create(self, validated_data):
        event = validated_data.get('event')
        event.availiable_seats -= validated_data.get('seat_reserved')
        event.save()
        return Reservation.objects.create(**validated_data)
        

# ============================================================
# OLD APPROACH: Using serializers.Serializer
# ============================================================

'''
class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 220)
    venue = serializers.CharField(max_length = 220)
    date = serializers.DateField()
    total_seats = serializers.IntegerField()
    availiable_seats = serializers.IntegerField()
    status = serializers.ChoiceField(choices=EVENT_STATUS_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Event.objects.create(**validated_data)
'''