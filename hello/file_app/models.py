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

# class BogotaSms(models.Model):
#     telefono = models.BigIntegerField(blank=True, null=True)
#     fecha = models.DateTimeField(blank=True, null=True)
#     estado = models.BooleanField(blank=True, null=True)
#     cedula = models.BigIntegerField(blank=True, null=True)
#     mensaje = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'bogota_sms'
#         unique_together = (('telefono', 'fecha', 'estado', 'cedula', 'mensaje'),)

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

    class Meta:
        managed = False
        db_table = 'tipificaciones'
        unique_together = (('codigo01', 'codigo02', 'codigo03', 'codigo04', 'codigo05', 'codigo06', 'codigo07', 'codigo08', 'codigo09', 'codigo10'),)


class Codigos(models.Model):
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'codigos'

class NombreRama(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nombre_rama'

class Tareas(models.Model):
    tarea_id = models.BigAutoField(primary_key=True)
    tarea_fecha_creacion = models.DateTimeField(auto_now_add=True)
    unidad_id = models.BigIntegerField()
    registros = models.BigIntegerField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'

class Asignaciones(models.Model):
    asignacion_id = models.BigIntegerField(primary_key=True)
    unidad = models.ForeignKey('Unidades', models.DO_NOTHING)
    asignacion_nombre = models.CharField(max_length=100)
    asignacion_fecha_creacion = models.DateField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    estado = models.BooleanField()
    fecha_apertura = models.DateField()

    class Meta:
        managed = False
        db_table = 'asignaciones'

class Unidades(models.Model):
    unidad_id = models.BigIntegerField(primary_key=True)
    unidad_nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    unidad_estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'