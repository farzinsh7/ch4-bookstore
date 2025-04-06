from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    permission_required = "books.special_status"
    
    def get_queryset(self):
        return Book.objects.prefetch_related('reviews__author',).all()
    

class SearchResultsListView(ListView):
    model = Book
    template_name = "books/search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))