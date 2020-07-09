# Generated by Django 2.2.10 on 2020-07-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0049_systemuser_sftp_root'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together={('org_id', 'name')},
        ),
    ]