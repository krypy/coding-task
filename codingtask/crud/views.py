from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from crud.models import Client
from crud.forms import ClientForm


def index(request):
    return render(request, 'index.html')    


@login_required
def home(request):
    clients = Client.objects.all()
    return render(request, 'home.html', {'clients': clients})


@login_required
def logout(request):
    auth_logout(request)
    return redirect(reverse('index'))



@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            client = Client(
                first_name=data['first_name'],
                last_name=data['last_name'],
                iban=data['iban'],
                created_by=request.user
            )
            client.save()
            return redirect(reverse('home'))
    else: 
        form = ClientForm()
    return render(request, 'edit.html', {'form': form, 'title': 'Add Client', 'submit': 'Add'})


@login_required
def edit_client(request, client_id ):
    try:
        client = Client.objects.get(created_by=request.user, pk=client_id)
    except Client.DoesNotExist:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            client.first_name = data['first_name']
            client.last_name = data['last_name']
            client.iban = data['iban']
            client.save()
            return redirect(reverse('home'))

    else:
        form = ClientForm(instance=client)


    return render(request, 'edit.html', {'form': form, 'title': 'Edit Client', 'submit': 'Update'})


@login_required
def delete_client(request, client_id ):
    try:
        client = Client.objects.get(created_by=request.user, pk=client_id)
        client.delete()
    except Client.DoesNotExist:
        pass
    return redirect(reverse('home'))
