from django.db import models


class ConcreteModel(models.Model):
    pass


class AbstractModel(models.Model):
    foreign_key = models.ForeignKey('ConcreteModel')

    class Meta:
        abstract = True
