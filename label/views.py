from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from label.models import Label

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from home.views import OwnerOnlyMixin
from label.forms import LabelSearchForm
from django.db.models import Q

class LabelLV(LoginRequiredMixin, ListView):
    model = Label
    paginate_by = 10

    def get_queryset(self, *args, **kwargs): 
        qs = Label.objects.all() 
        search_keyword = self.request.GET.get("qs",None) 
        
        if search_keyword is not None: 
            label_list = Label.objects.filter(Q(number__icontains=search_keyword) | Q(category__icontains=search_keyword)).distinct()
            return label_list 
        else:
            return qs 
        
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        return context
    
    # 참고 : https://woolbro.tistory.com/75
    # 참고 : https://parkhyeonchae.github.io/2020/04/02/django-project-18/

class LabelDV(DetailView):
    model = Label

class LabelCV(LoginRequiredMixin, CreateView):
    template_name = 'label/label_form.html'
    model = Label    
    fields = ('number', 'image', 'category', 'info', 'tags')
    success_url = reverse_lazy('label:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class LabelChangeLV(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label/label_change_list.html'
    paginate_by = 10
    #def get_queryset(self):
    #    return Label.objects.filter(owner=self.request.user)

class LabelUV(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ('number', 'image', 'category', 'info', 'tags')
    success_url = reverse_lazy('label:index')

class LabelDelV(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('label:index')

class TagCloudTV(LoginRequiredMixin, TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(LoginRequiredMixin, ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Label
    paginate_by = 10

    def get_queryset(self):
        return Label.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context