from django.shortcuts import render
from django.views import generic
from .models import Authors, Books, Comments, Ratings, BooksAuthorsLink, Publishers, Tags, BooksTagsLink, BooksRatingsLink, Data
from django.http import HttpResponseRedirect
# from .forms import SearchForms


# def get_results(request): # TODO this might not be what i want
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = SearchForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             books = Books.objects.all()
#             if form.title:
#                 books.filter(sort_icontains=form.title)
#             if form.author:
#                 books.filter(author_sort_icontains=form.author)
      
#             return HttpResponseRedirect('/results/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})

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
        context['books'] = context['books'] = sorted([b.book for b in books.all()],  key=lambda x: x.title)
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
        context['books'] = sorted([b.book for b in books.all()], key=lambda x: x.title)
        return context


class TagDetailView(generic.DetailView):
    model = Tags

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(TagDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        books = BooksTagsLink.objects.filter(tag=context["object"].id)
        context['books'] = sorted([b.book for b in books.all()],  key=lambda x: x.title)
        return context
