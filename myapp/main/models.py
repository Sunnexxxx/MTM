from django.db import models


class Human(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.PositiveIntegerField('Age')

    class Meta:
        abstract = True
        ordering = ['-id']


class Parent(Human):

    def __str__(self):
        return '{} - {}'.format(self.name, self.surname)


class Kid(Human):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.surname, self.parent)


class Shop(models.Model):
    name = models.CharField('Shop name', max_length=50)
    icecream = models.ManyToManyField('Icecream')

    def __str__(self):
        return '{} - {}'.format(self.name, self.icecream.all())


class Icecream(models.Model):
    name = models.CharField('Label', max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
