from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Group
from .forms import ThreadForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def group_index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'groups': groups })

def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    thread_form = ThreadForm()
    if group.placeholder == " ":
        words = group.name.split()
        word_length = len(words)

        first_word = group.name.split(" ")[0]
        second_word = group.name.split(" ")[1] if word_length >= 2 else "" 
        third_word = group.name.split(" ")[2] if word_length >= 3 else ""
        
        match word_length:
            case word_length if word_length >= 3:
                stock_image = (first_word[0] + second_word[0] + third_word[0])
            case word_length if word_length == 2:
                stock_image = (first_word[0] + second_word[0])
            case word_length if word_length == 1:
                stock_image = (first_word[0])
        
        group.placeholder = stock_image
        group.save()

    if group is not None:
        return render(request, 'groups/detail.html', {'group': group, 'thread_form': thread_form })
    else:
        raise Http404('Group does not exist')

def add_thread(request, group_id):
    form = ThreadForm(request.POST)
    if form.is_valid():
        new_thread = form.save(commit=False)
        new_thread.group_id = group_id
        new_thread.save()
    return redirect('group-detail', group_id = group_id)    


class GroupCreate(CreateView): 
    model = Group
    fields = '__all__'

class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'

class GroupDelete(DeleteView):
    model = Group
    success_url = '/groups/'