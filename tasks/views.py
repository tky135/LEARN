from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
# Create your views here.
def show(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/show.html', {
        'tasks': request.session['tasks']
    })
def addpage(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        task = form.data['task']
        request.session['tasks'] += [task]
        return HttpResponseRedirect(reverse('show'))
    else:
        form = NewTaskForm()
        return render(request, 'tasks/addpage.html', {
            'form' : form
        })
