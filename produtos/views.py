from django.shortcuts import redirect, render  # type: ignore

from .forms import CategoriaForm, EmbalagemForm, FornecedorForm, LocalForm
from .models import Categoria, Embalagem, Fornecedor, Local


def inicio(request):  # noqa: F811
    return render(request, 'menu.html')


def listar_locais(request):  # noqa: F811
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome_icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})


def adicionar_local(request):  # noqa: F811
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def listar_embalagens(request):  # noqa: F811
    consulta = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()
    if consulta:
        embalagens = embalagens.filter(nome_icontains=consulta)
    if sigla:
       embalagens = embalagens.filter(sigla=sigla)  # noqa: E111
    return render(request, 'produtos/listar_embalagens.html', {'embalagens': embalagens})  # noqa: E501


def adicionar_embalagens(request):  # noqa: F811
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagens.html', {'form': form})  # noqa: E501


def editar_locais(request, pk):
    local = Local.objects.get(pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/editar_locais.html', {'form': form, 'local': local})  # noqa: E501


def editar_embalagens(request, pk):
    embalagens = Embalagem.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagens)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm(instance=embalagens)
    return render(request, 'produtos/editar_embalagens.html', {'form': form, 'embalagens': embalagens})  # noqa: E501


def excluir_locais(request, pk):
    local = Local.objects.get(pk=pk)
    local.delete()
    return redirect('listar_locais')


def excluir_embalagens(request, pk):
    embalagens = Embalagem.objects.get(pk=pk)
    embalagens.delete()
    return redirect('listar_embalagens')


def listar_categorias(request):  # noqa: F811
    consulta = request.GET.get('q')
    categoria = Categoria.objects.all()
    if consulta:
        categoria = categoria.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_categorias.html', {'categorias': categoria})  # noqa: E501


def adicionar_categorias(request):  # noqa: F811
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/adicionar_categorias.html', {'form': form})  # noqa: E501


def editar_categorias(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'produtos/editar_categorias.html', {'form': form, 'categoria': categoria})  # noqa: E501


def excluir_categorias(request, pk):
    categorias = Categoria.objects.get(pk=pk)
    categorias.delete()
    return redirect('listar_categorias')


def listar_fornecedores(request):  # noqa: F811
    consulta = request.GET.get('q')
    fornecedor = Fornecedor.objects.all()
    if consulta:
        fornecedor = fornecedor.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_fornecedores.html', {'fornecedores': fornecedor})  # noqa: E501


def adicionar_fornecedores(request):  # noqa: F811
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'produtos/adicionar_fornecedores.html', {'form': form})  # noqa: E501


def editar_fornecedores(request, pk):  # noqa: F811
    fornecedor = Fornecedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'produtos/editar_fornecedores.html', {'form': form, 'fornecedores': fornecedor})  # noqa: E501
