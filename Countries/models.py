from django.db import models

class CountrySelection(models.Model):
    COUNTRY_CHOICES = [
        ("Nigeria", "Nigeria"),
        ("United States", "United States"),
        ("United Kingdom", "United Kingdom"),
        ("Canada", "Canada"),
        ("Eritrea", "Eritrea"),
        ("Germany", "Germany"),
        ("France", "France"),
        ("Australia", "Australia"),
        ("Japan", "Japan"),
        ("South Korea", "South Korea"),
        ("South Africa", "South Africa"),
        ("Brazil", "Brazil"),
        ("Italy", "Italy"),
        ("Singapore", "Singapore"),
        ("Switzerland", "Switzerland"),
        ("New Zealand", "New Zealand"),
        ("Mexico", "Mexico"),
        ("Russia", "Russia"),
        ("Turkey", "Turkey"),
        ("Malaysia", "Malaysia"),
        ("Saudi Arabia", "Saudi Arabia"),
        ("Belgium", "Belgium")
    ]
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    guest_id = models.CharField(max_length=255)
    
