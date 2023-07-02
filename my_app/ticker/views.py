from django.shortcuts import render,redirect
from django.views import View

from .forms import TickerForms
from .utils import anim_create

class Index(View):
    def get(self, request):
        form=TickerForms()
        return render(request, 'index.html', context={
            'form':form,
        })

    def post(self,request):
        form=TickerForms(request.POST)    

        if form.is_valid():
            form.save()

        return redirect("/runtext?text="+form.cleaned_data['message'])


def runtext(request):
    anim_create(text=request.GET['text'])

    return render(request, 'runtext.html',context={
        'text':request.GET['text'],
    })        