from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bible_app', '0005_aramaicword_tag_usernote_bookmark_versetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='verse',
            name='_processed_text',
            field=models.TextField(blank=True, null=True, verbose_name='Texto Processado'),
        ),
        migrations.CreateModel(
            name='TraducaoEspecifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo_original', models.CharField(max_length=100, unique=True, verbose_name='Termo Original')),
                ('traducao', models.CharField(max_length=100, verbose_name='Tradução')),
                ('notas', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Tradução Específica',
                'verbose_name_plural': 'Traduções Específicas',
                'ordering': ['termo_original'],
            },
        ),
    ]