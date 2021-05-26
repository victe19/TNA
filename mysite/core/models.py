
from django.db import models
from .validators import validate_file_extension
from django.core.validators import MaxValueValidator, MinValueValidator


class File(models.Model):
    file = models.FileField(validators=[validate_file_extension])
    subject = models.CharField(max_length=15)
    prof = models.CharField(max_length=20)
    day = models.IntegerField(validators=[MaxValueValidator(31),MinValueValidator(1)])
    month = models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])


    def __str__(self):
        return self  # ?

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
