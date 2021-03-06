# Generated by Django 3.0.5 on 2020-05-05 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import org.custom_model_field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0002_auto_20200429_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=200)),
                ('invite_slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_slug', models.SlugField(max_length=40)),
                ('can_join_without_invite', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('tagline', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to='teesco-backend/static/profile_pic')),
                ('cover_pic', models.ImageField(upload_to='teesco-backend/static/cover_pic')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', org.custom_model_field.PermissionField()),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Org')),
            ],
        ),
        migrations.DeleteModel(
            name='PermissionSetTestModel',
        ),
        migrations.AddField(
            model_name='member',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Org'),
        ),
        migrations.AddField(
            model_name='member',
            name='permissions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.PermissionSet'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Org'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='default_permission_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.PermissionSet'),
        ),
        migrations.AddField(
            model_name='group',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Org'),
        ),
    ]
