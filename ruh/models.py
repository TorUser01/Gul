from django.db import models
from django.template.defaultfilters import slugify
from datetime import *

class RuhCategory(models.Model):
    ruhCategory        = models.CharField(max_length=200, blank=True, null=True)
    slug                = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.ruhCategory

    def save(self, *args, **kwargs):
        self.slug = slugify(self.ruhCategory)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Ruh Category'



class Ruh(models.Model):
    name                = models.CharField(max_length=200, blank=True, null=True)
    title               = models.CharField(max_length=200, blank=True, null=True)
    solution1           = models.CharField(max_length=200, blank=True, null=True)
    solution2           = models.CharField(max_length=200, blank=True, null=True)
    solution3           = models.CharField(max_length=200, blank=True, null=True)
    subject             = models.TextField()
    category            = models.ForeignKey(RuhCategory, on_delete=models.CASCADE, blank=True, null=True)
    ruh_image1          = models.ImageField(upload_to='ruh_image/', blank=True, null=True)
    ruh_image2          = models.ImageField(upload_to='ruh_image/', blank=True, null=True)
    ruh_Video           = models.FileField(upload_to='ruh_video/', blank=True, null=True)
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
        verbose_name = 'Ruh'
        verbose_name_plural = 'Ruh'
        ordering = ["-publicatetime"]



class FAQS(models.Model):
    ruh                     = models.ForeignKey(Ruh, on_delete=models.CASCADE, blank=True, null=True)
    question                =models.CharField(max_length=200, blank=True, null=True)
    answer                  = models.TextField()

    def __str__(self):
        return self.question


    class Meta:
        verbose_name_plural = 'Question&Answer'
