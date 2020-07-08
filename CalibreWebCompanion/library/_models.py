# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)
    link = models.TextField()

    class Meta:
        managed = False
        db_table = 'authors'


class Comments(models.Model):
    book = models.ForeignField("Book")
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Data(models.Model):
    book = models.IntegerField()
    format = models.TextField()
    uncompressed_size = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'data'


class Identifiers(models.Model):
    book = models.IntegerField()
    type = models.TextField()
    val = models.TextField()

    class Meta:
        managed = False
        db_table = 'identifiers'


class Languages(models.Model):
    lang_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'languages'


class Publishers(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishers'


class Ratings(models.Model):
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class Series(models.Model):
    name = models.TextField()
    sort = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'


class Tags(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tags'


class Books(models.Model):
    title = models.TextField()
    sort = models.TextField(blank=True, null=True)
    # This field type is a guess.
    timestamp = models.TextField(blank=True, null=True)
    # This field type is a guess.
    pubdate = models.TextField(blank=True, null=True)
    series_index = models.FloatField()
    author_sort = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    lccn = models.TextField(blank=True, null=True)
    path = models.TextField()
    flags = models.IntegerField()
    uuid = models.TextField(blank=True, null=True)
    has_cover = models.BooleanField(blank=True, null=True)
    last_modified = models.TextField()  # This field type is a guess.
    authors = models.ManyToManyField(
        Authors,
        through='BooksAuthorsLink',
        through_fields=('book', 'author'))
    languages = models.ManyToManyField(
        Languages,
        through='BooksLanguagesLink',
        through_fields=('book', 'lang_code'))
    publishers = models.ManyToManyField(
        Publishers,
        through='BooksPublishersLink',
        through_fields=('book', 'publisher'))
    series = models.ManyToManyField(
        Series,
        through='BooksSeriesLink',
        through_fields=('book', 'series'))
    tags = models.ManyToManyField(
        Tags,
        through='BooksTagsLink',
        through_fields=('book', 'tag'))

    class Meta:
        managed = False
        db_table = 'books'


class BooksAuthorsLink(models.Model):
    book = models.ForeignKey(db_column="book")
    author = models.ForeignKey(db_column="author")

    class Meta:
        managed = False
        db_table = 'books_authors_link'


class BooksLanguagesLink(models.Model):
    book = models.ForeignKey(db_colum="book")
    lang_code = models.ForeignKey(db_column="lang_code")
    item_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_languages_link'


class BooksPublishersLink(models.Model):
    book = models.ForeignKey(db_column="book")
    publisher = models.ForeignKey(db_column="publisher")

    class Meta:
        managed = False
        db_table = 'books_publishers_link'


# class BooksRatingsLink(models.Model): # TODO add this somehow
#     book = models.ForeignKey(db_column="book")
#     rating = models.IntegerField()
#     class Meta:
#         managed = False
#         db_table = 'books_ratings_link'


class BooksSeriesLink(models.Model):
    book = models.ForeignKey(db_column="book")
    series = models.ForeignKey(db_column="series")

    class Meta:
        managed = False
        db_table = 'books_series_link'


class BooksTagsLink(models.Model):
    book = models.ForeignKey(db_column="book")
    tag = models.ForeignKey(db_column="tag")

    class Meta:
        managed = False
        db_table = 'books_tags_link'


# class BooksPluginData(models.Model):
#     book = models.IntegerField()
#     name = models.TextField()
#     val = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'books_plugin_data'


# class ConversionOptions(models.Model):
#     format = models.TextField()
#     book = models.IntegerField(blank=True, null=True)
#     data = models.BinaryField()
#
#     class Meta:
#         managed = False
#         db_table = 'conversion_options'
#
# class LibraryId(models.Model):
#     uuid = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'library_id'
#
# class CustomColumns(models.Model):
#     label = models.TextField()
#     name = models.TextField()
#     datatype = models.TextField()
#     mark_for_delete = models.BooleanField()
#     editable = models.BooleanField()
#     display = models.TextField()
#     is_multiple = models.BooleanField()
#     normalized = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'custom_columns'
#
# class Preferences(models.Model):
#     key = models.TextField()
#     val = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'preferences'
#
# class Feeds(models.Model):
#     title = models.TextField()
#     script = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'feeds'
#
#
# class LastReadPositions(models.Model):
#     book = models.IntegerField()
#     format = models.TextField()
#     user = models.TextField()
#     device = models.TextField()
#     cfi = models.TextField()
#     epoch = models.FloatField()
#     pos_frac = models.FloatField()
#
#     class Meta:
#         managed = False
#         db_table = 'last_read_positions'


# class MetadataDirtied(models.Model):
#     book = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'metadata_dirtied'
