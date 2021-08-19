from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from actor.models import Actor

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from home.views import OwnerOnlyMixin
from actor.forms import ActorSearchForm
from django.db.models import Q

class ActorLV(LoginRequiredMixin, ListView):
    model = Actor
    paginate_by = 10

    def get_queryset(self, *args, **kwargs): 
        qs = Actor.objects.all() 
        search_keyword = self.request.GET.get("qs",None) 
        
        if search_keyword is not None: 
            actor_list = Actor.objects.filter(Q(name__icontains=search_keyword) | Q(name_jpn__icontains=search_keyword) | Q(name_eng__icontains=search_keyword)).distinct()
            return actor_list 
        else:
            return qs 
        
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        return context
    
    # 참고 : https://woolbro.tistory.com/75
    # 참고 : https://parkhyeonchae.github.io/2020/04/02/django-project-18/
    
class ActorDV(DetailView):
    model = Actor

class ActorCV(LoginRequiredMixin, CreateView):
    model = Actor
    fields = ('name', 'name_jpn', 'name_eng', 'image', 'info')
    success_url = reverse_lazy('actor:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ActorChangeLV(LoginRequiredMixin, ListView):
    model = Actor
    template_name = 'actor/actor_change_list.html'
    paginate_by = 10
    #def get_queryset(self):
    #    return Actor.objects.filter(owner=self.request.user)

    def get_queryset(self, *args, **kwargs): 
        qs = Actor.objects.all() 
        search_keyword = self.request.GET.get("qs",None) 
        
        if search_keyword is not None: 
            actor_list = Actor.objects.filter(Q(name__icontains=search_keyword) | Q(name_jpn__icontains=search_keyword) | Q(name_eng__icontains=search_keyword)).distinct()
            return actor_list 
        else:
            return qs 

class ActorUV(LoginRequiredMixin, UpdateView):
    model = Actor
    fields = ('name', 'name_jpn', 'name_eng', 'image', 'info')
    success_url = reverse_lazy('actor:index')

class ActorDelV(LoginRequiredMixin, DeleteView):
    model = Actor
    success_url = reverse_lazy('actor:index')

class SearchActorFormView(FormView):
    form_class = ActorSearchForm
    template_name = 'actor/actor_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        actor_list = Actor.objects.filter(Q(name__icontains=searchWord) | Q(name_jpn__icontains=searchWord) | Q(name_eng__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = actor_list
        
        return render(self.request, self.template_name, context)