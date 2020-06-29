from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import TemplateView

class IndexTemplateView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def calc_42(request):
    return redirect(reverse('calc', kwargs={'a': 40, 'b': 2}))


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })
