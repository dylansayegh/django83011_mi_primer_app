from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/pages_list.html'
    context_object_name = 'pages'
    ordering = ['-fecha_creacion']  # Mostrar más recientes primero

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')
    
    def get_queryset(self):
        # Solo permitir editar páginas del usuario actual
        return Page.objects.filter(autor=self.request.user)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')
    
    def get_queryset(self):
        # Solo permitir borrar páginas del usuario actual
        return Page.objects.filter(autor=self.request.user)
