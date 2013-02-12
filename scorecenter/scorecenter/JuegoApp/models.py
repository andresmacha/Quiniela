from django.db import models
from django.shortcuts import render_to_response

# Create your models here.
class Juego(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    equipoa = models.CharField(max_length=135, db_column='EquipoA') # Field name made lowercase.
    equipob = models.CharField(max_length=135, db_column='EquipoB') # Field name made lowercase.
    resultadoa = models.IntegerField(null=True, db_column='ResultadoA', blank=True) # Field name made lowercase.
    resultadob = models.IntegerField(null=True, db_column='ResultadoB', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'juego'