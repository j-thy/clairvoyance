from django.db import models


class Event(models.Model):
    slug = models.CharField(max_length=200, blank=True, default='', primary_key=True)
    name = models.CharField(max_length=200, blank=True, default='')
    region = models.CharField(max_length=200, blank=True, default='')
    image_file = models.CharField(max_length=200, blank=True, default='')

    # Use after_import to check what images need to be copied over and copy it over from the scripts folder

    def __str__(self):
        return self.name

class Banner(models.Model):
    slug = models.CharField(max_length=200, blank=True, default='', primary_key=True)
    name = models.CharField(max_length=200, blank=True, default='')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, default='')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Servant(models.Model):
    id_num = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200, blank=True, default='')
    name = models.CharField(max_length=200, blank=True, default='')
    jp_rateups = models.ManyToManyField(Banner, related_name='jp_rateups')
    na_rateups = models.ManyToManyField(Banner, related_name='na_rateups')

    def __str__(self):
        return self.name
