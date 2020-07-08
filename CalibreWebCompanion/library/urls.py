from django.urls import path
from . import views



urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('publishers/', views.PublisherListView.as_view(), name='publishers'),
    path('ratings/', views.RatingListView.as_view(), name='ratings'),
    path('tags/', views.TagListView.as_view(), name='tags'),

    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail-view'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail-view'),
    path('publisher/<int:pk>', views.PublisherDetailView.as_view(), name='publisher-detail-view'),
    path('rating/<int:pk>', views.RatingDetailView.as_view(), name='rating-detail-view'),
    path('tag/<int:pk>', views.TagDetailView.as_view(), name='tag-detail-view'),


]