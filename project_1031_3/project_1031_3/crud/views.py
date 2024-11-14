from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView
# from django.views.generic.edit import CreateView
# from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product 
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

# def product_list_view(request):
#     products = Product.objects.all()
#     return render(request, "crud/product_list.html", {"products":products})
