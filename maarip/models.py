from django.db import models
from django.template.defaultfilters import slugify
from datetime import *



class Slider(models.Model):
    title               = models.CharField(max_length=128)
    image               = models.TextField()
    subtitle            = models.TextField()

    class Meta:
        verbose_name = 'Slider'

    def __str__(self):
        return self.title


















class MaaripCategory(models.Model):
    maaripCategory          = models.CharField(max_length=200, blank=True, null=True)
    slug                    = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.maaripCategory

    def save(self, *args, **kwargs):
        self.slug = slugify(self.maaripCategory)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Maarip Category'



class Maarip(models.Model):
    name                    = models.CharField(max_length=200, blank=True, null=True)
    category                = models.ManyToManyField(MaaripCategory)
    maarip_image            = models.ImageField(upload_to='maarip_image/', blank=True, null=True)
    maarip_Video            = models.FileField(upload_to='maarip_Video/', blank=True, null=True)
    description             = models.TextField()
    active                  = models.BooleanField()
    publicatetime           = models.DateTimeField(auto_now_add=False)
    slug                    = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

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
        verbose_name = 'Maarip'
        verbose_name_plural = 'Maarip'
        ordering = ["-publicatetime"]











class ContactUs(models.Model):
    name                = models.CharField(max_length=64, null=True, blank=True)
    surname             = models.CharField(max_length=64, null=True, blank=True)
    phone               = models.CharField(max_length=16, null=True, blank=True)
    email               = models.EmailField(null=False, blank=True)
    subject             = models.CharField(max_length=64, null=True, blank=True)
    description         = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.subject}-{self.phone}'
