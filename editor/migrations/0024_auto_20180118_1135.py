# Generated by Django 2.0.1 on 2018-01-18 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0023_auto_20171018_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editoritem',
            name='licence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='editor.Licence'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='licence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editor.Licence'),
        ),
        migrations.AlterField(
            model_name='project',
            name='default_licence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='editor.Licence'),
        ),
        migrations.AlterField(
            model_name='question',
            name='licence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editor.Licence'),
        ),
    ]