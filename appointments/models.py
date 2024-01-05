from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from datetime import date, datetime, timedelta

class Appointment(models.Model):
    speciality = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Add 45 minutes to start_time to calculate end_time
        if self.time and not self.end_time:
            end_time = (datetime.combine(date.today(), self.time) + timedelta(minutes=45)).time()
            self.end_time = end_time
        super().save(*args, **kwargs)
    
    patient = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="doctor_appointed"
    )
    doctor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="booked_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"By: {self.patient.first_name} for Dr. {self.doctor.first_name}"

    def get_absolute_url(self):
        return reverse("view_details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("-created_at",)
