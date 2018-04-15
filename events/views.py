from django.shortcuts import render, redirect
from .forms import eventForm
from django.http import HttpResponseRedirect
from .models import Events
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


def eventsList(request):
    events = Events.objects.all()
    return render(request, 'events/eventsList.html', {'events': events})

def createEvent(request):
    if request.method == 'POST':
        event_form = eventForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            return redirect('/')
    else:
        event_form = eventForm()
        return render(request, 'events/addEvent.html', {'event': event_form})

def eventDetails(request, pk):
    event = Events.objects.get(pk=pk)
    return render(request, 'events/eventDetails.html', {'event': event})

class EventUpdateView(UpdateView):
    queryset = Events.objects.all()
    form_class = eventForm
    model = Events
    template_name = 'events/eventUpdate.html'

class EventDeleteView(DeleteView):
    model = Events
    queryset = Events.objects.all()
    context_object_name = 'item'
    template_name = 'events/eventDelete.html'
    success_url = reverse_lazy('home')
