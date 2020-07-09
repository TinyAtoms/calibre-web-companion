from .models import Author, Tag, Publisher, Language, Rating, Series


def filters(request):
    unique_authors = Author.objects.all().order_by('sort')
    unique_tags = Tag.objects.all().order_by('name')
    unique_publishers = Publisher.objects.all().order_by('name')
    unique_languages = Language.objects.all()
    unique_ratings = Rating.objects.all().order_by('rating')
    unique_series = Series.objects.all().order_by('sort')

    return {
        "unique_authors": unique_authors,
        "unique_tags": unique_tags,
        "unique_publishers": unique_publishers,
        "unique_languages": unique_languages,
        "unique_ratings": unique_ratings,
        "unique_series": unique_series
    }
