# Generated by Django 3.0.7 on 2020-07-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sort', models.TextField(blank=True, null=True)),
                ('link', models.TextField()),
            ],
            options={
                'db_table': 'authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('sort', models.TextField(blank=True, null=True)),
                ('timestamp', models.TextField(blank=True, null=True)),
                ('pubdate', models.TextField(blank=True, null=True)),
                ('series_index', models.FloatField()),
                ('author_sort', models.TextField(blank=True, null=True)),
                ('isbn', models.TextField(blank=True, null=True)),
                ('lccn', models.TextField(blank=True, null=True)),
                ('path', models.TextField()),
                ('flags', models.IntegerField()),
                ('uuid', models.TextField(blank=True, null=True)),
                ('has_cover', models.BooleanField(blank=True, null=True)),
                ('last_modified', models.TextField()),
            ],
            options={
                'db_table': 'books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookAuthorLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'books_authors_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookLanguageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_order', models.IntegerField()),
            ],
            options={
                'db_table': 'books_languages_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookPublisherLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'books_publishers_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookRatingLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'books_ratings_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookSeriesLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'books_series_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookTagLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'books_tags_link',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.IntegerField()),
                ('type', models.TextField()),
                ('val', models.TextField()),
            ],
            options={
                'db_table': 'identifiers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_code', models.TextField()),
            ],
            options={
                'db_table': 'languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sort', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'publishers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ratings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Authors',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='BooksAuthorsLink',
        ),
        migrations.DeleteModel(
            name='BooksLanguagesLink',
        ),
        migrations.DeleteModel(
            name='BooksPublishersLink',
        ),
        migrations.DeleteModel(
            name='BooksRatingsLink',
        ),
        migrations.DeleteModel(
            name='BooksSeriesLink',
        ),
        migrations.DeleteModel(
            name='BooksTagsLink',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Identifiers',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='Publishers',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
