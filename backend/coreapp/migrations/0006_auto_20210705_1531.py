# Generated by Django 3.2.4 on 2021-07-05 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0005_auto_20210704_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='compiler',
            name='compile_cmd',
            field=models.CharField(default="echo 'meow123'", max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CompilerConfiguration',
            fields=[
                ('shortname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('flags', models.CharField(max_length=100)),
                ('compiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.compiler')),
            ],
        ),
    ]