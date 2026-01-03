"""
Unit tests for the Task model.
"""
import unittest
from datetime import datetime
from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Test cases for the Task model.
    """
    def test_task_creation(self):
        """Test creating a task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertIsInstance(task.created_at, datetime)

    def test_task_creation_defaults(self):
        """Test creating a task with minimal data."""
        task = Task(id=1, title="Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)
        self.assertIsInstance(task.created_at, datetime)

    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task(id=1, title="Test Task", description="Test Description")
        expected = "[O] 1: Test Task - Test Description"
        self.assertEqual(str(task), expected)

        # Test with completed task
        task.completed = True
        expected = "[X] 1: Test Task - Test Description"
        self.assertEqual(str(task), expected)

        # Test with no description
        task = Task(id=1, title="Test Task")
        expected = "[O] 1: Test Task - No description"
        self.assertEqual(str(task), expected)

    def test_task_validation(self):
        """Test task validation."""
        # Valid task
        task = Task(id=1, title="Test Task")
        self.assertTrue(task.validate())

        # Invalid task with empty title
        task = Task(id=1, title="")
        self.assertFalse(task.validate())

        # Invalid task with whitespace-only title
        task = Task(id=1, title="   ")
        self.assertFalse(task.validate())

        # Valid task with description
        task = Task(id=1, title="Test Task", description="Test Description")
        self.assertTrue(task.validate())


if __name__ == '__main__':
    unittest.main()