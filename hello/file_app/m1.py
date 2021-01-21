# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asignacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='idunidad')
    nombre = models.CharField(max_length=120)
    tipoasignacion = models.IntegerField()
    fechaapertura = models.DateField()
    fechacierre = models.DateField()
    fechacreacion = models.DateTimeField()
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion'


class AuxIndicativos(models.Model):
    departamento = models.CharField(primary_key=True, max_length=-1)
    ciudad = models.CharField(max_length=-1)
    indicativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aux_indicativos'
        unique_together = (('departamento', 'ciudad'),)


class Baseasignacion(models.Model):
    idasignacion = models.ForeignKey(Asignacion, models.DO_NOTHING, db_column='idasignacion')
    identificacion = models.CharField(max_length=30)
    obligacion = models.CharField(max_length=30)
    diasmora = models.IntegerField()
    saldocapital = models.FloatField()
    saldomora = models.FloatField()
    saldocobrar = models.FloatField()
    concatenacion = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'baseasignacion'
        unique_together = (('obligacion', 'identificacion', 'idasignacion'),)


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nombredb = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    schema_name = models.CharField(max_length=-1, blank=True, null=True)
    logo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Clienteusuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    idusuario = models.BigIntegerField()
    idcliente = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'clienteusuario'


class DefinicionTokens(models.Model):
    id = models.BigAutoField()
    token = models.CharField(max_length=-1)
    tipo_conversacion = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'definicion_tokens'


class HerramientasLimite(models.Model):
    limite_id = models.AutoField(primary_key=True)
    unidad_id = models.IntegerField()
    herramienta = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    fecha_limite = models.DateField()

    class Meta:
        managed = False
        db_table = 'herramientas_limite'


class HerramientasProcesos(models.Model):
    herramienta = models.BooleanField()
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'herramientas_procesos'


class IndicadoresGeneral(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=-1, blank=True, null=True)
    indicador = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'indicadores_general'
        unique_together = (('id', 'indicador'),)


class Indicativos(models.Model):
    ciudad_depto = models.CharField(max_length=255)
    indicativo_bpo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indicativos'


class Indicators(models.Model):
    unit_id = models.CharField(primary_key=True, max_length=-1)
    user_id = models.CharField(max_length=-1)
    full_name = models.CharField(max_length=-1, blank=True, null=True)
    unit_name = models.CharField(max_length=-1, blank=True, null=True)
    customer_name = models.CharField(max_length=-1, blank=True, null=True)
    fec = models.DateField()
    contacts = models.IntegerField(blank=True, null=True)
    commitment_port = models.IntegerField(blank=True, null=True)
    commitment_sales = models.IntegerField(blank=True, null=True)
    calls = models.IntegerField(blank=True, null=True)
    pause_sec = models.IntegerField(blank=True, null=True)
    break_field = models.IntegerField(db_column='break', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    active_pause = models.IntegerField(blank=True, null=True)
    restroom = models.IntegerField(blank=True, null=True)
    failure = models.IntegerField(blank=True, null=True)
    cons_coord = models.IntegerField(blank=True, null=True)
    lunch = models.IntegerField(blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    front = models.IntegerField(blank=True, null=True)
    folder = models.IntegerField(blank=True, null=True)
    training = models.IntegerField(blank=True, null=True)
    feedback = models.IntegerField(blank=True, null=True)
    marking = models.IntegerField(blank=True, null=True)
    nxdial = models.IntegerField(blank=True, null=True)
    co = models.IntegerField(blank=True, null=True)
    pause = models.IntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    typing = models.IntegerField(blank=True, null=True)
    wait_sec = models.IntegerField(blank=True, null=True)
    talk_sec = models.IntegerField(blank=True, null=True)
    dispo_sec = models.IntegerField(blank=True, null=True)
    dead_sec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicators'
        unique_together = (('unit_id', 'user_id', 'fec'),)


class Metas(models.Model):
    tipo = models.CharField(max_length=255)
    unidad = models.ForeignKey('Unidad', models.DO_NOTHING)
    llamadas = models.IntegerField(blank=True, null=True)
    clientes = models.IntegerField(blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    compromisos = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metas'


class ModulosWiser(models.Model):
    modulo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'modulos_wiser'


class NotificacionesWiser(models.Model):
    usuario = models.ForeignKey('UsuariosWiser', models.DO_NOTHING)
    is_read = models.BooleanField()
    is_hidden = models.BooleanField()
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notificaciones_wiser'


class Pagos(models.Model):
    pago_id = models.BigAutoField(primary_key=True)
    deudor_identificacion = models.CharField(max_length=100, blank=True, null=True)
    obligacion_id = models.CharField(max_length=100, blank=True, null=True)
    pago_valor = models.BigIntegerField(blank=True, null=True)
    pago_fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'


class PerfilesWiser(models.Model):
    perfil = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'perfiles_wiser'


class PermisosWiser(models.Model):
    perfil = models.ForeignKey(PerfilesWiser, models.DO_NOTHING)
    modulo = models.ForeignKey(ModulosWiser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permisos_wiser'


class Productividad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    clientes = models.IntegerField()
    contactos = models.IntegerField(blank=True, null=True)
    compromisos = models.IntegerField(blank=True, null=True)
    llamadas = models.IntegerField(blank=True, null=True)
    conversion1 = models.CharField(max_length=255, blank=True, null=True)
    conversion2 = models.CharField(max_length=255, blank=True, null=True)
    vicidial = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'productividad'
        unique_together = (('id', 'fecha'),)


class ResultadoLlamada(models.Model):
    id_resultado = models.BigAutoField()
    id_asignacion = models.BigIntegerField()
    identificacion = models.CharField(max_length=-1)
    tipificacion = models.CharField(max_length=-1)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resultado_llamada'


class SesionesWiser(models.Model):
    sesion_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('UsuariosWiser', models.DO_NOTHING)
    tipo = models.TextField()  # This field type is a guess.
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'sesiones_wiser'


class Telefono(models.Model):
    id = models.BigAutoField(primary_key=True)
    idasignacion = models.BigIntegerField()
    identificacion = models.CharField(max_length=30)
    numerotelefono = models.CharField(max_length=30)
    fechacreacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'telefono'


class Unidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente')
    nombre = models.CharField(max_length=150)
    fechacreacion = models.DateTimeField()
    vicidial = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad'


class Unidadusuario(models.Model):
    idusuario = models.BigIntegerField()
    idunidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidadusuario'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuariowin = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    extension = models.CharField(max_length=15, blank=True, null=True)
    cedula = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuariosWiser(models.Model):
    nombre = models.CharField(max_length=255)
    perfil = models.ForeignKey(PerfilesWiser, models.DO_NOTHING)
    password = models.CharField(max_length=255)
    estado = models.BooleanField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    vicidial = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_wiser'
