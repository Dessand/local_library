from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Book

class AuthorModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		#Set up non-modified objects used by all test methods
		Author.objects.create(first_name='Big', last_name='Bob')

	def test_first_name_label(self):
		author=Author.objects.get(id=1)
		field_label = author._meta.get_field('first_name').verbose_name
		self.assertEquals(field_label,'first name')

	def test_date_of_death_label(self):
		author=Author.objects.get(id=1)
		field_label = author._meta.get_field('date_of_death').verbose_name
		self.assertEquals(field_label,'Died')

	def test_first_name_max_length(self):
		author=Author.objects.get(id=1)
		max_length = author._meta.get_field('first_name').max_length
		self.assertEquals(max_length,100)

	def test_get_absolute_url(self):
		author=Author.objects.get(id=1)
		#This will also fail if the urlconf is not defined.
		self.assertEquals(author.get_absolute_url(),'/catalog/author/1')

class BookModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		#Set up non-modified objects used by all test methods
		Book.objects.create(title = 'Таракан', summary = 'Просто книга', isbn = '3348219565834')

	def test_title_label(self):
		book = Book.objects.get(id=1)
		field_label = book._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')

	def test_language_label(self):
		book = Book.objects.get(id=1)
		field_label = book._meta.get_field('language').verbose_name
		self.assertEquals(field_label, 'language')

	def test_get_absolute_url(self):
		book = Book.objects.get(id=1)
		self.assertEquals(book.get_absolute_url(),'/catalog/book/1')
		
