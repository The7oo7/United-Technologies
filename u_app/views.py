from django.shortcuts import render, redirect
from .models import  *
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages


class Create(CreateView):
    fields = ('image','name', 'description')
    model = Card
    success_url = reverse_lazy('django:home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class UpdateViews(UpdateView):
    model = Card
    fields = ('image','name', 'description')
    success_url = reverse_lazy('django:home')


def index(request):
    context={}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        UserMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.info(request, 'Your message has successfully been sent to the manager!')
        return redirect('django:home')
    context["dataset"] = Card.objects.all()
    return render(request, 'index.html',context)
