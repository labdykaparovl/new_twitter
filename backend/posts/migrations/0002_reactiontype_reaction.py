# Generated by Django 4.2 on 2023-05-09 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionType',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('reaction', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.reactiontype')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tweet')),
            ],
        ),
    ]