from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from todo.models import Todo


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'


class TodoCV(CreateView):
    template_name = 'todo/todo_form.html'
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todo:list')


class TodoLV(ListView):
    template_name = 'todo/todo_list.html'
    model = Todo


class TodoDelV(DeleteView):
    template_name = 'todo/todo_confirm_delete.html'
    model = Todo
    success_url = reverse_lazy('todo:list')
