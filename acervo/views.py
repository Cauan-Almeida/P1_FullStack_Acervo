from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from .forms import LivroForm

def inicio(request):
    return HttpResponse('Olá, acervo!')


def lista_livros(request):
    q = request.GET.get('q')
    status = request.GET.get('status')

    livros = Livro.objects.all()

    if q and q.strip():
        livros = livros.filter(titulo__icontains=q.strip())

    if status == 'disponivel':
        livros = livros.filter(disponivel=True)
    elif status == 'emprestado':
        livros = livros.filter(disponivel=False)

    tem_filtro = bool((q and q.strip()) or status in ['disponivel', 'emprestado'])

    return render(
        request, 'acervo/lista.html',
        {
            'livros': livros,
            'tem_filtro': tem_filtro
        }
    )

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form, 'titulo': 'Cadastrar Livro'})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'acervo/form.html', {'form': form, 'titulo': 'Editar Livro'})

def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista')
    return render(request, 'acervo/confirmar_exclusao.html', {'livro': livro})