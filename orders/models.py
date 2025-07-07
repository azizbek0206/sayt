from django.db import models
from menu.models import MenuItem

class Order(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"
