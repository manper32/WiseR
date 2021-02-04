from rest_framework import serializers
from file_app.models import File, Gestiones, Tareas, VicidialPause, CampaingList

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')

class GestionSerializer(serializers.ModelSerializer):
  class Meta():
    model = Gestiones
    fields = (
      'gestion_id',
      'tarea_id',
      'gestion_fecha',
      'usuario_id',
      'deudor_id',
      'asignacion_id',
      'telefono',
      'canal',
      'id_tipificacion',
      'descripcion',
      'nom_contacto_tercero',
      'tel_adicional',
      'ciudad_tel_adicional',)

class TareasSerializer(serializers.ModelSerializer):
  class Meta():
    model = Tareas
    fields = (
      'tarea_id',
      'tarea_fecha_creacion',
      'unidad_id',
      'registros',
      'clientes',
      'obligaciones',
      'tipo',
      'nombre',
      'list_id')

class VicidialPauseSerializer(serializers.ModelSerializer):
  class Meta():
    model = VicidialPause
    fields = ('id','pause')

class CampaignListSerializer(serializers.ModelSerializer):
  class Meta():
    model = CampaingList
    fields = (
      'id_list',
      'campaing_name',
      'unit_id',
      'campaing_type')