from rest_framework import serializers
from file_app.models import File, Gestiones

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