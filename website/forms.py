from django import forms

from website.models import Contact, Newsletter

class ExampleForm(forms.Form):
    Name= forms.CharField(max_length= 255)
    Email= forms.EmailField()
    Subject= forms.CharField(max_length= 255)
    Message= forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    Name= forms.CharField(max_length= 255)
    Email= forms.EmailField()
    Subject= forms.CharField(max_length= 255, required= False)
    Message= forms.CharField(widget=forms.Textarea)

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"