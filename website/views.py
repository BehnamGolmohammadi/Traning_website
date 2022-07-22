from django.http import BadHeaderError, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages
from website.models import Contact


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        Form= ContactForm(request.POST)
        if Form.is_valid():
            try:
                handle= Contact()
                handle.Name= "Unknown"
                handle.Email= Form.cleaned_data['Email']
                handle.Subject= Form.cleaned_data["Subject"]
                handle.Message= Form.cleaned_data["Message"]
                handle.save()
                messages.success(request, 'Contact message submitted successfully.')
            except :
                messages.error(request, 'Contact message did not submitted because your input is not valid')
        else:
            messages.error(request, 'Contact message did not submitted because your input is not valid')
    
    Form= ContactForm()
    
    return render(request, 'website/contact.html', {'Form':Form})

def newsletter(request):
    if request.method == 'POST':
        Form= NewsletterForm(request.POST)
        if Form.is_valid:
            try:
                Form.save()
                messages.success(request, 'Well done.\nYou will recive newsletter every days since now.')
            except:
                messages.warning(request, 'Your email format is not valid\nPlease try agian.')
                return HttpResponseRedirect('/#Footer')
        else:
            print(request.POST)
            messages.error(request, 'Your input is not like an E-mail\nPlease try agian.')
    Form= NewsletterForm
    return HttpResponseRedirect('/')

