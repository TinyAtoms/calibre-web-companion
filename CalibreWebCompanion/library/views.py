from django.shortcuts import render
from django.views import generic
from .models import Authors, Books, Comments, Ratings, BooksAuthorsLink, Publishers, Tags, BooksTagsLink, BooksRatingsLink, Data
from django.http import HttpResponseRedirect
from .forms import SearchForm
from django.db import models
from django.db.models import Q

class SearchView(generic.TemplateView):
    template_name = 'search.html'

class ResultsView(generic.ListView): # no clue if this is secure. 
    # according to this https://stackoverflow.com/questions/13574043/how-do-django-forms-sanitize-text-input-to-prevent-sql-injection-xss-etc 
    # it is
    model = Books
    template_name = 'results.html'
    def get_queryset(self): # new
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        return Books.objects.filter(
            Q(sort__icontains=title) and Q(author_sort__icontains=author)
        )

class AuthorListView(generic.ListView):
    model = Authors


class BookListView(generic.ListView):
    model = Books


class PublisherListView(generic.ListView):
    model = Publishers


class RatingListView(generic.ListView):
    model = Ratings


class TagListView(generic.ListView):
    model = Tags


class AuthorDetailView(generic.DetailView):
    model = Authors

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BooksAuthorsLink.objects.filter(author=context["object"].id)
        context['books'] = context['books'] = sorted(
            [b.book for b in books.all()],  key=lambda x: x.title)
        return context


class BookDetailView(generic.DetailView):
    model = Books

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        try:
            context['comment'] = Comments.objects.get(
                book=context["object"].id).text
        except:
            pass
        context["imgpath"] = context["object"].path + "/cover.jpg"
        download = Data.objects.get(book=context["object"].id)
        context["download"] = f"{context['object'].path}/{download.name}.{download.format}"
        return context


class PublisherDetailView(generic.DetailView):
    model = Publishers


class RatingDetailView(generic.DetailView):
    model = Ratings

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RatingDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BooksRatingsLink.objects.filter(rating=context["object"].id)
        context['books'] = sorted(
            [b.book for b in books.all()], key=lambda x: x.title)
        return context


class TagDetailView(generic.DetailView):
    model = Tags

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(TagDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BooksTagsLink.objects.filter(tag=context["object"].id)
        context['books'] = sorted(
            [b.book for b in books.all()],  key=lambda x: x.title)
        return context
