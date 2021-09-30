from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Gear

class GearListView(ListView):
    model = Gear
    template_name = 'gear_list.html'

class GearDetailView(DetailView):
    model = Gear
    template_name = 'gear_detail.html'

class GearCreateView(CreateView):
    model = Gear
    template_name = 'gear_create.html'
    fields = ['name', 'purchaser', 'description']

class GearUpdateView(UpdateView):
    model = Gear
    template_name = 'gear_update.html'
    fields = ['name', 'purchaser', 'description']

class GearDeleteView(DeleteView):
    model = Gear
    template_name = 'gear_delete.html'
    success_url = reverse_lazy('gear_list')

class AboutView(TemplateView):
    model = Gear
    template_name = 'about.html'

