from django.http import HttpResponse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView


# class Home(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Welcome to Traveler Management")

class Home(TemplateView):
    template_name = 'common/home.html'
    extra_context = {'welcome_message': "Welcome to the home page of Asya's website!"}

    def get_context_data(self, **kwargs):
        kwargs.update({'current_date': now()})
        return super().get_context_data(**kwargs)

class Redirect(RedirectView):
    # url = "https://softuni.bg/trainings/5432/django-basics-september-2026#lesson-108916"
    pattern_name = 'common:home'