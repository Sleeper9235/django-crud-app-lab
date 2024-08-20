from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Group, Thread
from .forms import ThreadForm


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args,**kwargs)
        if self.request.user.is_authenticated:
            context['groups'] = Group.objects.filter(user=self.request.user)
            return context
        else: 
            context['groups'] = None
            return context

def about(request): 
    return render(request, 'about.html')

@login_required
def group_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups': groups })

@login_required
def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    thread_form = ThreadForm()
    stock_name = []
    if group.placeholder == " " or group.placeholder != stock_name:
        words = group.name.split()
        word_length = len(words)

        first_word = group.name.split(" ")[0].upper()
        second_word = group.name.split(" ")[1].upper() if word_length >= 2 else "" 
        third_word = group.name.split(" ")[2].upper() if word_length >= 3 else ""
        
        match word_length:
            case word_length if word_length >= 3:
                stock_image = (first_word[0] + second_word[0] + third_word[0])
            case word_length if word_length == 2:
                stock_image = (first_word[0] + second_word[0])
            case word_length if word_length == 1:
                stock_image = (first_word[0])
                
        group.placeholder = stock_image
        group.save()
        
        stock_name.append(group.placeholder)
        
    if group is not None:
        return render(request, 'groups/detail.html', {'group': group, 'thread_form': thread_form })
    else:
        raise Http404('Group does not exist')

@login_required
def add_thread(request, group_id):
    form = ThreadForm(request.POST)
    if form.is_valid():
        new_thread = form.save(commit=False)
        new_thread.group_id = group_id
        new_thread.save()
    return redirect('group-detail', group_id = group_id)    

@login_required
def remove_thread(request, group_id, thread_id):
    group = Group.objects.get(id=group_id)
    thread = Group.objects.get(id=thread_id)
    thread.group.remove
    return redirect('group-detail', group_id=group.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('group-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def thread_update(request, id):
    thread = Thread.objects.get(id = id)
    
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('group-index')
    else:
        form = ThreadForm(instance=thread)
        
    return render(request,
                  'my_app/thread_update.html', 
                  {'form': form})
    
class GroupCreate(LoginRequiredMixin, CreateView): 
    model = Group
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = '__all__'

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/groups/'
    
class ThreadUpdate(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = ['name', 'description']  
    
class ThreadDelete(LoginRequiredMixin, DeleteView):
    model = Thread
    success_url = '/groups/'