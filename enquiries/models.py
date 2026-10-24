from django.db import models


class Enquiry(models.Model):
    class TourType(models.TextChoices):
        FIT = "FIT", "FIT"
        GROUP = "Group", "Group"
        PILGRIMAGE = "Pilgrimage", "Pilgrimage"
        CORPORATE = "Corporate", "Corporate"

    class HotelCategory(models.TextChoices):
        BUDGET = "Budget", "Budget"
        THREE_STAR = "3-star", "3-star"
        FOUR_STAR = "4-star", "4-star"
        FIVE_STAR = "5-star", "5-star / Luxury"
        NOT_SURE = "Not sure", "Not sure yet"

    class Transport(models.TextChoices):
        CAR = "Car", "Car / SUV"
        TRAVELLER = "Tempo Traveller", "Tempo Traveller"
        COACH = "Coach", "Coach / Bus"
        NOT_REQUIRED = "Not required", "Not required"
        NOT_SURE = "Not sure", "Not sure yet"

    class Status(models.TextChoices):
        NEW = "New", "New"
        CONTACTED = "Contacted", "Contacted"
        QUOTED = "Quoted", "Quoted"
        WON = "Won", "Won"
        LOST = "Lost", "Lost"

    name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    city_country = models.CharField(max_length=160)
    travel_start_date = models.DateField()
    travel_end_date = models.DateField(blank=True, null=True)
    guests = models.PositiveIntegerField()
    destinations = models.CharField(max_length=300)
    tour_type = models.CharField(max_length=20, choices=TourType.choices)
    hotel_category = models.CharField(max_length=20, choices=HotelCategory.choices)
    transport = models.CharField(max_length=30, choices=Transport.choices)
    requirements = models.TextField()
    consent_given = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.company_name} — {self.name} ({self.created_at:%d %b %Y})"
