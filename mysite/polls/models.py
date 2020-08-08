from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Capitan(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.IntegerField()

    class Meta:
        verbose_name = _("Capitan")
        verbose_name_plural = _("Capitanes")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Capitan_detail", kwargs={"pk": self.pk})


class Lider(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.IntegerField()
    capitan = models.ForeignKey(Capitan, on_delete=models.PROTECT)


    class Meta:
        verbose_name = _("Lider")
        verbose_name_plural = _("Lideres")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Lider_detail", kwargs={"pk": self.pk})

class Municipio(models.Model):

    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Municipio")
        verbose_name_plural = _("Municipios")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Municipio_detail", kwargs={"pk": self.pk})

class Comuna(models.Model):

    name = models.CharField(max_length=100)  
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    capitanes = models.ManyToManyField(Capitan)

    class Meta:
        verbose_name = _("Comuna")
        verbose_name_plural = _("Comunas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comuna_detail", kwargs={"pk": self.pk})

class PuestosDeVotacion(models.Model):

    nombres = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("PuestosDeVotacion")
        verbose_name_plural = _("PuestosDeVotacions")

    def __str__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse("PuestosDeVotacion_detail", kwargs={"pk": self.pk})


class Barrio(models.Model):

    nombre = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Barrio")
        verbose_name_plural = _("Barrios")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Barrio_detail", kwargs={"pk": self.pk})


class DatosDelVolante(models.Model):

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=100)
    cedula = models.CharField(max_length=100)
    mesa = models.CharField(max_length=100)
    lider = models.ForeignKey(Lider, on_delete=models.PROTECT)
    barrio = models.ForeignKey(Barrio, on_delete=models.PROTECT)
    puesto_votacion = models.ForeignKey(PuestosDeVotacion, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("DatosDelVolante")
        verbose_name_plural = _("DatosDelVolantes")

    def __str__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse("DatosDelVolante_detail", kwargs={"pk": self.pk})



class LiderRespBarrio(models.Model):

    lider = models.ForeignKey(Lider, on_delete=models.PROTECT)
    capitan_comuna = models.ForeignKey(Capitan, on_delete=models.PROTECT)
    barrio = models.ForeignKey(Barrio, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("liderRespBarrio")
        verbose_name_plural = _("liderRespBarrio")

    def __str__(self):
        return f"{self.lider} → {self.capitan_comuna} → {self.barrio}"

    def get_absolute_url(self):
        return reverse("LiderRespBarrio_detail", kwargs={"pk": self.pk})
