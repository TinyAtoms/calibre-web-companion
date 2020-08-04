from .models import Author, Tag, Publisher, Language, Rating, Series
from django.db.models import Count
import logging

logger = logging.getLogger(__name__)

def filters(request):
    # unique_authors = Author.objects.all().order_by('sort')
    # unique_tags = Tag.objects.all().order_by('name')
    # unique_publishers = Publisher.objects.all().order_by('name')
    # unique_ratings = Rating.objects.all().order_by('rating')
    # unique_languages = Language.objects.all()
    # unique_series = Series.objects.all().order_by('sort')
    # unique_authors = Author.objects.annotate(num_books=Count('book')).order_by('sort')
    unique_authors = Author.objects.only('name', "id").annotate(num_books=Count('book')).order_by('name')
    unique_tags = Tag.objects.annotate(num_books=Count('book')).order_by('name')
    unique_publishers = Publisher.objects.annotate(num_books=Count('book')).order_by('name')
    unique_languages = Language.objects.annotate(num_books=Count('book')).order_by('lang_code')
    unique_ratings = Rating.objects.annotate(num_books=Count('book'))
    unique_series = Series.objects.annotate(num_books=Count('book')).order_by('sort')
    

    return {
        "unique_authors": unique_authors,
        "unique_tags": unique_tags,
        "unique_publishers": unique_publishers,
        "unique_languages": unique_languages,
        "unique_ratings": unique_ratings,
        "unique_series": unique_series
    }
