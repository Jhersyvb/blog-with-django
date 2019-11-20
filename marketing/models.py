from django.db import models


class Signup(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.email
