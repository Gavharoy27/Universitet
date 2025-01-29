from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length = 100)
    aktiv = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Yonalish'
        verbose_name_plural = 'Yonalishlar'

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length = 100)
    yonalish = models.ForeignKey(Yonalish, on_delete = models.CASCADE)
    asosiy = models.CharField(max_length = 200)

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'

    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length = 5, choices = (('Erkak', 'Erkak'), ('Ayol', 'Ayol')))
    daraja = models.CharField(max_length = 15, choices = (('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr')))
    fan = models.ForeignKey(Fan, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Ustoz'
        verbose_name_plural = 'Ustozlar'
 
    def __str__(self):
        return self.ism