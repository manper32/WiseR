# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseTarea(models.Model):
    base_tarea_id = models.BigIntegerField(primary_key=True)
    tarea_id = models.BigIntegerField()
    deudor_id = models.CharField(max_length=100)
    obligacion_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'base_tarea'


class BasesAsignacion(models.Model):
    base_asignacion_id = models.BigIntegerField(primary_key=True)
    asignacion = models.ForeignKey(Asignaciones, models.DO_NOTHING)
    base_asignacion_nombre = models.CharField(max_length=-1)
    fecha_carge = models.DateTimeField()
    deudores = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    deudores_nuevos = models.BigIntegerField()
    obligaciones_nuevas = models.BigIntegerField()
    deudores_salientes = models.BigIntegerField()
    obligaciones_salientes = models.BigIntegerField()
    tipo_archivo = models.CharField(max_length=-1)
    tipo_ingreso = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bases_asignacion'


class BogotaSms(models.Model):
    telefono = models.BigIntegerField(primary_key=True)
    fecha = models.DateTimeField()
    estado = models.BooleanField()
    cedula = models.BigIntegerField()
    mensaje = models.CharField(max_length=-1)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bogota_sms'
        unique_together = (('telefono', 'fecha', 'estado', 'cedula', 'mensaje'),)


class CamposObligatorios(models.Model):
    id_campo = models.IntegerField(primary_key=True)
    campo_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'campos_obligatorios'


class Codigos(models.Model):
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'codigos'


class Compromisos(models.Model):
    deudor_id = models.CharField(primary_key=True, max_length=-1)
    obligacion_id = models.CharField(max_length=-1)
    valor = models.BigIntegerField()
    fecha_compromiso = models.DateField()
    fecha_pago = models.DateField()
    asesor = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'compromisos'
        unique_together = (('deudor_id', 'obligacion_id', 'valor', 'fecha_compromiso', 'fecha_pago', 'asesor'),)


class ConsAsignacion(models.Model):
    asignacion_id = models.BigIntegerField(primary_key=True)
    fecha_registro = models.DateField()
    obligacion_id = models.CharField(max_length=-1)
    unidad_nombre = models.CharField(max_length=-1)
    fecha_cargue = models.DateTimeField()
    estado = models.CharField(max_length=-1)
    deudor_id = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'cons_asignacion'
        unique_together = (('asignacion_id', 'fecha_registro', 'obligacion_id'),)


class Correos(models.Model):
    correo = models.CharField(primary_key=True, max_length=255)
    deudor_id = models.CharField(max_length=100)
    correo_id = models.BigIntegerField()
    correo_estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'correos'
        unique_together = (('correo', 'deudor_id'),)


class DatosAdicionales(models.Model):
    dato_adicional_id = models.BigIntegerField(primary_key=True)
    obligacion = models.ForeignKey('Obligaciones', models.DO_NOTHING)
    campo_archivo_nombre = models.CharField(max_length=255)
    campo_archivo_valor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_adicionales'


class Deudores(models.Model):
    deudor_id = models.CharField(primary_key=True, max_length=100)
    deudor_nombre = models.CharField(max_length=100, blank=True, null=True)
    deudor_estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deudores'


class Direcciones(models.Model):
    direccion = models.CharField(primary_key=True, max_length=300)
    deudor_id = models.CharField(max_length=100)
    direccion_id = models.BigIntegerField()
    direccion_estado = models.BooleanField()
    departamento = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    indicativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'
        unique_together = (('direccion', 'deudor_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estructuras(models.Model):
    estructura_id = models.BigIntegerField(primary_key=True)
    estructura_nombre = models.CharField(max_length=100)
    estructura_fecha_creacion = models.DateField()
    unidad = models.ForeignKey('Unidades', models.DO_NOTHING)
    tipo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructuras'


class EstructurasCampos(models.Model):
    est_campos_id = models.BigIntegerField(primary_key=True)
    estructura = models.ForeignKey(Estructuras, models.DO_NOTHING)
    campos_archivo = models.CharField(max_length=255)
    tipo = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=-1, blank=True, null=True)
    estado = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructuras_campos'


class FileAppFile(models.Model):
    file = models.CharField(max_length=100)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'file_app_file'


class Gestiones(models.Model):
    gestion_id = models.BigIntegerField(primary_key=True)
    tarea_id = models.BigIntegerField()
    gestion_fecha = models.DateTimeField(blank=True, null=True)
    usuario_id = models.CharField(max_length=50)
    deudor_id = models.CharField(max_length=100)
    asignacion_id = models.BigIntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    canal = models.CharField(max_length=20)
    id_tipificacion = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    nom_contacto_tercero = models.CharField(max_length=-1, blank=True, null=True)
    tel_adicional = models.BigIntegerField(blank=True, null=True)
    ciudad_tel_adicional = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestiones'


class InsumoCallbot(models.Model):
    insumo_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'insumo_callbot'


class MejorGestion(models.Model):
    deudor_id = models.CharField(primary_key=True, max_length=50)
    mes = models.IntegerField()
    anio = models.IntegerField()
    indicador = models.CharField(max_length=50, blank=True, null=True)
    repeticion = models.IntegerField(blank=True, null=True)
    llamadas = models.IntegerField(blank=True, null=True)
    sms = models.IntegerField(blank=True, null=True)
    correos = models.IntegerField(blank=True, null=True)
    gescall = models.IntegerField(blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    no_contacto = models.IntegerField(blank=True, null=True)
    fecha_gestion = models.DateTimeField(blank=True, null=True)
    visitas = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    asesor = models.CharField(max_length=-1, blank=True, null=True)
    fecha_primer_gestion = models.DateField(blank=True, null=True)
    fecha_ultima_gestion = models.DateField(blank=True, null=True)
    ultimo_alo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mejor_gestion'
        unique_together = (('deudor_id', 'mes', 'anio'),)


class MejorGestionDia(models.Model):
    deudor_id = models.CharField(primary_key=True, max_length=50)
    dia = models.IntegerField()
    indicador = models.CharField(max_length=50, blank=True, null=True)
    repeticion = models.IntegerField(blank=True, null=True)
    llamadas = models.IntegerField(blank=True, null=True)
    sms = models.IntegerField(blank=True, null=True)
    correos = models.IntegerField(blank=True, null=True)
    gescall = models.IntegerField(blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    no_contacto = models.IntegerField(blank=True, null=True)
    fecha_gestion = models.DateTimeField(blank=True, null=True)
    visitas = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    asesor = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mejor_gestion_dia'
        unique_together = (('deudor_id', 'dia'),)


class NombreRama(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nombre_rama'


class Obligaciones(models.Model):
    obligacion_id = models.CharField(primary_key=True, max_length=100)
    deudor = models.ForeignKey(Deudores, models.DO_NOTHING)
    obligacion_estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'obligaciones'


class ObligacionesAsignacion(models.Model):
    oblig_asg_id = models.BigIntegerField(primary_key=True)
    obligacion = models.ForeignKey(Obligaciones, models.DO_NOTHING)
    asignacion = models.ForeignKey(Asignaciones, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'obligaciones_asignacion'


class Pagos(models.Model):
    pago_id = models.BigIntegerField(primary_key=True)
    deudor_id = models.CharField(max_length=100, blank=True, null=True)
    obligacion_id = models.CharField(max_length=100, blank=True, null=True)
    pago_valor = models.BigIntegerField(blank=True, null=True)
    pago_fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'


class Promesas(models.Model):
    promesa_id = models.BigIntegerField(primary_key=True)
    gestion_id = models.BigIntegerField()
    obligacion_id = models.CharField(max_length=100)
    promesa_valor = models.BigIntegerField()
    promesa_fecha_creacion = models.DateField()
    promesa_fecha_acordada = models.DateField()
    tipo = models.CharField(max_length=-1)
    cuotas = models.IntegerField(blank=True, null=True)
    pagon_inicial = models.BigIntegerField(blank=True, null=True)
    valor_cuota = models.BigIntegerField(blank=True, null=True)
    porcentaje_descuento = models.IntegerField(blank=True, null=True)
    valor_descuento = models.BigIntegerField(blank=True, null=True)
    valor_pago_con_descuento = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promesas'


class Tareas(models.Model):
    tarea_id = models.BigIntegerField(primary_key=True)
    tarea_fecha_creacion = models.DateTimeField()
    unidad_id = models.BigIntegerField()
    registros = models.BigIntegerField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    tipo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'


class Telefonos(models.Model):
    telefono = models.BigIntegerField(primary_key=True)
    deudor_id = models.CharField(max_length=100)
    telefono_id = models.BigIntegerField()
    telefono_tipo = models.CharField(max_length=10, blank=True, null=True)
    telefono_estado = models.BooleanField()
    departamento = models.CharField(max_length=-1, blank=True, null=True)
    ciudad = models.CharField(max_length=-1, blank=True, null=True)
    indicativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefonos'
        unique_together = (('telefono', 'deudor_id'),)


class TelefonosPositivos(models.Model):
    deudor_id = models.CharField(primary_key=True, max_length=-1)
    telefono = models.BigIntegerField()
    marcaciones = models.IntegerField()
    fec_ultima_marcacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'telefonos_positivos'
        unique_together = (('deudor_id', 'telefono'),)


class TelefonosTmp(models.Model):
    telefono_id = models.BigIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    deudor_id = models.CharField(max_length=100, blank=True, null=True)
    telefono_tipo = models.CharField(max_length=10, blank=True, null=True)
    telefono_estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefonos_tmp'


class Tipificaciones(models.Model):
    codigo01 = models.IntegerField(primary_key=True)
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
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipificaciones'
        unique_together = (('codigo01', 'codigo02', 'codigo03', 'codigo04', 'codigo05', 'codigo06', 'codigo07', 'codigo08', 'codigo09', 'codigo10'),)


class TipoCliente(models.Model):
    deudor_id = models.CharField(max_length=100, blank=True, null=True)
    tipo_cliente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TiposCargue(models.Model):
    tipo_cargue_id = models.IntegerField(primary_key=True)
    tipo_cargue = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipos_cargue'


class Unicos(models.Model):
    obligacion_id = models.CharField(max_length=100, blank=True, null=True)
    deudor_id = models.CharField(max_length=100, blank=True, null=True)
    unico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unicos'


class Unidades(models.Model):
    unidad_id = models.BigIntegerField(primary_key=True)
    unidad_nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    unidad_estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'


class WolkCbot(models.Model):
    id_chat = models.CharField(max_length=-1, blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)
    routing_point = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    cust_name = models.CharField(max_length=-1, blank=True, null=True)
    cust_email = models.CharField(max_length=-1, blank=True, null=True)
    cust_phone = models.BigIntegerField(blank=True, null=True)
    cust_query = models.CharField(max_length=-1, blank=True, null=True)
    chatbot_answer = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wolk_cbot'


class WolkChats(models.Model):
    chat_id = models.BigIntegerField(blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)
    chat_date = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=-1, blank=True, null=True)
    user_email = models.CharField(max_length=-1, blank=True, null=True)
    user_phone = models.BigIntegerField(blank=True, null=True)
    user_chat_chars = models.IntegerField(blank=True, null=True)
    agent_id = models.BigIntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=-1, blank=True, null=True)
    agent_chat_chars = models.BigIntegerField(blank=True, null=True)
    chat_duration = models.BigIntegerField(blank=True, null=True)
    cod_act = models.CharField(max_length=-1, blank=True, null=True)
    comment = models.CharField(max_length=-1, blank=True, null=True)
    id_customer = models.CharField(max_length=-1, blank=True, null=True)
    agent_skill = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=-1, blank=True, null=True)
    sentiment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wolk_chats'


class WolkConv(models.Model):
    chat_id = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)
    from_msg = models.CharField(max_length=-1, blank=True, null=True)
    from_field = models.CharField(db_column='from_', max_length=-1, blank=True, null=True)  # Field renamed because it ended with '_'.
    to_field = models.CharField(db_column='to_', max_length=-1, blank=True, null=True)  # Field renamed because it ended with '_'.
    time = models.DateTimeField(blank=True, null=True)
    msg = models.CharField(max_length=-1, blank=True, null=True)
    sentiment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wolk_conv'


class WolkManage(models.Model):
    phone = models.BigIntegerField(primary_key=True)
    manage_date = models.DateTimeField()
    deudor_id = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    commit_date = models.DateTimeField(blank=True, null=True)
    valor = models.CharField(max_length=-1, blank=True, null=True)
    dues = models.CharField(max_length=-1, blank=True, null=True)
    reason_nopay = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wolk_manage'
        unique_together = (('phone', 'manage_date'),)
