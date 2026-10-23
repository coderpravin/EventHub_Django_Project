from django.db import models

# Create your models here.
EVENT_STATUS_CHOICES = [
    ("upcoming", "Upcoming"),
    ("ongoing", "Ongoing"),
    ("completed", "Completed"),
    ("cancelled", "Cancelled"),
]

class Event(models.Model):
    title = models.CharField(max_length=220)
    venue = models.CharField(max_length=220)
    date = models.DateField()
    total_seats = models.PositiveIntegerField()
    availiable_seats = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=EVENT_STATUS_CHOICES, default="upcoming")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.venue}"

STATUS_CHOICES = [
    ("confirmed", "Confirmed"),
    ("cancelled", "Cancelled")
]

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reservations")
    attendee_name = models.CharField(max_length=220)
    attendee_email = models.EmailField()
    seat_reserved = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="confirmed")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee_name} - {self.event.title} - {self.seat_reserved} {self.created_at}"

    class Meta:
        ordering = ['-created_at']

    
    
