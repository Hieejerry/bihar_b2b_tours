from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("company_name", "name", "phone", "guests", "tour_type", "travel_start_date", "status", "created_at")
    list_filter = ("status", "tour_type", "hotel_category", "transport", "travel_start_date")
    search_fields = ("name", "company_name", "email", "phone", "destinations")
    list_editable = ("status",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Agent details", {"fields": ("name", "company_name", "email", "phone", "city_country")} ),
        ("Tour requirement", {"fields": ("travel_start_date", "travel_end_date", "guests", "destinations", "tour_type", "hotel_category", "transport", "requirements")} ),
        ("Lead management", {"fields": ("status", "consent_given", "created_at", "updated_at")} ),
    )
