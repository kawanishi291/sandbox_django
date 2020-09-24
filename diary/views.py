from django.views.generic import TemplateView, FormView
from .forms import InquiryForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm