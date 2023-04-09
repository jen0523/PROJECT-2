from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import PcOutForm
import sys


projectsList = [

    {'id': '1', 'title': 'Check in Probe Cards'},

    { 'id': '2', 'title': 'Check out Probe Cards'},

    {'id': '3', 'title': 'Probe Card Inventory' },

    {'id': '4', 'title': 'Probe Card Status' },

]

def ProbeCards(request):
    page= 'xxxxxx'
    number = 10
    context= {'page': page, 'number': number, 'ProbeCards': projectsList}
    return render(request,'ProbeCards/home.html', context)


def PCout(request):
    if request.method == "POST":
        print("add data", file=sys.stderr)
        # create a form instance and populate it with data from the request:
        form = PcOutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PcOutForm()
        return render(request,'ProbeCards/checkout.html',{"form": form})
    



def PCin(request, qk):

    PCinObj = None
    for i in projectsList:
        if i['id'] == qk:
            PCinObj = i
    return render(request,'ProbeCards/checkin.html',{'PCin':PCinObj})

def PCinv(request, rk):

    PCinvObj = None
    for i in projectsList:
        if i['id'] == rk:
            PCinvObj = i
    return render(request,'ProbeCards/pcinv.html',{'PCinv':PCinvObj})

def PCstatus(request, sk):

    PCstatusObj = None
    for i in projectsList:
        if i['id'] == sk:
            PCstatusObj = i

    return render(request,'ProbeCards/pcstatus.html',{'PCstatus':PCstatusObj})