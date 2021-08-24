from django.db import models


# Create your models here.


class Dispatcher(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class OwnerOperator(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, null=True, blank=True)
    track_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class InvoiceStatus(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    dispatcher = models.ForeignKey(Dispatcher, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(OwnerOperator, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    dh = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    origin = models.CharField(max_length=255)
    milage = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    destination = models.CharField(max_length=255)
    trip_rate = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    notes = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE, default=InvoiceStatus.objects.first().pk)

    def __str__(self):
        return self.board.name
