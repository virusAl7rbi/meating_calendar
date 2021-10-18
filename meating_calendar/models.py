from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


class Accounts(models.Model):
    name = models.CharField(max_length=150,default="")
    email = models.EmailField(max_length=150, unique=True,default="")
    _id = models.PositiveIntegerField(validators=[MinValueValidator(0000), MaxValueValidator(9999)],default=1000,unique=True)

    def __str__(self):
        return f"{self.name}-{self._id}"


class Meating(models.Model):
    meating_status = (
        ("now", "meating is now"),
        ("end", "meating end"),
        ("soon", "meating in future"),
    )
    title = models.CharField(max_length=120)
    manager = models.ForeignKey('Accounts', on_delete=models.CASCADE, null=False, blank=False, default=1)
    long_meaning_by_days = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    long_meaning_by_hours = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    s_time = models.DateTimeField(null=False, blank=False)
    e_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        choices=meating_status, max_length=50, default=meating_status[2]
    )
    building_choices = (("1", (("1", "building 1"), ("2", "building 2"))),)
    room = models.CharField(choices=building_choices, max_length=50, default="")

    def save(self, *args, **kwargs):
        self.e_time = self.s_time + timedelta(
            hours=self.long_meaning_by_hours, days=self.long_meaning_by_days
        )
        super(Meating, self).save(*args, **kwargs)

    def __str__(self):
        return self.title