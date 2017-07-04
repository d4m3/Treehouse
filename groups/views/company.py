from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views import generic


# Used for Update
from braces.views import SetHeadlineMixin

from groups import models
from .. import forms
# from ..models import Company


# Create
class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.CompanyForm
    headline = 'Create Company'
    success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


# Update
class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.CompanyForm
    # success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/form.html'

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return f'Edit {self.object.name}'

    # Send user to this page after successfully updating
    def get_success_url(self):
        return reverse('groups:companies:detail', kwargs={'slug':self.object.slug})


# View Details
class Detail(LoginRequiredMixin, generic.FormView):
    form_class = forms.CompanyInviteForm
    template_name = 'companies/detail.html'

    def get_success_url(self):
        self.get_object()
        return reverse('groups:companies:detail', kwargs={'slug':self.object.slug})

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_object(self):
        self.object = self.request.user.companies.get(slug=self.kwargs.get('slug'))
        return  self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object=self.request.user.companies.get(slug=self.kwargs.get('slug'))
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        models.CompanyInvite.objects.create(
            from_user=self.request.user,
            to_user=form.invitee,
            company=self.get_object()
        )
        return response

# View for seeing an invitation to a group
class Invites(LoginRequiredMixin, generic.ListView):
    template_name = 'companies/invites.html'

    def get_queryset(self):
        return self.request.user.companyinvite_received.all()























