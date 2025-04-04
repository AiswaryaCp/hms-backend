from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_mrn = models.CharField(max_length=30, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.patient_mrn:
            last_patient = Patient.objects.order_by('-id').first()
            last_mrn_number = int(last_patient.patient_mrn[3:]) if last_patient and last_patient.patient_mrn else 1000
            self.patient_mrn = f"MRN{last_mrn_number + 1}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_mrn} - {self.first_name} {self.last_name}"