from inertia import lazy, render
from .models import Event
from django.views import View
from django.core.paginator import Paginator
from asgiref.sync import sync_to_async


# 2. Event view is created
class EventView(View):
    async def get(self, request):
        events = Paginator([event async for event in Event.objects.all()], 10)

        try: 
            # Get the page number from the query string
            page_num = int(request.GET.get('page') if request.GET.get('page') else 1)
            # If page_num is greater than the total number of pages, raise a ValueError
            if page_num > events.num_pages or page_num < 1:
                raise ValueError
            # Get all events from the database
            # Using inertia, render events.svelte, and send it the events object through props.
            return render(request, 'events', props={
                "events": lazy(lambda: events.page(page_num).object_list),
                "num_pages": lazy(lambda: events.num_pages),
            })
        except ValueError:
            # Render a 404 page
            return render(request, '404')

class ExampleView(View):
    async def get(self, request):
        return render(request, 'example')