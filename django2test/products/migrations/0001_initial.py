# Generated by Django 2.0.7 on 2018-11-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
