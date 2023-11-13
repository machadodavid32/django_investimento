from django.contrib import admin

# Register your models here.

# Aqui podemos importar direto pra tela do admin todas as tabelas que queremos.
from .models import Investimento

admin.site.register(Investimento)

