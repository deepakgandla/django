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
from .forms import CreateOrderForm, CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

@login_required(login_url="login")
@admin_only
def products(request):
    products=Product.objects.all()

    return render(request,"dash/products.html",{'products':products})

class Feature(View):
    def get(self,request):
        return render(request,'dash/feature.html')


@login_required(login_url='dash:login')
@admin_only
def home(request):
        customers = Customer.objects.all()
        orders=Order.objects.all()
        total_orders = Order.objects.all().count()
        delivered = Order.objects.filter(status='delivered').count()
        outfor = Order.objects.filter(status='out for deliver').count()
        dispatched = Order.objects.filter(status='dispatched').count()
        pending = outfor + dispatched



        context = {'customers': customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending
                   , 'orders':orders}
        return render(request,'dash/home.html', context)


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
            user=form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+username)
            return redirect('dash:login')

        return render(request, 'dash/registration.html', {'form':form})

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'dash/login.html')


def logoutPage(request):
    logout(request)
    return redirect('dash:login')

@login_required(login_url='dash:login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    orders_count=orders.count()

    filter=OrderFilter(request.GET, queryset=orders)
    orders=filter.qs



    context={'customer':customer, 'orders':orders, 'orders_count':orders_count
             , 'filter':filter}
    return render(request,'dash/customer.html', context)

@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer=Customer.objects.get(id=pk)

    #form=CreateOrderForm(initial={'customer':customer})
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)

    if request.method=='POST':
        formset=OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request,'dash/create_order.html',context)


def updateOrder(request, pk):
    order=Order.objects.get(id=pk)
    form=CreateOrderForm(instance=order)
    if request.method=='POST':
        form=CreateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'dash/update_order.html', context)


@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'order':order}
    return render(request, 'dash/delete_order.html', context)

@login_required(login_url='dash:login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):

    orders=request.user.customer.order_set.all()
    total_orders=orders.count()
    delivered = orders.filter(status='delivered').count()
    outfor = orders.filter(status='out for deliver').count()
    dispatched = orders.filter(status='dispatched').count()
    pending = outfor + dispatched


    context={'orders' : orders, 'total_orders' : total_orders, 'delivered' : delivered
             , 'pending' : pending}


    return render(request, 'dash/user_page.html', context)


def accountSettings(request):

    customer=request.user.customer
    orders=customer.order_set.all()
    form=CustomerForm(instance=customer)

    if request.method == 'POST':
        form=CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dash:account_settings')

    context={'form': form, 'orders' : orders}

    return render(request, 'dash/settings.html', context)


def shop(request):
    products = Product.objects.all()


    context={'products' : products}

    return render(request, 'dash/shopping.html', context)

def order(request, pk):
    product=Product.objects.get(id=pk)
    customer = request.user.customer
    #form = CreateOrderForm(initial={'customer': customer.id, 'product': product.id, 'status': 'dispatched'})

    if request.method == 'POST':
        order=Order(customer=Customer(id=customer.id),
                    product=Product(id=product.id),
                    status='dispatched')
        order.save()
        return redirect('dash:order_done')
    context={'product':product}

    return render(request, 'dash/order.html', context)

def orderDone(request):
    return render(request, 'dash/order_done.html')

def orderDetail(request, pk):

    order = Order.objects.get(id=pk)
    customer=order.customer.name
    context = {'order':order, 'customer':customer}
    print(customer)
    print(request.user)
    return render(request, 'dash/order_detail.html', context)

def allCustomerOrders(request):
    customer = request.user.customer
    orders=customer.order_set.all()
    context={'customer':customer, 'orders':orders}
    return render(request, 'dash/customer_orders.html', context)