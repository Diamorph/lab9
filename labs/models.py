from django.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length = 30)
    rate = models.IntegerField(default = 0)
    check = models.FloatField(default = 0)
    city = models.CharField(max_length = 30)
    date = models.DateField()
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    def dict(self):
        return {
            'name': self.name,
            'rate': self.rate,
            'check' : self.check,
            'city': self.city,
            'id': self.id,
            'image': self.image.url,
        }