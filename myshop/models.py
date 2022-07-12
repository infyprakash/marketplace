from django.db import models
from oscar.apps.partner.models import Partner
# Create your models here.

class FbChatModel(models.Model):
    partner = models.ForeignKey(Partner,on_delete=models.CASCADE)
    code = models.TextField()
