from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import InquiryForm, DiaryCreateForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Diary

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)

class DiaryDetail(DetailView):
    model = Diary
    template_name = "diary_detail.html"
    
class DiaryList(ListView):
    model = Diary
    template_name = "diary_list.html"
    
class DiaryCreate(CreateView):
    model = Diary
    form_class = DiaryCreateForm
    template_name = "diary_create.html"
    success_url = reverse_lazy('diary:diary_list')
    
class DiaryUpdate(UpdateView):
    model = Diary
    form_class = DiaryCreateForm
    template_name = "diary_update.html"
    success_url = reverse_lazy('diary:diary_list')
    
class DiaryDelete(DeleteView):
    model = Diary
    template_name = "diary_delete.html"
    success_url = reverse_lazy('diary:diary_list')