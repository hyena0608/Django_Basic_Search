from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Crew
from django.db.models import Q # new

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Crew
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Crew.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list