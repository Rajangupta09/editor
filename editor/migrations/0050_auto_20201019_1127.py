# Generated by Django 3.1 on 2020-10-19 10:27

from django.db import migrations, models

def apply_project_invitations(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    ProjectAccess = apps.get_model('editor','ProjectAccess')
    ProjectInvitation = apps.get_model('editor','ProjectInvitation')
    for invitation in ProjectInvitation.objects.all():
        users = User.objects.filter(email__iexact=invitation.email)
        project = invitation.project
        for u in users:
            if u == project.owner or ProjectAccess.objects.filter(project=project, user=u).exists():
                invitation.applied = True
                break
        if invitation.applied:
            invitation.save()

class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0049_auto_20201012_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='projectinvitation',
            name='applied',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(apply_project_invitations, migrations.RunPython.noop)
    ]
