from inertia import lazy, render
from .models import Event
from django.views import View
from django.core.paginator import Paginator
from asgiref.sync import sync_to_async


# 2. Event view is created
class EventView(View):
    async def get(self, request):
        events = Paginator([event async for event in Event.objects.all()], 10)

        # Get all events from the database
        # Using inertia, render events.svelte, and send it the events object through props.
        return render(request, 'events', props={
            "events": lazy(lambda: events.page(min(int(request.GET.get('page') if request.GET.get('page') else 1), events.num_pages)).object_list),
        })

class ExampleView(View):
    async def get(self, request):
        return render(request, 'example')