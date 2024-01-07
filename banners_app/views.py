from inertia import lazy, render
from .models import Event
from django.views import View


def example_view(request):
    return render(request, "Example", props={"inertia": True})

# 2. Event view is created
class EventView(View):
    def get(self, request):
        # Get all events from the database
        # Using inertia, render events.svelte, and send it the events object through props.
        return render(request, 'events', props={
            "events": lazy(lambda: Event.objects.all()),
        })
