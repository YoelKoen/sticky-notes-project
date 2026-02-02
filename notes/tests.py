from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteProjectTests(TestCase):

    def setUp(self):
        # Create a sample note for testing
        self.note = Note.objects.create(
            title="Test Note", content="This is a test content"
        )

    def test_note_content(self):
        # Check if the note was created with the correct data
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test content")

    def test_note_list_view(self):
        # Check if the homepage (note list) loads correctly
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        # Check if the update page loads correctly
        response = self.client.get(reverse("note_update", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
