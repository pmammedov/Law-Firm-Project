from typing import Any
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
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
		# cat = Category.objects.all()
		data = Article.objects.all()

		# context["cat"] = cat
		context['data'] = data
		return context

class BlogListView(ListView):
	model = Article
	paginate_by = 4
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		# cat = Category.objects.all()
		data = Article.objects.all()

		# context["cat"] = cat
		context['data'] = data
		return context

class BackBlogListView(ListView):
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


class ArticleList(ListView):
	model = Article
	template_name = 'blog/article_list.html'
	context_object_name = 'object'


class postDetails(DetailView): 
	model = Article
	form_class = CommentForm
	 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		frm =  self.form_class()
		new = Article.objects.all()[:10]
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
	
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	cat = Category.objects.all()
	# 	# data = Article.objects.all()
	# 	context["cat"] = cat
	# 	# context['data'] = data
	# 	return context

# class BlogCreateView(CreateView):
# 	model = Article
# 	fields = ('title', 'thumb', 'body')
# 	template_name = 'admin/mngmnt/appointment_detail.html'
# 	success_url = '/blog_list/'


# def create_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:blog_list')  # Replace with your redirect target
#     else:
#         form = ArticleForm()
#     return render(request, 'blog/create_article.html', {'form': form})

class CreateArticleView(CreateView):
	model = Article
	form_class = ArticleForm
	template_name = 'blog/create_article.html'
	success_url = reverse_lazy('blog:blog_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	
# class BlogDeleteView(DeleteView):
# 	model = Article
# 	template_name = 'admin/mngmnt/appointment_detail.html'
# 	success_url = reverse_lazy('blog')

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog_list')
    template_name = "admin/mngmnt/appointment_detail.html"  # Optional if you need a confirmation page

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)