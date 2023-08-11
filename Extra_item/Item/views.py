from django.shortcuts import render, get_object_or_404
from . models import Objec, Grup
from django.views.generic import ListView, DetailView
from random import sample as sm, shuffle as sh, choice as ch


def show_all_objec(request):
    objecs = Objec.objects.order_by('grup')
    return render(request, 'Item/all_objecs.html', {
        'objecs': objecs,
    })


class Show_all_grups(ListView):
    template_name = 'Item/all_grups.html'
    model = Grup
    context_object_name = 'grups'


class DetailGrup(DetailView):
    template_name = 'Item/one_grup.html'
    model = Grup
    context_object_name = 'grup'


def random_objecs(request, slug, n):
    grup = get_object_or_404(Grup, slug=slug)
    objecs = grup.objecs.all()
    one_false = ch(list(filter(lambda x: not x.ident, objecs)))
    many_true = sm(list(filter(lambda x: x.ident, objecs)), n - 1)
    many_true.append(one_false)
    sh(many_true)
    random_objecs = sm(many_true, n)
    return render(request, 'Item/random_objecs.html', {
        'random_objecs': random_objecs,
        'grup': grup,
    })
