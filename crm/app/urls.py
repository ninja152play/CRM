from django.urls import path
from .views import *

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/create/', CampaignCreateView.as_view(), name='campaign_create'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaigns/<int:pk>/update/', CampaignUpdateView.as_view(), name='campaign_update'),
    path('campaigns/<int:pk>/delete/', CampaignDeleteView.as_view(), name='campaign_delete'),

    path('leads/', LeadListView.as_view(), name='lead_list'),
    path('leads/create/', LeadCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('leads/<int:pk>/activate/', LeadActivateView.as_view(), name='lead_activate'),
    path('leads/<int:pk>/deactivate/', LeadDeactivateView.as_view(), name='lead_deactivate'),

    path('active-clients/', ActiveClientListView.as_view(), name='activeclient_list'),
    path('active-clients/add/', ActiveClientCreateView.as_view(), name='activeclient_create'),
    path('active-clients/<int:pk>/', ActiveClientDetailView.as_view(), name='activeclient_detail'),
    path('active-clients/<int:pk>/edit/', ActiveClientUpdateView.as_view(), name='activeclient_update'),
    path('active-clients/<int:pk>/delete/', ActiveClientDeleteView.as_view(), name='activeclient_delete'),

    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/create/', ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/<int:pk>/update/', ContractUpdateView.as_view(), name='contract_update'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),

    path('statistics/', campaign_stats, name='payment_list'),
]