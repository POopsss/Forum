from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from forum.models import *


def red(request):
    template_name = "user.html"
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    context = {
        'qwe': ('qwe', 'ads', 'zxc'),
        'asd': FUser.objects.get(email=request.user),
    }
    return render(request, template_name, context)
    # return redirect('/accounts/login/')


# class User(TemplateView):
#
#     template_name = "user.html"
#     context_object_name = 'user'
#
#     def get_context_data(self, **kwargs):
#         red()
        # context = super().get_context_data(**kwargs)
        # try:
        #     context['user'] = FUser.objects.get(email=self.request.user)
        # except:
        #     return context
        # return context