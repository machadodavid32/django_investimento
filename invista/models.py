from django.db import models
from datetime import datetime
# Create your models here.

# Criando uma classe com todas as funcionalidades de um banco de dados, incluindo tabelas
class Investimento(models.Model):
    investimento = models.TextField(max_length=255) # tamanho maximo desta coluna
    valor = models.FloatField() # o valor será decimal
    pago = models.BooleanField(default=False) # padrão em False pois ainda não pago
    data = models.DateField(default=datetime.now) # padrão no horario atual
   
    
    
# Acima trata-se de uma tabela de banco de dados. Para outros tipos de tabela, é só consultar ..
# .. a doc do django na internet    