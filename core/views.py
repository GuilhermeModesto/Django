from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome='Digite seu nome', idade='Digite sua idade'):
    return HttpResponse(f'<h1>Hello {nome} {idade} anos<h1>')


def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse(f'A soma de {num1} + {num2} = {soma}')

def multiplica(request, n1, n2):
    return HttpResponse(f'A multiplicação de {n1}x{n2} = {n1*n2}')
