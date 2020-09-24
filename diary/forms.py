from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    mail = forms.EmailField(label='Email')
    title = forms.CharField(label='Title', max_length=30)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=50)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください'

    def send_email(self):
        subject = 'title'
        mail_to = ["sneky.56347sk@icloud.com",]
        mail_from = "mail@gmail.com"
        body = 'message!!'
        mail_msg = EmailMessage(subject=subject, from_email=mail_from, to=mail_to, body=body)
        mail_msg.send()