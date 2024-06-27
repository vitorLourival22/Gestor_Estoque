from os import name
from pyexpat import model
from django.db import models
from Utils.BaseModel import BaseModel

class Categoria(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome da categoria', unique=True)

    class Meta:
        db_table = 'categorias'

class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='categoria do produto')
    embalagens = models.ManyToManyField('produtos.Embalagem',  verbose_name='Embalagens do Produtos')

    class Meta:
        db_table = 'produtos'

class Fornecedor(BaseModel):
    nome_social = models.CharField(max_length=100, verbose_name='Razao Social do fornecedor', unique=True)
    nome_fantasia = models.CharField(max_length=100, verbose_name='nome Fantasia do fornecedor')
    produtos =models.ManyToManyField('produtos.Produto', verbose_name='Produtos do Fornecedor' )
   
    
    class Meta:
        db_table = 'fornecedores'

class Embalagem(BaseModel):
    name = models.CharField(max_length=50, verbose_name= 'Nome da embalagem')
    sigla = models.CharField(max_length=3, verbose_name= 'Sigla da embalagem')
    
    class Meta:
        db_table = 'embalagens'

class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [ 
        ( 1 , 'Entrada'),
        ( -1 , 'Saída')
    ]
    fornecedor = models.ForeignKey('produtos.Fornecedor', on_delete=models.CASCADE, verbose_name= 'Fornecedor do produto armazenado')
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, verbose_name='produto da movimentação')
    quantidade = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Quantidade Movimentada')
    local = models.ForeignKey('produtos.local', on_delete=models.CASCADE, verbose_name='Local da Movimentação')
    tipo = models.IntegerField(choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de Movimentação')
    
    class Meta:
        db_table = 'movimentacoes'
        
class Local(BaseModel):
    TIPOS_DE_LOCAL = [
        ('F', 'Fisico'),
        ('D', 'Digital')
    ]
    nome = models.CharField(max_length=50, verbose_name='nome do local armazenado', unique=True)
    tipo = models.CharField(max_length=1, choices=TIPOS_DE_LOCAL, verbose_name='Tipo de local armazenado')
    
    class Meta:
        db_table = 'locais'