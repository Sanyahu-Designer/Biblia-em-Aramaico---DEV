"""Service for handling Bible navigation and retrieval operations."""
from django.db.models import QuerySet
from ..models import Book, Chapter
from .verse_service import VerseService
from .navigation_service import NavigationService
from ..utils.text_utils import format_chapter_reference

class BibleService:
    def __init__(self):
        self.verse_service = VerseService()
        self.navigation_service = NavigationService()

    @staticmethod
    def get_books() -> QuerySet:
        """Retrieve all books ordered by their order field.
        Returns:
            QuerySet: Queryset of all books
        """
        return Book.objects.all().order_by('order')

    @staticmethod
    def get_chapters(book_id: int) -> QuerySet:
        """Retrieve chapters for a specific book.
        Args:
            book_id (int): ID of the book
        Returns:
            QuerySet: Queryset of chapters for the specified book
        """
        return Chapter.objects.filter(book_id=book_id).values('id', 'number')

    def get_verses(self, chapter_id: int) -> QuerySet:
        """Retrieve verses for a specific chapter with related data.
        Args:
            chapter_id (int): ID of the chapter
        Returns:
            QuerySet: Queryset of verses with related data
        """
        return self.verse_service.get_verses_by_chapter(chapter_id)

    def get_chapter_context(self, chapter_id: int) -> dict:
        """Get complete chapter context including verses and navigation.
        Args:
            chapter_id (int): ID of the chapter
        Returns:
            dict: Context containing verses and navigation data
        """
        chapter = Chapter.objects.select_related('book').get(id=chapter_id)
        verses = self.get_verses(chapter_id)
        navigation = self.navigation_service.get_adjacent_chapters(chapter_id)
        
        return {
            'chapter': chapter,
            'verses': verses,
            'previous_chapter': navigation['previous_chapter'],
            'next_chapter': navigation['next_chapter']
        }

    def get_verses_by_chapter(self, chapter_id: int) -> QuerySet:
        """Wrapper for retrieving verses by chapter ID.
        Args:
            chapter_id (int): ID of the chapter
        Returns:
            QuerySet: Queryset of verses for the specified chapter
        """
        return self.get_verses(chapter_id)

    def search_verses(self, search_text: str, page: int = 1) -> QuerySet:
        """Search verses across the Bible.
        Args:
            search_text (str): Text to search for
            page (int): Page number for pagination
        Returns:
            QuerySet: Filtered and paginated queryset of verses
        """
        return self.verse_service.search_verses(search_text, page)