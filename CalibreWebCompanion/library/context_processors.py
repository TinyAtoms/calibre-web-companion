from .models import Authors, Tags, Publishers, Languages, Ratings, Series


def filters(request):
    unique_authors = Authors.objects.all().order_by('sort')
    unique_tags = Tags.objects.all().order_by('name')
    unique_publishers = Publishers.objects.all().order_by('name')
    unique_languages = Languages.objects.all()
    unique_ratings = Ratings.objects.all().order_by('rating')
    unique_series = Series.objects.all().order_by('sort')

    return {
        "unique_authors": unique_authors,
        "unique_tags": unique_tags,
        "unique_publishers": unique_publishers,
        "unique_languages": unique_languages,
        "unique_ratings": unique_ratings,
        "unique_series": unique_series
    }
