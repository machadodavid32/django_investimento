from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


# Função render nos permite renderizar uma página html

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para investir')


# Sempre que quisermos criar uma nova página, é necessário entrar neste arquivo views e fazer uma 
# nova função

def pagina_contato(request):
    return HttpResponse('Página de contato')

def minha_historia(request):
    pessoa = {
        'nome': 'Jeff',
        'idade': 28,
        'hobby': 'games'
    }
    return render(request,'investimentos/minha_historia.html', pessoa)
# Esta função acima está encaminhando informações direto pra página. Numa aplicação real,...
# os dado da pessoa podem vir de um banco de dados, sendo atualizado dinamicamente para a pagina. 

def novo_investimento(resquest):
    return render(resquest, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento':request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')    
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)    
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {
            'formulario':formulario
        })
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)    
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

@login_required    
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)        
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item':investimento})