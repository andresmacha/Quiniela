# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

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

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class Juego(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    equipoa = models.CharField(max_length=135, db_column='EquipoA') # Field name made lowercase.
    equipob = models.CharField(max_length=135, db_column='EquipoB') # Field name made lowercase.
    resultadoa = models.IntegerField(null=True, db_column='ResultadoA', blank=True) # Field name made lowercase.
    resultadob = models.IntegerField(null=True, db_column='ResultadoB', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'juego'

class Prediccion(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    idusuario = models.ForeignKey(authuser, db_column='id') # Field name made lowercase.
    idjuego = models.ForeignKey(Juego, db_column='IdJuego') # Field name made lowercase.
    equipoa = models.IntegerField(null=True, db_column='EquipoA', blank=True) # Field name made lowercase.
    equipob = models.IntegerField(null=True, db_column='EquipoB', blank=True) # Field name made lowercase.
    resultado = models.ForeignKey(TipoResultado, null=True, db_column='Resultado', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'prediccion'

class TipoResultado(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    nombre = models.CharField(max_length=135, db_column='Nombre') # Field name made lowercase.
    valor = models.IntegerField(db_column='Valor') # Field name made lowercase.
    class Meta:
        db_table = u'tipo_resultado'

class Usuario(models.Model):
    #id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    nombre = models.CharField(max_length=135, db_column='Nombre') # Field name made lowercase.
    fechanacimiento = models.DateField(null=True, db_column='FechaNacimiento', blank=True) # Field name made lowercase.
    nombreusuario = models.CharField(max_length=135, db_column='NombreUsuario') # Field name made lowercase.
    clave = models.CharField(max_length=135, db_column='Clave') # Field name made lowercase.
    class Meta:
        db_table = u'usuario'

