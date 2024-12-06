from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bible_app', '0002_add_translator_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='verse',
            name='aramaic_source',
            field=models.CharField(
                choices=[
                    ('curetonian', 'Antigos Evangelhos Curetonianos Siríacos'),
                    ('sinaiticus', 'Palimpsesto Sinaítico Siríaco Antigo'),
                    ('peshitta', 'Peshitta')
                ],
                default='peshitta',
                max_length=20,
                verbose_name='Fonte do Texto Aramaico'
            ),
            preserve_default=False,
        ),
    ]