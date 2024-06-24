from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView , DetailView ,View
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.models import Group 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import *
from .forms import *

def ContactFunc(request):
    template_name = 'contact.html'
    return render(request,template_name)

class HomeScreen(ListView):

	model = Article
	paginate_by = 4
     
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):

		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		data = Article.objects.all()

		context["cat"] = cat
		context['data'] = data
		return context

class BlogListView(ListView):
	model = Article
	paginate_by = 4
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		data = Article.objects.all()

		context["cat"] = cat
		context['data'] = data
		return context

class BlogListView(ListView):
    model = Article
    template_name = 'admin/mngmnt/appointment_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blog'] = Article.objects.all()
        return context

class BlogDetailView(DetailView):
	model = Article
	template_name = 'blog/details.html'
	context_object_name = 'article'



class postDetails(DetailView): 
	model = Article
	form_class = CommentForm
	 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		frm =  self.form_class()
		new = Article.objects.all()[:10]
		cat = Category.objects.all()
		post  = Article.objects.all()
		related_query = ''

		ref = []

		title = self.get_object().title

		# if title:
		# 	related_query = post.filter(
		# 		Q(title__icontains=title)|
		# 		Q(intro__icontains=title)
		# 	) 
		data = title.split(' ')

		obj = self.get_object().id

		for i in data:
			if i != '-':
				# print(str(i))
				related_query = post.filter( Q(title__icontains=i) )
				ref.append(related_query)
		
		context['r_post'] = ref		
		context["cat"] = cat
		context["frm"] = frm 
		context["comm"] = self.get_object().comments.filter(active=True)
		context["comm_all"] = self.get_object().comments.filter(active=True).count()
		context["data"] = new
		return context

	
	def post(self, request,pk, *args, **kwargs ):
		form = self.form_class(request.POST,request.FILES)
		
		if form.is_valid():
			instance = form.save(commit=False)
			instance.post = Article.objects.get(pk=pk)
			instance.save()		
			return redirect(self.get_object().get_absolute_url())
		return render(request,self.template_name,{'form':form})
 
class SearchProduct(ListView):
	model = Article
	template_name = 'blog/results.html'
    
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			object_list = self.model.objects.filter(
				Q(title__icontains=query)|
				Q(intro__icontains=query)|
				Q(body__icontains=query)
			)
		else:
			object_list = self.model.objects.all()
		return object_list 
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = Category.objects.all()
		# data = Article.objects.all()
		context["cat"] = cat
		# context['data'] = data
		return context
	
 
 