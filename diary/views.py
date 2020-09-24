from django.views.generic import TemplateView, FormView
from .forms import InquiryForm
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')
    
    def form_valid(self, form):
        form.send_email()
        return super().form_invalid(form)