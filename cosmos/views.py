from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from cosmos.models import GMM
from cosmos.forms import GMMCreateForm, GMMUpdateForm, GMMDeleteForm


def index(request):
    return render(request, "index.html")


def resources(request):
    gmm_list = GMM.objects.order_by("-date").all()
    template = loader.get_template("resources.html")
    context = {
        "gmm_list": gmm_list,
    }
    return HttpResponse(template.render(context, request))


class GMMAdd(CreateView):
    form_class = GMMCreateForm
    model = GMM

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Create", css_class="btn-primary"))
        return form


class GMMUpdate(UpdateView):
    form_class = GMMUpdateForm
    model = GMM

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Update", css_class="btn-primary"))
        return form


class GMMDelete(DeleteView):
    form_class = GMMDeleteForm
    model = GMM
    success_url = reverse_lazy("resources")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Delete", css_class="btn-primary"))
        return form
