from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class Gestiones(models.Model):
    gestion_id = models.BigAutoField(primary_key=True)
    tarea_id = models.BigIntegerField()
    gestion_fecha = models.DateTimeField(auto_now_add=True)
    usuario_id = models.CharField(max_length=50)
    deudor_id = models.CharField(max_length=250)
    asignacion_id = models.BigIntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    canal = models.CharField(max_length=20)
    id_tipificacion = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    nom_contacto_tercero = models.CharField(max_length=250, blank=True, null=True)
    tel_adicional = models.BigIntegerField(blank=True, null=True)
    ciudad_tel_adicional = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestiones'

class Tipificaciones(models.Model):
    codigo01 = models.IntegerField()
    codigo02 = models.IntegerField()
    codigo03 = models.IntegerField()
    codigo04 = models.IntegerField()
    codigo05 = models.IntegerField()
    codigo06 = models.IntegerField()
    codigo07 = models.IntegerField()
    codigo08 = models.IntegerField()
    codigo09 = models.IntegerField()
    codigo10 = models.IntegerField()
    prioridad = models.IntegerField(blank=True, null=True)
    indicador = models.IntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipificaciones'
        unique_together = (('codigo01', 'codigo02', 'codigo03', 'codigo04', 'codigo05', 'codigo06', 'codigo07', 'codigo08', 'codigo09', 'codigo10', 'unidad'),)


class Codigos(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codigos'
        unique_together = (('codigo', 'unidad'),)

class NombreRama(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nombre_rama'
        unique_together = (('id', 'unidad'),)

class Tareas(models.Model):
    tarea_id = models.BigAutoField(primary_key=True)
    tarea_fecha_creacion = models.DateTimeField(auto_now_add=True)
    unidad_id = models.BigIntegerField()
    registros = models.BigIntegerField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    list_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'

class Asignaciones(models.Model):
    asignacion_id = models.BigIntegerField(primary_key=True)
    unidad = models.ForeignKey('Unidad', models.DO_NOTHING)
    asignacion_nombre = models.CharField(max_length=100)
    asignacion_fecha_creacion = models.DateField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    estado = models.BooleanField()
    fecha_apertura = models.DateField()

    class Meta:
        managed = False
        db_table = 'asignaciones'

class Unidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='idcliente')
    nombre = models.CharField(max_length=150)
    fechacreacion = models.DateTimeField()
    vicidial = models.CharField(max_length=120, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad'

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nombredb = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    schema_name = models.CharField(max_length=150, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    user_group = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

class IndicadoresGeneral(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    indicador = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'indicadores_general'
        unique_together = (('id', 'indicador'),)

class VicidialPause(models.Model):
    id = models.IntegerField(blank=True, null=True)
    pause = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'vicidial_pause'

class TipificacionesHerramientas(models.Model):
    id = models.IntegerField(primary_key=True)
    herramienta = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tipificaciones_herramientas'
        unique_together = (('id', 'herramienta'),)

class UsuariosWiser(models.Model):
    nombre = models.CharField(max_length=255)
    perfil = models.ForeignKey('PerfilesWiser', models.DO_NOTHING)
    password = models.CharField(max_length=255)
    estado = models.BooleanField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    vicidial = models.CharField(max_length=150, blank=True, null=True)
    password_expiration = models.DateField(blank=True, null=True)
    restore_password = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_wiser'

class PerfilesWiser(models.Model):
    perfil = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'perfiles_wiser'

class CampaingList(models.Model):
    id_list = models.BigAutoField(primary_key=True)
    campaing_name = models.CharField(max_length=100, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    campaing_type = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'campaing_list'