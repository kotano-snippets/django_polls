from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from hello_django.calc.models import History
# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        summ = a + b
        History(value=summ).save()
        return render(
            request, 'calc/index.html',
            context={'num1': a, 'num2': b, 'summ': summ}
        )
        # return HttpResponse('Sum of {} and {} is {}'.format(a, b, summ))
        # return HttpResponse('{} + {} = {}'.format(a, b, summ))


class HistoryView(View):

    def get(self, request, *args, **kwargs):
        last_ten = History.objects.all().order_by('-timestamp')[:10]

        return render(request, 'calc/history.html', context={'story_list': last_ten})


# def index(request):
#     return HttpResponse('calc')
