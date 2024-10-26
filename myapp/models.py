# models.py
from django.db import models

class LeaveRequest(models.Model):
    employee = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'En attente'), ('approved', 'Approuvé'), ('rejected', 'Rejeté')])
    
    def __str__(self):
        return f"{self.employee} - {self.leave_type} - {self.status}"
