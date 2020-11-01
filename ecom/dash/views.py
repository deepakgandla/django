from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, DeleteView
# Create your views here.
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def products(request):
    products=Product.objects.all()

    return render(request,"dash/products.html",{'products':products})

class Feature(View):
    def get(self,request):
        return render(request,'dash/feature.html')

class HomeView(View):
    def get(self,request):
        return render(request,'dash/home.html')

class ProductDetailView(DetailView):
    model = Product

    def get(self, request, pk):

        product=Product.objects.get(id=pk)

        context={'product':product}

        return render(request, 'dash/product.html',context)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'dash/product_confirm_delete.html'
    success_url = reverse_lazy('dash:products')

class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form=CreateUserForm()
        return render(request, 'dash/registration.html', {'form':form})
    def post(self, request):
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request,'created user'+user)
            return redirect('login')

        return render(request, 'dash/registration.html', {'form':form})





