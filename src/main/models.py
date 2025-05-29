from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    date = models.DateTimeField(verbose_name="Vaqti")
    # Boshqa kerakli maydonlarni qo'shishingiz mumkin

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    address = models.TextField(verbose_name="Manzil")
    # Boshqa kerakli maydonlarni qo'shishingiz mumkin

    def __str__(self):
        return self.name