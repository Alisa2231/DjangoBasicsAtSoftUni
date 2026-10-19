from django.db import models


class Countries(models.TextChoices):
    BG = "BG", "Bulgaria"
    UK = "UK", "United Kingdom"
    DE = "DE", "Germany"
    FR = "FR", "France"
    PT = 'PT', 'Portugal'
    OTHER = "OTHER", "Other"