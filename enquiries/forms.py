from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    destinations = forms.MultipleChoiceField(
        choices=[
            ("Bodh Gaya", "Bodh Gaya"),
            ("Rajgir", "Rajgir"),
            ("Nalanda", "Nalanda"),
            ("Vishali and Keshariya", "Vishali and Keshariya"),
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Destinations required",
    )

    class Meta:
        model = Enquiry
        fields = [
            "name", "company_name", "email", "phone", "city_country",
            "travel_start_date", "travel_end_date", "guests", "destinations",
            "tour_type", "hotel_category", "transport", "requirements", "consent_given",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "company_name": forms.TextInput(attrs={"placeholder": "Agency / company name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@company.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 00000 00000"}),
            "city_country": forms.TextInput(attrs={"placeholder": "City, Country"}),
            "travel_start_date": forms.DateInput(attrs={"type": "date"}),
            "travel_end_date": forms.DateInput(attrs={"type": "date"}),
            "guests": forms.NumberInput(attrs={"placeholder": "e.g. 24", "min": "1"}),
            "tour_type": forms.Select(),
            "hotel_category": forms.Select(),
            "transport": forms.Select(),
            "requirements": forms.Textarea(attrs={"placeholder": "Tell us about nights, rooms, meals, guide language, pickup city or any special request.", "rows": 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("travel_start_date")
        end = cleaned_data.get("travel_end_date")
        if start and end and end < start:
            self.add_error("travel_end_date", "End date cannot be before start date.")
        return cleaned_data

    def clean_destinations(self):
        return ", ".join(self.cleaned_data["destinations"])
