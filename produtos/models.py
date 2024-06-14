from pyexpat import model
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome da categoria', unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação da categoria')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data de atualização da categoria')

    class Meta:
        tb_table = 'categorias'

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='categoria do produto')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data da criação do produto')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data de atualização do produto')

    class Meta:
        tb_table = 'produtos'

class Fornecedor(models.Model):
    nome_social = models.CharField(max_length=100, verbose_name='Razao Social do fornecedor', unique=True)
    nome_fantasia = models.CharField(max_length=100, verbose_name='nome Fantasia do fornecedor')
    produtos =models.ManyToManyField(Produto, verbose_name='Produtos do Fornecedor', through='FornecedorProduto', )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data da criação do fornecedor')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data de atualização do fornecedor')
    
    class Meta:
        tb_table = 'fornecedores'

class FornecedorProduto(model.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='fornecedor do produto')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='produto do fornecedor')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço do produto')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data da criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='data de atualização')