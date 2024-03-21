# users/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add more fields as needed

    def __str__(self):
        return self.username
class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_rental_bill = models.DecimalField(max_digits=10, decimal_places=2)
    due = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    month = models.DateField(default=datetime.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        # Calculate total_rental_bill before saving
        self.total_rental_bill = self.calculate_total_rental_bill()
        super().save(*args, **kwargs)

    def calculate_total_rental_bill(self):
        total_electricity_bill = 0
        # Iterate over all electricity instances associated with the user
        for electricity_instance in self.user.electricity_set.all():
            total_electricity_bill += electricity_instance.total_electricity_bill
        return self.rent_amount + total_electricity_bill

class Electricity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    previous_month_bill = models.DecimalField(max_digits=10, decimal_places=2)
    present_month_bill = models.DecimalField(max_digits=10, decimal_places=2)
    consumed_units = models.DecimalField(max_digits=10, decimal_places=2)
    per_unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_electricity_bill = models.DecimalField(max_digits=10, decimal_places=2, default = 0)

    def save(self, *args, **kwargs):
        self.total_electricity_bill = self.consumed_units * self.per_unit_cost
        super(Electricity, self).save(*args, **kwargs)
