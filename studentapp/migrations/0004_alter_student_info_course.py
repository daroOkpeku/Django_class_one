# Generated by Django 5.0.6 on 2024-06-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_alter_attendance_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='course',
            field=models.CharField(choices=[('SF', 'Software Engineering'), ('AI', 'Artificial Intelligence'), ('ME', 'Blockchain Technology'), ('BI', 'business intelligence')], max_length=255),
        ),
    ]