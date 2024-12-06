from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bible_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verse',
            name='translator',
            field=models.CharField(
                choices=[('yosef_chaim', 'Yosef Chaim'), ('netzer_netzarim', 'Netzer Netzarim')],
                default='yosef_chaim',
                max_length=20,
                verbose_name='Tradutor'
            ),
        ),
        migrations.AddField(
            model_name='verse',
            name='translator_note',
            field=models.TextField(blank=True, null=True, verbose_name='Nota do Tradutor'),
        ),
    ]