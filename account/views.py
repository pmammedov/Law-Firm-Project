from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login , logout
from django.views.generic import ListView , DetailView ,View,TemplateView, DeleteView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from .userForms import ApointmentForm, CreateUserForm, SignUpForm, UserEditForm, LawyerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.db.models import Count
from django.db.models import Count
from .models import Lawywer



class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        ctx = {
            'form': self.form_class() ,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = True #u need to deactivate account till it is confirmed
            user.save()
            # FarmPlotModel.objects.create(name="default",size="1 x 1(acres)",farm_location="default",user=user)
            #send activation email

            # this_site = get_current_site(request)
            # site = this_site.domain
            # subject = 'Activate Your %(site) Account'
            # message = render_to_string('registration/account_activation_email.html', {
            #     'user': user,
            #     'domain': site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': email_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)

            messages.success(request, ('We have sent a confirmation link to your email to activate your account\nPlease follow your email and click on the link!'))

            return redirect('account:login')

        return render(request, self.template_name, {'form': form})

class UserEditCreateView(CreateView):
    template_name = 'admin/mngmnt/create_user.html'
    models = User
    form_class = UserEditForm
    success_url = reverse_lazy('account:lawyer-list')

class AdminView(TemplateView):
    template_name = "admin/mngmnt/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['apointments'] = Apointment.objects.filter(client=self.request.user)        
        context['lawyers_3'] = Lawywer.objects.all()[:3]        
        return context
    
class CreateLawyerView(CreateView):
    model = Lawywer
    form_class = LawyerForm
    template_name = "admin/mngmnt/create_lawyer.html"
    success_url = reverse_lazy('account:lawyer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Lawyer'
        print('burasi calistiiiii')
        return context

class LawyerListView(LoginRequiredMixin, ListView):
    model = Lawywer
    template_name = "admin/mngmnt/lawyer_list_view.html"
    context_object_name = 'lawyers'
    user_form = CreateUserForm
    lawyer_form = LawyerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["non_lawyer_users"] = User.objects.exclude(id__in=Lawywer.objects.values_list('user_id', flat=True))        
        return context
    
    def post(self, request, *args, **kwargs):
        form_user = self.user_form(request.POST, request.FILES)
        form_lawyer = self.lawyer_form(request.POST, request.FILES)
        
        if form_user.is_valid() and form_lawyer.is_valid():
            print ('forms are valid')
            user = form_user.save(commit=False)
            print('user saved with success --> ',user)    
            user.save()
            instance  = form_lawyer.save(commit=False)
            instance.user = user
            instance.save()
            print('lawyer saved with success --> ',instance)    
            messages.success(request, ('lawyer saved with success'))
        if form_user.errors:
            messages.error(request, (form_user.errors))  
            print('user form errors --> ',form_user.errors)
        if form_lawyer.errors:
            messages.error(request, (form_lawyer.errors))  
            print('lawyer form errors --> ',form_lawyer.errors)
        return redirect('account:lawyer-list')

        

    

class LawyerDetailView(DetailView):
    model = Lawywer
    form_class = ApointmentForm
    template_name = "admin/mngmnt/lawyer_detail_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        client = self.request.user
        if form.is_valid():
            instance = form.save(commit=False)
            instance.client = client
            instance.lawyer = self.get_object()
            instance.save()
            messages.success(self.request, f'You have successfully set an appointment with {self.get_object()}')
        return redirect('account:lawyer-list')
    
class DeleteLawyerView(DeleteView):
    model = Lawywer
    template_name = "admin/mngmnt/lawyer_list_view.html"
    success_url = reverse_lazy('account:lawyer-list')

class ApointmentListView(ListView):
    model = Apointment
    template_name = "admin/mngmnt/appointment_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['apointments'] = Apointment.objects.filter(client=self.request.user)
        print(context['apointments'])  # Debug statement to check the queryset
        return context
    
    # def post(self, request, *args, **kwargs):
    #     appointment_id = request.POST.get('id')
    #     if appointment_id:
    #         appointment = Apointment.objects.filter(appointment_id=appointment_id, client=self.request.user).first()
    #         if appointment:
    #             appointment.delete()
    #     return redirect('account:apointment')

class AppointmentDeleteView(DeleteView):
    model = Apointment
    success_url = reverse_lazy('account:apointment')
    template_name = "admin/mngmnt/appointment_view.html"  # Optional if you need a confirmation page

    def get_queryset(self):
        return Apointment.objects.filter(client=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

class TopPerformersView(ListView):
    model = Lawywer
    template_name = 'admin/mngmnt/index.html'  # Update with your actual template path
    context_object_name = 'lawyers_3'
    paginate_by = 10  # Adjust as needed

    def get_queryset(self):
        return Lawywer.objects.annotate(
            num_appointments=Count('appointments')
        ).order_by('-num_appointments')[:3]
    

def appointment_detail(request):
    # appointment = get_object_or_404(Apointment, pk=pk)
    return render(request, 'admin/mngmnt/appointment_detail.html')