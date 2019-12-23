from django.http import Http404   ##this also raises 404 error just like get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm, ProductForm_Shortcut
from .models import Product

##############################for article#############################################
from .models import Article
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  UpdateView, DeleteView)
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'testing/index.html')

def product_create_view(request):
    form = ProductForm(request.POST or None)  #i dont know it yet
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form':form}
    return render(request, 'testing/createProd.html', context)


#pure django form
#this kind of form contails validations too..... All kind of validations....
def product_create_view_two(request):
    form = RawProductForm(request.GET)   # this is just initializing.... it wont do any good....
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'testing/createProd2.html', context)


### shortcut for above method.... by using 1 method as base
def product_create_view_three(request):
    form = ProductForm_Shortcut(request.POST or None)  #i dont know it yet
    if form.is_valid():
        form.save()
        form = ProductForm_Shortcut()

    context = {'form':form}
    return render(request, 'testing/createProd3.html', context)


def render_initial_data(request):
    initial_data = {
        'title': 'My Awesome Title',
    }
    form = ProductForm_Shortcut(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm_Shortcut()
    context = {'form':form}
    return render(request, 'testing/createProd2.html', context)


def dynamic_lookup_view(request, prod_id):
    #obj = Product.objects.get(id = prod_id) ##instead of this we can use get_object_or_404 to raise a 404 error if id is not found

    #method 1 to raise 404
    ##obj = get_object_or_404(Product, id=prod_id)

    # method 2 to raise 404 ------- It uses try and except block
    try:
        obj = Product.objects.get(id = prod_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'obj':obj
    }
    return render(request, 'testing/prodDetail.html', context)

def delete_product(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)
    print(request.method)
    if request.method == "GET":
        #confirming delete..... where as in get requests we dont have to write the above line....
        obj.delete()
    context = {
        'obj': obj
    }
    return render(request, 'testing/delete.html', context)

def product_list_view(request):
    query_set = Product.objects.all()    #gives a list of objects
    context = {
        'object_list':query_set
    }
    return render(request, 'testing/prod_list.html', context)





class ArticleListView(ListView):
    queryset = Article.objects.all()       ####this is requirement
    #<app_name>/<model_name>_list
    template_name = 'testing/Article_list.html'

class ArticleDetailView(DetailView):
    template_name = 'testing/Article_detail.html'
    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'testing/Article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    ##Not necessary
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('testing:article_list_view')
