from django.views import View
from inertia import render
import logging
from .models import Servant

class Index(View):
    def get(self, request):
        logger = logging.getLogger("Index")
        logger.debug("DEBUG")
        logger.info("INFO")
        logger.error("ERROR")
        logger.warning("WARNING")
        logger.critical("CRITICAL HIT! ")
        return render(request, 'sample_app/index', props={
            'events': [
                'Milano',
                'Napoli',
            ],
            'page_name': 'Home'
        })


class About(View):
    def get(self, request):
        servants = Servant.objects.all()
        servant_names = [str(servant) for servant in servants]
        return render(request, 'sample_app/about', props={
            'events': servant_names,
            'page_name': 'About us'
        })
