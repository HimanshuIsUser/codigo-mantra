# Generated by Django 4.2.7 on 2023-11-26 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('blog', '0006_alter_blogmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_profile'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.user_profile'),
        ),
    ]
