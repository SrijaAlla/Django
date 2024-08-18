from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Product, Category, Review
from .forms import ProductForm, CategoryForm, ReviewsForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product_list.html', {'page_obj': page_obj})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# @login_required
def product_create(request):
    context ={}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
		
    context['form']= form
    return render(request, "product_form.html", context)
        
# @login_required
# @permission_required('products.change_product', raise_exception=True)
def product_update(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products/"+ id+"/detail/")
    context["form"] = form 
    return render(request, "product_form.html", context)

def product_delete(request, id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})       

def category_list(request):
     categories = Category.objects.all()
     return render(request, 'categories_list.html', {'categories': categories})

# def category_update(request):
#      context = {}
#      category = get_object_or_404(Category, id=id)
#      form = CategoryForm(request.POST or None, instance=category)
#      if form.is_valid():
#           form.save()
#           return HttpResponseRedirect('/category/'+id+'/detail/')
#      context['form'] = form
#      return render(request, 'category_form.html',context )
