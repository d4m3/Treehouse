from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views import generic


# Used for Update
from braces.views import SetHeadlineMixin

from .. import forms
from ..models import Family


# Create
class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.FamilyForm
    headline = 'Create Family'
    success_url = reverse_lazy('users:dashboard')
    template_name = 'families/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


# Update
class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.FamilyForm
    # success_url = reverse_lazy('users:dashboard')
    template_name = 'families/form.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return f'Edit {self.object.name}'

    # Send user to this page after successfully updating
    def get_success_url(self):
        return reverse('groups:families:detail', kwargs={'slug':self.object.slug})


# View Details
class Detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'families/detail.html'

    def get_queryset(self):
        return self.request.user.families.all()


























