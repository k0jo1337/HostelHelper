from django.shortcuts import render
from django.views.generic import TemplateView


class NewsView(TemplateView):
    template_name = 'news/homepage.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)


