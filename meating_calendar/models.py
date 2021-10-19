from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta


class Accounts(models.Model):
    name = models.CharField(max_length=150, default="")
    email = models.EmailField(max_length=150, unique=True, default="")
    _id = models.PositiveIntegerField(
        validators=[MinValueValidator(0000), MaxValueValidator(9999)],
        default=1000,
        unique=True,
    )

    def __str__(self):
        return f"{self.name}-{self._id}"


class Meating_room(models.Model):
    building = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    floor = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    room = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"B{self.building}-F{self.floor}-R{self.room}"


class Meating(models.Model):
    meating_status = (
        ("now", "meating is active"),
        ("end", "meating end"),
        ("soon", "meating in future"),
    )
    title = models.CharField(max_length=120)
    manager = models.ForeignKey(
        "Accounts", on_delete=models.CASCADE, blank=False, default=1
    )
    long_meaning_by_days = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    long_meaning_by_hours = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    s_time = models.DateTimeField(blank=False)
    e_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        choices=meating_status, max_length=50, default=meating_status[2]
    )
    room = models.ForeignKey(
        Meating_room, on_delete=models.CASCADE, blank=False, default=1
    )

    def save(self, *args, **kwargs):

        self.e_time = self.s_time + timedelta(
            hours=self.long_meaning_by_hours, days=self.long_meaning_by_days
        )
        print(self.status)
        super(Meating, self).save(*args, **kwargs)

    def now(self):
        return self.s_time <= datetime.datetime.now() < self.e_time

    def __str__(self):
        return self.title
