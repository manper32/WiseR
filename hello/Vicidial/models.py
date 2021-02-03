from django.db import models

class VicidialStatusValidator(models.Model):
    status = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    call_type = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vicidial_status_validator'
