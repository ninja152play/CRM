from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Count, Sum
from django.utils.decorators import method_decorator

from .decorators import role_required
from .models import *
from .forms import *

# Create your views here.
@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class ServiceListView(generic.ListView):
    model = Service
    template_name = 'app/service_list.html'


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class ServiceCreateView(generic.CreateView):
    model = Service
    fields = ['name', 'description', 'price']
    template_name = 'app/service_form.html'
    success_url = reverse_lazy('service_list')


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'app/service_detail.html'


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class ServiceUpdateView(generic.UpdateView):
    model = Service
    fields = ['name', 'description', 'price']
    template_name = 'app/service_form.html'
    success_url = reverse_lazy('service_list')


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class ServiceDeleteView(generic.DeleteView):
    model = Service
    success_url = reverse_lazy('service_list')


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class CampaignListView(generic.ListView):
    model = Campaign
    template_name = 'app/campaign_list.html'


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class CampaignCreateView(generic.CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'app/campaign_form.html'
    success_url = reverse_lazy('campaign_list')


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class CampaignDetailView(generic.DetailView):
    model = Campaign
    template_name = 'app/campaign_detail.html'


@method_decorator(role_required('ADMIN', 'MARKETER'), name='dispatch')
class CampaignUpdateView(generic.UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'app/campaign_form.html'
    success_url = reverse_lazy('campaign_list')


class CampaignDeleteView(generic.DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')


@method_decorator(role_required('ADMIN', 'OPERATOR', 'MANAGER'), name='dispatch')
class LeadListView(generic.ListView):
    queryset = Lead.objects.filter(status='POTENTIAL').all()
    template_name = 'app/lead_list.html'


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class LeadCreateView(generic.CreateView):
    model = Lead
    fields = ['full_name', 'phone', 'email', 'campaign']
    template_name = 'app/lead_form.html'
    success_url = reverse_lazy('lead_list')


@method_decorator(role_required('ADMIN', 'OPERATOR', 'MANAGER'), name='dispatch')
class LeadDetailView(generic.DetailView):
    model = Lead
    template_name = 'app/lead_detail.html'


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class LeadUpdateView(generic.UpdateView):
    model = Lead
    fields = ['full_name', 'phone', 'email', 'campaign']
    template_name = 'app/lead_form.html'
    success_url = reverse_lazy('lead_list')


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class LeadDeleteView(generic.DeleteView):
    model = Lead
    success_url = reverse_lazy('lead_list')


@method_decorator(role_required('ADMIN', 'MANAGER'), name='dispatch')
class LeadActivateView(generic.UpdateView):
    model = Lead
    fields = []

    def test_func(self):
        return self.request.user.role in ['ADMIN', 'MANAGER']

    def form_valid(self, form):
        form.instance.status = 'ACTIVE'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('activeclient_create')


@method_decorator(role_required('ADMIN', 'MANAGER'), name='dispatch')
class LeadDeactivateView(generic.UpdateView):
    model = Lead
    fields = []

    def test_func(self):
        return self.request.user.role in ['ADMIN', 'MANAGER']

    def form_valid(self, form):
        form.instance.status = 'POTENTIAL'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lead_list')



class ActiveClientListView(generic.ListView):
    model = ActiveClient
    template_name = 'app/activeclient_list.html'
    context_object_name = 'clients'
    paginate_by = 10

class ActiveClientDetailView(generic.DetailView):
    model = ActiveClient
    template_name = 'app/activeclient_detail.html'

class ActiveClientCreateView(generic.CreateView):
    model = ActiveClient
    form_class = ActiveClientForm
    template_name = 'app/activeclient_form.html'
    success_url = reverse_lazy('activeclient_list')

    def get_initial(self):
        initial = super().get_initial()
        if 'lead_id' in self.request.GET:
            initial['lead'] = self.request.GET.get('lead_id')
        return initial

class ActiveClientUpdateView(generic.UpdateView):
    model = ActiveClient
    form_class = ActiveClientForm
    template_name = 'app/activeclient_form.html'

    def get_success_url(self):
        return reverse('activeclient_detail', kwargs={'pk': self.object.pk})

class ActiveClientDeleteView(generic.DeleteView):
    model = ActiveClient
    template_name = 'app/activeclient_confirm_delete.html'
    success_url = reverse_lazy('activeclient_list')


@method_decorator(role_required('ADMIN', 'MANAGER'), name='dispatch')
class ContractListView(generic.ListView):
    model = Contract
    template_name = 'app/contract_list.html'


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class ContractCreateView(generic.CreateView):
    model = Contract
    fields = ['name', 'service', 'lead', 'start_date', 'end_date', 'amount', 'document']
    template_name = 'app/contract_form.html'
    success_url = reverse_lazy('contract_list')

    widgets = {
        'start_date': forms.DateInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'autocomplete': 'off'
            },
            format='%d.%m.%Y'
        ),
        'end_date': forms.DateInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'autocomplete': 'off'
            },
            format='%d.%m.%Y'
        ),
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].input_formats = ['%d.%m.%Y', '%Y-%m-%d']
        form.fields['end_date'].input_formats = ['%d.%m.%Y', '%Y-%m-%d']
        return form


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class ContractDetailView(generic.DetailView):
    model = Contract
    template_name = 'app/contract_detail.html'


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class ContractUpdateView(generic.UpdateView):
    model = Contract
    fields = ['name', 'service', 'lead', 'start_date', 'end_date', 'amount', 'document']
    widgets = {
        'start_date': forms.DateInput(attrs={'type': 'text'}),
        'end_date': forms.DateInput(attrs={'type': 'text'}),
    }
    template_name = 'app/contract_form.html'
    success_url = reverse_lazy('contract_list')


@method_decorator(role_required('ADMIN', 'OPERATOR'), name='dispatch')
class ContractDeleteView(generic.DeleteView):
    model = Contract
    success_url = reverse_lazy('contract_list')


def campaign_stats(request):
    campaigns = Campaign.objects.annotate(
        leads_count=Count('lead'),
        active_leads=Count('lead', filter=models.Q(lead__status='ACTIVE')),
        total_income=Sum('lead__contract__amount')
    )
    return render(request, 'app/stats.html', {'campaigns': campaigns})


