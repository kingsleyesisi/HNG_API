from django.db import models


class Info(models.Model):
    email = models.EmailField(max_length=30)
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return super().__str__()