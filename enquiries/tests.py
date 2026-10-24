from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Enquiry


class HomeViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Request B2B Quote")
        self.assertContains(response, "Bodh Gaya")

    def test_gallery_manifest_lists_each_destination(self):
        response = self.client.get(reverse("gallery_manifest"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            set(response.json()),
            {"bodh-gaya", "rajgir", "nalanda", "vaishali & Kesariya"},
        )

    def test_valid_enquiry_is_saved(self):
        start = date.today() + timedelta(days=30)
        response = self.client.post(
            reverse("home"),
            {
                "name": "Asha Sharma",
                "company_name": "Example Tours",
                "email": "asha@example.test",
                "phone": "+91 98765 43210",
                "city_country": "Delhi, India",
                "travel_start_date": start.isoformat(),
                "travel_end_date": (start + timedelta(days=4)).isoformat(),
                "guests": 18,
                "destinations": ["Bodh Gaya", "Rajgir", "Nalanda"],
                "tour_type": "Group",
                "hotel_category": "3-star",
                "transport": "Tempo Traveller",
                "requirements": "Need twin rooms, breakfast and an English-speaking guide.",
                "consent_given": "on",
            },
        )
        self.assertRedirects(response, f"{reverse('home')}#enquiry")
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.get()
        self.assertEqual(enquiry.company_name, "Example Tours")
        self.assertEqual(enquiry.destinations, "Bodh Gaya, Rajgir, Nalanda")
