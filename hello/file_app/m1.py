# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acuerdos(models.Model):
    acuerdo_id = models.BigIntegerField(primary_key=True)
    deudor_id = models.IntegerField()
    nombre_deudor = models.CharField(max_length=255)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    mes_acuerdo = models.CharField(max_length=255)
    tipo = models.TextField()  # This field type is a guess.
    saldo_capital = models.BigIntegerField(blank=True, null=True)
    plazo = models.IntegerField()
    valor_cuota = models.CharField(max_length=255, blank=True, null=True)
    tasa_interes = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acuerdos'


class AlternativasTipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'alternativas_tipo'


class AsignacionActualArchivo(models.Model):
    tipoid = models.CharField(max_length=150, blank=True, null=True)
    deudor_id = models.CharField(max_length=150, blank=True, null=True)
    asignacion_id = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_actual_archivo'


class AsignacionActualMongo(models.Model):
    tipoid = models.CharField(max_length=150, blank=True, null=True)
    deudor_id = models.CharField(max_length=150, blank=True, null=True)
    asignacion_id = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_actual_mongo'


class Asignaciones(models.Model):
    asignacion_id = models.BigIntegerField(primary_key=True)
    unidad_id = models.BigIntegerField()
    asignacion_nombre = models.CharField(max_length=100)
    asignacion_fecha_creacion = models.DateField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    estado = models.BooleanField()
    fecha_apertura = models.DateField()
    fecha_cierre = models.DateField()

    class Meta:
        managed = False
        db_table = 'asignaciones'


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


class CampaingList(models.Model):
    id_list = models.IntegerField()
    campaing_name = models.CharField(max_length=-1, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    campaing_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'campaing_list'


class Campos(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    visible = models.BooleanField(blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    main = models.BooleanField(blank=True, null=True)
    unidad_id = models.IntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campos'


class CamposObligatorios(models.Model):
    id_campo = models.IntegerField(primary_key=True)
    campo_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'campos_obligatorios'


class Codigos(models.Model):
    descripcion = models.CharField(max_length=-1, blank=True, null=True)
    codigo = models.IntegerField(primary_key=True)
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'codigos'
        unique_together = (('codigo', 'unidad'),)


class Comites(models.Model):
    comite_id = models.BigIntegerField(primary_key=True)
    deudor_id = models.IntegerField()
    nombre_deudor = models.CharField(max_length=255)
    nombre_coordinador = models.CharField(max_length=255)
    texto_comite = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comites'


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


class Estructuras(models.Model):
    estructura_id = models.BigIntegerField(primary_key=True)
    estructura_nombre = models.CharField(max_length=100)
    estructura_fecha_creacion = models.DateField()
    unidad_id = models.IntegerField()
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


class GestionPreguntas(models.Model):
    id = models.BigAutoField(primary_key=True)
    gestion_id = models.BigIntegerField()
    pregunta1 = models.CharField(max_length=255, blank=True, null=True)
    pregunta2 = models.CharField(max_length=255, blank=True, null=True)
    pregunta3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestion_preguntas'


class Gestiones(models.Model):
    gestion_id = models.BigIntegerField(primary_key=True)
    tarea_id = models.BigIntegerField()
    gestion_fecha = models.DateTimeField(blank=True, null=True)
    usuario_id = models.CharField(max_length=50)
    deudor_id = models.CharField(max_length=100)
    asignacion_id = models.BigIntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    canal = models.CharField(max_length=20)
    id_tipificacion = models.BigIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    nom_contacto_tercero = models.CharField(max_length=-1, blank=True, null=True)
    tel_adicional = models.BigIntegerField(blank=True, null=True)
    ciudad_tel_adicional = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestiones'


class HelperChecks(models.Model):
    type = models.CharField(max_length=255)
    visible = models.BooleanField(blank=True, null=True)
    checked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helper_checks'


class HelperInputs(models.Model):
    type = models.CharField(max_length=255)
    text = models.CharField(max_length=255, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    hint = models.CharField(max_length=255, blank=True, null=True)
    disabled = models.BooleanField(blank=True, null=True)
    allow_state = models.BooleanField(blank=True, null=True)
    state_on = models.CharField(max_length=255, blank=True, null=True)
    state_off = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helper_inputs'


class HelperItems(models.Model):
    posicion = models.IntegerField()
    check = models.ForeignKey(HelperChecks, models.DO_NOTHING)
    label = models.ForeignKey('HelperLabels', models.DO_NOTHING)
    input = models.ForeignKey(HelperInputs, models.DO_NOTHING)
    contact = models.IntegerField(blank=True, null=True)
    attempt = models.IntegerField(blank=True, null=True)
    unit_id = models.IntegerField()
    save_item = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helper_items'


class HelperLabels(models.Model):
    type = models.CharField(max_length=255)
    text = models.CharField(max_length=255, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    modal = models.ForeignKey('HelperModals', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helper_labels'


class HelperModals(models.Model):
    type = models.CharField(max_length=255)
    text = models.CharField(max_length=255, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helper_modals'


class HerramientasProcesos(models.Model):
    herramienta = models.BooleanField()
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'herramientas_procesos'


class IndicadoresGeneral(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=255)
    indicador = models.CharField(max_length=255)
    indicador_contacto = models.IntegerField(blank=True, null=True)
    indicador_efectividad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicadores_general'
        unique_together = (('id', 'indicador'),)


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
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nombre_rama'
        unique_together = (('id', 'unidad'),)


class NombresPreguntas(models.Model):
    unidad_id = models.IntegerField(blank=True, null=True)
    pregunta = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'nombres_preguntas'


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
    estado = models.CharField(max_length=50)
    fecha_actualizacion = models.DateField()

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
        unique_together = (('obligacion_id', 'pago_fecha'),)


class Promesas(models.Model):
    promesa_id = models.BigIntegerField(primary_key=True)
    gestion = models.ForeignKey(Gestiones, models.DO_NOTHING)
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


class TareaManual(models.Model):
    usuario_id = models.BigIntegerField()
    deudor_id = models.CharField(max_length=255)
    tarea_id = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_manual'


class Tareas(models.Model):
    tarea_id = models.BigIntegerField(primary_key=True)
    tarea_fecha_creacion = models.DateTimeField()
    unidad_id = models.BigIntegerField()
    registros = models.BigIntegerField()
    clientes = models.BigIntegerField()
    obligaciones = models.BigIntegerField()
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    list_id = models.BigIntegerField(blank=True, null=True)

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
    unidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipificaciones'
        unique_together = (('codigo01', 'codigo02', 'codigo03', 'codigo04', 'codigo05', 'codigo06', 'codigo07', 'codigo08', 'codigo09', 'codigo10', 'unidad'),)


class Tipificaciones(models.Model):
    codigo01 = models.IntegerField(blank=True, null=True)
    codigo02 = models.IntegerField(blank=True, null=True)
    codigo03 = models.IntegerField(blank=True, null=True)
    codigo04 = models.IntegerField(blank=True, null=True)
    codigo05 = models.IntegerField(blank=True, null=True)
    codigo06 = models.IntegerField(blank=True, null=True)
    codigo07 = models.IntegerField(blank=True, null=True)
    codigo08 = models.IntegerField(blank=True, null=True)
    codigo09 = models.IntegerField(blank=True, null=True)
    codigo10 = models.IntegerField(blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)
    indicador = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    unidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipificaciones_'


class TipificacionesHerramientas(models.Model):
    id = models.IntegerField(primary_key=True)
    herramienta = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'tipificaciones_herramientas'
        unique_together = (('id', 'herramienta'),)


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


class TmpCodgestion(models.Model):
    idactual = models.IntegerField(blank=True, null=True)
    idnuevo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_codgestion'


class TmpComovamos(models.Model):
    id_tipificacion = models.BigIntegerField(blank=True, null=True)
    gestion_id = models.BigIntegerField(blank=True, null=True)
    tarea_id = models.BigIntegerField(blank=True, null=True)
    gestion_fecha = models.DateTimeField(blank=True, null=True)
    usuario_id = models.CharField(max_length=50, blank=True, null=True)
    deudor_id = models.CharField(max_length=100, blank=True, null=True)
    asignacion_id = models.BigIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    canal = models.CharField(max_length=20, blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)
    indicador = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_comovamos'


class TmpPruebas(models.Model):
    ident = models.CharField(max_length=-1, blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_pruebas'


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
