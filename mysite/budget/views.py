from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import Person
from django.http import Http404, HttpResponseRedirect
from .forms import NameForm, UploadFileForm

from .back import handle_uploaded_file

def index(request):
    persons = Person.objects.all()

    context = {
        'persons': persons,
    }
    return render(request, 'budget/index.html', context)

class DetailView(TemplateView):
    def get(self, request, person_id):
        try:
            persons = Person.objects.all()
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
        
        context = {
            'persons': persons,
            'person': person,
            'first_name': person.first_name, 
            'last_name': person.last_name,
            'income': person.income,

        }
        return render(request, 'budget/detail.html', context)


class PersonView(TemplateView):
    def get(self, request):
        persons = Person.objects.all()

        context = {
            'persons': persons,
        }
        return render(request, 'budget/person.html', context)

class AddView(TemplateView):
    template = 'budget/add.html'

    def get(self, request):
        form = NameForm
        context = {'form': form}
        return render(request, self.template, context)


    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            form = NameForm()
            p = Person(first_name=text['first_name'], last_name=text['last_name'], income = text['income'])
            p.save()
        context = {
            'form': form,
            'text': text,
            }

        return render(request, self.template, context)


class UploadView(TemplateView):
    template_name = 'budget/upload.html'

    def get(self, request):
        form = UploadFileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/upload')
        else:
            form = UploadFileForm()
        return render(request, self.template_name, {'form': form})
