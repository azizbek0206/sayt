from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class RestaurantInfo(models.Model):
    """Restaurant asosiy ma'lumotlari"""
    name = models.CharField(max_length=100, verbose_name="Restoran nomi")
    description = models.TextField(verbose_name="Tavsif")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Manzil")
    working_hours = models.CharField(max_length=100, verbose_name="Ish vaqti")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram")
    telegram_url = models.URLField(blank=True, null=True, verbose_name="Telegram")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Restoran ma'lumoti"
        verbose_name_plural = "Restoran ma'lumotlari"

    def __str__(self):
        return self.name