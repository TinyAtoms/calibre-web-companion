from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('publishers/', views.PublisherListView.as_view(), name='publishers'),
    path('ratings/', views.RatingListView.as_view(), name='ratings'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('series/', views.SeriesListView.as_view(), name='series'),


    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail-view'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail-view'),
    path('publisher/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail-view'),
    path('rating/<int:pk>', views.RatingDetailView.as_view(), name='rating-detail-view'),
    path('series/<int:pk>', views.SeriesDetailView.as_view(), name='series-detail-view'),
    path('tag/<int:pk>', views.TagDetailView.as_view(), name='tag-detail-view'),

    path('results/', views.ResultsView.as_view(), name='results'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('accounts/sign_up/',views.sign_up,name="sign-up")


]