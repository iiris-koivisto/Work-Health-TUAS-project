# Generated by Django 4.1.3 on 2022-11-06 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('admin_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number_answers', models.IntegerField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WorkHealth.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=700)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkHealth.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('option_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(max_length=150)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkHealth.question')),
            ],
        ),
    ]