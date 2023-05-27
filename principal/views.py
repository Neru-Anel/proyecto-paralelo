from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .forms import Data


# Create your views here.
def main(request):
    num = 4
    return render(request,'index.html',{
        'num': num
    })

def hello(request):
    return HttpResponse("First Page")

#def secuencial(request,texto_1,texto_2):
#    return render(request, "secuencial.html",{
#        'texto_1': texto_1,
#        'texto_2': texto_2,
#    })

def secuencial(request: HttpRequest):
    texto_1 = request.POST['input1']
    texto_2 = request.POST['input2']
    return render(request, 'secuencial.html',{
        'texto_1': texto_1,
        'texto_2': texto_2,
    }
    )