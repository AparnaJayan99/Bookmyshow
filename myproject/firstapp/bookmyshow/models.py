from django.db import models

# Create your models here.
class Book(models.Model):
    t_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    phone_no = models.IntegerField()
    showtime = models.CharField(max_length=50)

    class Meta:
        db_table = "book"