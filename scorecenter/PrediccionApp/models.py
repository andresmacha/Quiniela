from django.db import models

# Create your models here.

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class Juego(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    equipoa = models.CharField(max_length=135, db_column='EquipoA') # Field name made lowercase.
    equipob = models.CharField(max_length=135, db_column='EquipoB') # Field name made lowercase.
    resultadoa = models.IntegerField(null=True, db_column='ResultadoA', blank=True) # Field name made lowercase.
    resultadob = models.IntegerField(null=True, db_column='ResultadoB', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'juego'
        
class TipoResultado(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    nombre = models.CharField(max_length=135, db_column='Nombre') # Field name made lowercase.
    valor = models.IntegerField(db_column='Valor') # Field name made lowercase.
    class Meta:
        db_table = u'tipo_resultado'

class Usuario(models.Model):
    # id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    nombre = models.CharField(max_length=135, db_column='Nombre') # Field name made lowercase.
    fechanacimiento = models.DateField(null=True, db_column='FechaNacimiento', blank=True) # Field name made lowercase.
    nombreusuario = models.CharField(max_length=135, db_column='NombreUsuario') # Field name made lowercase.
    clave = models.CharField(max_length=135, db_column='Clave') # Field name made lowercase.
    class Meta:
        db_table = u'usuario'

class Prediccion(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    idusuario = models.ForeignKey(AuthUser, db_column='IdUsuario') # Field name made lowercase.
    idjuego = models.ForeignKey(Juego, db_column='IdJuego') # Field name made lowercase.
    equipoa = models.IntegerField(null=True, db_column='EquipoA', blank=True) # Field name made lowercase.
    equipob = models.IntegerField(null=True, db_column='EquipoB', blank=True) # Field name made lowercase.
    resultado = models.ForeignKey(TipoResultado, null=True, db_column='Resultado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'prediccion'