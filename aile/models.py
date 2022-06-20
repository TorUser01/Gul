from django.db import models
from django.template.defaultfilters import slugify
from datetime import *



class AileCategory(models.Model):
    aileCategory        = models.CharField(max_length=200, blank=True, null=True)
    slug                = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.aileCategory

    def save(self, *args, **kwargs):
        self.slug = slugify(self.aileCategory)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Aile Category'


class Aile(models.Model):
    name                = models.CharField(max_length=200, blank=True, null=True)
    category            = models.ForeignKey(AileCategory, on_delete=models.CASCADE, related_name='Aile_Category')
    aile_image          = models.ImageField(upload_to='aile_image/', blank=True, null=True)
    aile_Video          = models.FileField(upload_to='aile_Video/', blank=True, null=True)
    description         = models.TextField()
    active              = models.BooleanField()
    publicatetime       = models.DateTimeField(auto_now_add=False)
    slug                = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def Is_Past(self):
        today = date.today()
        if self.publicatetime.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing


    class Meta:
        verbose_name = 'Aile'
        verbose_name_plural = 'Aile'
        ordering = ["-publicatetime"]