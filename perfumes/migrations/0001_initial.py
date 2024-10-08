# Generated by Django 5.1 on 2024-08-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='perfumes/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'perfume',
                'verbose_name_plural': 'perfumes',
            },
        ),
    ]
