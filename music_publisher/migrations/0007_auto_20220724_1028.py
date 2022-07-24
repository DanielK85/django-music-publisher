# Generated by Django 3.2.14 on 2022-07-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0006_alter_cwrexport_nwr_rev'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='account_number',
            field=models.CharField(
                blank=True,
                help_text='Use this field for linking royalty statements with your accounting',
                max_length=100,
                null=True,
                verbose_name='Account #',
            ),
        ),
        migrations.AlterField(
            model_name='ackimport',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='alternatetitle',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='artistinwork',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='cwrexport',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='cwrexport',
            name='nwr_rev',
            field=models.CharField(
                choices=[
                    ('NWR', 'CWR 2.1: New work registrations'),
                    ('REV', 'CWR 2.1: Revisions of registered works'),
                    ('NW2', 'CWR 2.2: New work registrations'),
                    ('RE2', 'CWR 2.2: Revisions of registered works'),
                    ('WRK', 'CWR 3.0: Work registration'),
                    ('ISR', 'CWR 3.0: ISWC request (EDI)'),
                    ('WR1', 'CWR 3.1 DRAFT: Work registration'),
                ],
                db_index=True,
                default='NWR',
                max_length=3,
                verbose_name='CWR version/type',
            ),
        ),
        migrations.AlterField(
            model_name='dataimport',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='label',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='library',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='recording',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='release',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='work',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='workacknowledgement',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='writer',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
        migrations.AlterField(
            model_name='writerinwork',
            name='id',
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID',
            ),
        ),
    ]
