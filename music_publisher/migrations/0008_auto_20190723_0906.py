# Generated by Django 2.2.3 on 2019-07-23 09:06

from django.db import migrations, models
import music_publisher.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0007_auto_20190717_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='mr_society',
            field=models.CharField(blank=True, choices=[('55', 'SABAM, Belgium'), ('101', 'SOCAN, Canada'), ('88', 'CMRRA, Canada'), ('40', 'KODA, Denmark'), ('89', 'TEOSTO, Finland'), ('58', 'SACEM, France'), ('35', 'GEMA, Germany'), ('74', 'SIAE, Italy'), ('23', 'BUMA, Netherlands'), ('78', 'STEMRA, Netherlands'), ('90', 'TONO, Norway'), ('79', 'STIM, Sweden'), ('52', 'PRS, United Kingdom'), ('44', 'MCPS, United Kingdom'), ('10', 'ASCAP, United States'), ('21', 'BMI, United States'), ('71', 'SESAC Inc., United States'), ('34', 'HFA, United States'), ('319', 'ICE Services, Administrative Agency'), ('707', 'Musicmark, Administrative Agency')], max_length=3, null=True, validators=[music_publisher.validators.CWRFieldValidator('writer_pr_society')], verbose_name='Mechanical rights society'),
        ),
        migrations.AddField(
            model_name='writer',
            name='sr_society',
            field=models.CharField(blank=True, choices=[('55', 'SABAM, Belgium'), ('101', 'SOCAN, Canada'), ('88', 'CMRRA, Canada'), ('40', 'KODA, Denmark'), ('89', 'TEOSTO, Finland'), ('58', 'SACEM, France'), ('35', 'GEMA, Germany'), ('74', 'SIAE, Italy'), ('23', 'BUMA, Netherlands'), ('78', 'STEMRA, Netherlands'), ('90', 'TONO, Norway'), ('79', 'STIM, Sweden'), ('52', 'PRS, United Kingdom'), ('44', 'MCPS, United Kingdom'), ('10', 'ASCAP, United States'), ('21', 'BMI, United States'), ('71', 'SESAC Inc., United States'), ('34', 'HFA, United States'), ('319', 'ICE Services, Administrative Agency'), ('707', 'Musicmark, Administrative Agency')], max_length=3, null=True, validators=[music_publisher.validators.CWRFieldValidator('writer_pr_society')], verbose_name='Synchronization rights society'),
        ),
    ]
