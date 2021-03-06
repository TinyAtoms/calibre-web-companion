from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Comment, Rating, BookAuthorLink, Publisher, Tag, BookTagLink, BookRatingLink, Data, Identifier, Series
from django.http import HttpResponseRedirect
from .forms import SearchForm, UserCreationForm
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

# might be helpful for vary headers later
from django.utils.decorators import method_decorator


@login_required
def index(request):
    return render(request, 'accounts/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)


class SearchView(generic.TemplateView):
    template_name = 'search.html'

    def dispatch(self, *args, **kwargs):
        return super(SearchView, self).dispatch(*args, **kwargs)


class ResultsView(generic.ListView):  # no clue if this is secure.
    # according to this https://stackoverflow.com/questions/13574043/how-do-django-forms-sanitize-text-input-to-prevent-sql-injection-xss-etc
    # it is
    model = Book
    template_name = 'results.html'

    def dispatch(self, *args, **kwargs):
        return super(ResultsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):  # new
        title = self.request.GET.get('title')
        author = self.request.GET.get('author')
        identifier = self.request.GET.get("identifier")
        generic = self.request.GET.get("generic")
        books = Book.objects.prefetch_related("tags", "ratings")
        if title:
            books = books.filter(sort__icontains=title)
        if author:
            books = books.filter(author_sort__icontains=author)
        if identifier:
            books = books.filter(identifier__val=identifier)
        if generic:
            books = books.filter(
                Q(sort__icontains=generic) |
                Q(author_sort__icontains=generic) |
                Q(identifier__val=generic)
            )
        return books


class AuthorListView(generic.ListView):
    model = Author

    def dispatch(self, *args, **kwargs):
        return super(AuthorListView, self).dispatch(*args, **kwargs)


class BookListView(generic.ListView):
    model = Book

    def dispatch(self, *args, **kwargs):
        return super(BookListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        # Annotate the books with ratings, tags, etc
        # books = Book.objects.annotate(
        queryset = Book.objects.prefetch_related("tags", "ratings")
        return queryset


class PublisherListView(generic.ListView):
    model = Publisher

    def dispatch(self, *args, **kwargs):
        return super(PublisherListView, self).dispatch(*args, **kwargs)


class RatingListView(generic.ListView):
    model = Rating

    def dispatch(self, *args, **kwargs):
        return super(RatingListView, self).dispatch(*args, **kwargs)


class SeriesListView(generic.ListView):  # make url entry and template, sometime
    model = Series

    def dispatch(self, *args, **kwargs):
        return super(SeriesListView, self).dispatch(*args, **kwargs)


class TagListView(generic.ListView):
    model = Tag

    def dispatch(self, *args, **kwargs):
        return super(TagListView, self).dispatch(*args, **kwargs)


class AuthorDetailView(generic.DetailView):
    model = Author

    def dispatch(self, *args, **kwargs):
        return super(AuthorDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.prefetch_related("tags", "ratings")
        books = books.filter(authors=context["object"].id)
        context['books'] = sorted(books,  key=lambda x: x.title)
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def dispatch(self, *args, **kwargs):
        return super(BookDetailView, self).dispatch(*args, **kwargs)

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
        context["download"] = f"{context['object'].path}/{download.name}.{download.format.lower()}"
        return context


class PublisherDetailView(generic.DetailView):
    model = Publisher

    def dispatch(self, *args, **kwargs):
        return super(PublisherDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.prefetch_related("tags", "ratings")
        books = books.filter(publishers=context["object"].id)
        context['books'] = sorted(books,  key=lambda x: x.title)
        return context


class RatingDetailView(generic.DetailView):
    model = Rating

    def dispatch(self, *args, **kwargs):
        return super(RatingDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RatingDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.prefetch_related("tags", "ratings")
        books = books.filter(ratings=context["object"].id)
        context['books'] = sorted(books,  key=lambda x: x.title)
        return context


class TagDetailView(generic.DetailView):
    model = Tag

    def dispatch(self, *args, **kwargs):
        return super(TagDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(TagDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.prefetch_related("tags", "ratings")
        books = books.filter(tags=context["object"].id)
        context['books'] = sorted(books,  key=lambda x: x.title)
        return context


class SeriesDetailView(generic.DetailView):
    model = Series

    def dispatch(self, *args, **kwargs):
        return super(SeriesDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SeriesDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = Book.objects.prefetch_related("tags", "ratings")
        books = books.filter(series=context["object"].id)
        context['books'] = sorted(books,  key=lambda x: x.title)
        return context
