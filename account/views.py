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
from .userForms import ApointmentForm, SignUpForm, UserEditForm
from .models import *

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
    template_name = 'admin/mngmnt/edit.html'
    models = User
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        me = self.request.user
        context = {
            "form":self.form_class(instance=me),
            "User":User.objects.get(id=me.id),
        } 
        return render(request,self.template_name,context)


    def post(self, request, *args, **kwargs): 
        me = self.request.user
        forms = UserEditForm(self.request.POST,self.request.FILES,instance=me)
        if forms.is_valid():
            forms.save()
            return redirect("account:admin")
 
        return render(request,self.template_name)



class AdminView(TemplateView):
    template_name = "admin/mngmnt/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['apointments'] = Apointment.objects.filter(client=self.request.user)        
        context['lawyers_3'] = Lawywer.objects.all()[:3]        
        return context

class LawyerListView(ListView):
    model = Lawywer
    template_name = "admin/mngmnt/lawyer_list_view.html"

class LawyerDetailView(DetailView):
    model = Lawywer
    form_class  = ApointmentForm
    template_name = "admin/mngmnt/lawyer_detail_view.html"

    def get_context_data(self, *args, **kwargs) :
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
            messages.success(self.request, ('You have successfully set an appointment with %s' %(self.get_object())))
        return redirect('account:lawyer-list')

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
    
def appointment_detail(request):
    # appointment = get_object_or_404(Apointment, pk=pk)
    return render(request, 'admin/mngmnt/appointment_detail.html')