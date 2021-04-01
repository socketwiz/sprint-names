from django.db import models


class Names(models.Model):
    author = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(max_length=255)
    used = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    used_at = models.DateField(null=True)

    def __str__(self):
        return self.name
