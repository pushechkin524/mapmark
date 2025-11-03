from django.db import models

class Marker(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Marker {self.id}"

class Photo(models.Model):
    marker = models.ForeignKey(Marker, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='markers/')
    order = models.PositiveSmallIntegerField(default=0)
