"""
Unit tests for the TaskService.
"""
import unittest
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    """
    Test cases for the TaskService.
    """
    def setUp(self):
        """Set up a service with a fresh repository for each test."""
        self.repository = TaskRepository()
        self.service = TaskService(self.repository)

    def test_create_task_success(self):
        """Test creating a task successfully."""
        result = self.service.create_task("Test Title", "Test Description")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Test Title")
        self.assertEqual(result.description, "Test Description")
        self.assertFalse(result.completed)
        self.assertEqual(result.id, 1)

    def test_create_task_empty_title(self):
        """Test creating a task with an empty title (should fail)."""
        result = self.service.create_task("", "Test Description")
        self.assertIsNone(result)

        result = self.service.create_task("   ", "Test Description")
        self.assertIsNone(result)

    def test_create_task_no_description(self):
        """Test creating a task without a description."""
        result = self.service.create_task("Test Title")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Test Title")
        self.assertIsNone(result.description)

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when there are none."""
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        # Create some tasks
        self.service.create_task("Task 1", "Description 1")
        self.service.create_task("Task 2", "Description 2")

        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        titles = [task.title for task in tasks]
        self.assertIn("Task 1", titles)
        self.assertIn("Task 2", titles)

    def test_update_task_success(self):
        """Test updating a task successfully."""
        # Create a task first
        original_task = self.service.create_task("Original Title", "Original Description")
        self.assertIsNotNone(original_task)

        # Update the task
        result = self.service.update_task(original_task.id, "Updated Title", "Updated Description")
        self.assertIsNotNone(result)
        self.assertEqual(result.id, original_task.id)
        self.assertEqual(result.title, "Updated Title")
        self.assertEqual(result.description, "Updated Description")
        # Completion status should be preserved
        self.assertFalse(result.completed)

    def test_update_task_not_exists(self):
        """Test updating a task that doesn't exist."""
        result = self.service.update_task(999, "Updated Title", "Updated Description")
        self.assertIsNone(result)

    def test_update_task_empty_title(self):
        """Test updating a task with an empty title (should fail)."""
        # Create a task first
        original_task = self.service.create_task("Original Title", "Original Description")
        self.assertIsNotNone(original_task)

        # Try to update with empty title
        result = self.service.update_task(original_task.id, "", "Updated Description")
        self.assertIsNone(result)

        # Verify original task is unchanged
        retrieved_task = self.repository.get_task_by_id(original_task.id)
        self.assertEqual(retrieved_task.title, "Original Title")

    def test_delete_task_exists(self):
        """Test deleting a task that exists."""
        # Create a task first
        task = self.service.create_task("Test Title", "Test Description")
        self.assertIsNotNone(task)

        # Delete the task
        result = self.service.delete_task(task.id)
        self.assertTrue(result)

        # Verify task is gone
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_task_not_exists(self):
        """Test deleting a task that doesn't exist."""
        result = self.service.delete_task(999)
        self.assertFalse(result)

    def test_toggle_task_completion_success(self):
        """Test toggling task completion successfully."""
        # Create a task first
        task = self.service.create_task("Test Title", "Test Description")
        self.assertIsNotNone(task)
        self.assertFalse(task.completed)  # Initially not completed

        # Mark as complete
        result = self.service.toggle_task_completion(task.id, True)
        self.assertIsNotNone(result)
        self.assertTrue(result.completed)

        # Mark as incomplete
        result = self.service.toggle_task_completion(task.id, False)
        self.assertIsNotNone(result)
        self.assertFalse(result.completed)

    def test_toggle_task_completion_not_exists(self):
        """Test toggling completion for a task that doesn't exist."""
        result = self.service.toggle_task_completion(999, True)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()