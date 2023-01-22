from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AppealView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/login/'
