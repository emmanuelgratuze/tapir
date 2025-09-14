from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class UserDashboardView(LoginRequiredMixin,TemplateView):
    template_name = "shifts/user_dashboard.html"