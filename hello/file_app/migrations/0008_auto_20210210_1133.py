# Generated by Django 3.0.8 on 2021-02-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0007_delete_bogotasms'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuxIndicativos',
            fields=[
                ('departamento', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=150)),
                ('indicativo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aux_indicativos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampaingList',
            fields=[
                ('id_list', models.BigAutoField(primary_key=True, serialize=False)),
                ('campaing_name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_id', models.IntegerField(blank=True, null=True)),
                ('campaing_type', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'campaing_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('nombredb', models.CharField(max_length=50)),
                ('fechacreacion', models.DateTimeField(blank=True, null=True)),
                ('schema_name', models.CharField(blank=True, max_length=150, null=True)),
                ('logo', models.CharField(blank=True, max_length=250, null=True)),
                ('user_group', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Habeasdata',
            fields=[
                ('deudor_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('habeas_data', models.BooleanField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('telefono', models.BigIntegerField()),
            ],
            options={
                'db_table': 'habeasdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndicadoresGeneral',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=100, null=True)),
                ('indicador', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'indicadores_general',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerfilesWiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'perfiles_wiser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Telefonos',
            fields=[
                ('telefono', models.BigIntegerField()),
                ('deudor_id', models.CharField(max_length=100)),
                ('telefono_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('telefono_tipo', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono_estado', models.BooleanField()),
                ('departamento', models.CharField(blank=True, max_length=150, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('indicativo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'telefonos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipificacionesHerramientas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('herramienta', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'tipificaciones_herramientas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('fechacreacion', models.DateTimeField()),
                ('vicidial', models.CharField(blank=True, max_length=120, null=True)),
                ('prefijo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'unidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosWiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('estado', models.BooleanField(blank=True, null=True)),
                ('fechacreacion', models.DateTimeField(blank=True, null=True)),
                ('vicidial', models.CharField(blank=True, max_length=150, null=True)),
                ('password_expiration', models.DateField(blank=True, null=True)),
                ('restore_password', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuarios_wiser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VicidialPause',
            fields=[
                ('id', models.IntegerField(blank=True, null=True)),
                ('pause', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'vicidial_pause',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Unidades',
        ),
    ]