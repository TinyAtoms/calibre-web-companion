from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Comment, Rating, BookAuthorLink, Publisher, Tag, BookTagLink, BookRatingLink, Data
from django.http import HttpResponseRedirect
from .forms import SearchForm
from django.db import models
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request,'accounts/index.html')

    
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'registration/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

class SearchView(generic.TemplateView):
    template_name = 'search.html'


class ResultsView(generic.ListView):  # no clue if this is secure.
    # according to this https://stackoverflow.com/questions/13574043/how-do-django-forms-sanitize-text-input-to-prevent-sql-injection-xss-etc
    # it is
    model = Book
    template_name = 'results.html'

    def get_queryset(self):  # new
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        return Book.objects.filter(
            Q(sort__icontains=title) and Q(author_sort__icontains=author)
        )


class AuthorListView(generic.ListView):
    model = Author


class BookListView(generic.ListView):
    model = Book


class PublisherListView(generic.ListView):
    model = Publisher


class RatingListView(generic.ListView):
    model = Rating


class TagListView(generic.ListView):
    model = Tag


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BookAuthorLink.objects.filter(author=context["object"].id)
        context['books'] = sorted(
            [b.book for b in books.all()],  key=lambda x: x.title)
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        try:
            context['comment'] = Comment.objects.get(
                book=context["object"].id).text
        except:
            pass
        context["imgpath"] = context["object"].path + "/cover.jpg"
        download = Data.objects.get(book=context["object"].id)
        context["download"] = f"{context['object'].path}/{download.name}.{download.format}"
        return context


class PublisherDetailView(generic.DetailView):
    model = Publisher


class RatingDetailView(generic.DetailView):
    model = Rating

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RatingDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BookRatingLink.objects.filter(rating=context["object"].id)
        context['books'] = sorted(
            [b.book for b in books.all()], key=lambda x: x.title)
        return context


class TagDetailView(generic.DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(TagDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BookTagLink.objects.filter(tag=context["object"].id)
        context['books'] = sorted(
            [b.book for b in books.all()],  key=lambda x: x.title)
        return context
