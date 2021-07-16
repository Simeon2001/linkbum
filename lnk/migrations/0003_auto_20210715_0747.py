# Generated by Django 3.2.5 on 2021-07-15 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lnk', '0002_auto_20210614_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_media',
            name='fbk',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='gtb',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='ins',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='snt',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='twr',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='social_media',
            name='whp',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.CreateModel(
            name='site_links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.URLField(max_length=1000)),
                ('details', models.TextField(max_length=30)),
                ('clicks', models.IntegerField(default=0)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='lnk.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lnk.site_links'),
        ),
        migrations.DeleteModel(
            name='links',
        ),
    ]
