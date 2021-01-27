from django.db import models
from django.contrib.postgres.fields import JSONField


class Information(models.Model):
    info = JSONField()

    def __str__(self):
        return str(self.info)
