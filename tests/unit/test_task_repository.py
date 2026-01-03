"""
Unit tests for the TaskRepository.
"""
import unittest
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class TestTaskRepository(unittest.TestCase):
    """
    Test cases for the TaskRepository.
    """
    def setUp(self):
        """Set up a fresh repository for each test."""
        self.repository = TaskRepository()

    def test_create_task(self):
        """Test creating a new task."""
        task = Task(id=0, title="Test Task", description="Test Description")
        created_task = self.repository.create_task(task)

        self.assertEqual(created_task.id, 1)  # First task should get ID 1
        self.assertEqual(created_task.title, "Test Task")
        self.assertEqual(created_task.description, "Test Description")
        self.assertIn(1, self.repository._tasks)

    def test_create_task_with_provided_id(self):
        """Test creating a task with a provided ID."""
        task = Task(id=5, title="Test Task", description="Test Description")
        created_task = self.repository.create_task(task)

        self.assertEqual(created_task.id, 5)
        self.assertEqual(created_task.title, "Test Task")
        self.assertIn(5, self.repository._tasks)

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when repository is empty."""
        tasks = self.repository.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        # Add some tasks
        task1 = Task(id=0, title="Task 1")
        task2 = Task(id=0, title="Task 2")
        self.repository.create_task(task1)
        self.repository.create_task(task2)

        tasks = self.repository.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        titles = [task.title for task in tasks]
        self.assertIn("Task 1", titles)
        self.assertIn("Task 2", titles)

    def test_get_task_by_id_exists(self):
        """Test getting a task that exists."""
        task = Task(id=0, title="Test Task")
        created_task = self.repository.create_task(task)

        retrieved_task = self.repository.get_task_by_id(created_task.id)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, created_task.id)
        self.assertEqual(retrieved_task.title, "Test Task")

    def test_get_task_by_id_not_exists(self):
        """Test getting a task that doesn't exist."""
        task = self.repository.get_task_by_id(999)
        self.assertIsNone(task)

    def test_update_task_exists(self):
        """Test updating a task that exists."""
        # Create and add a task
        original_task = Task(id=0, title="Original Task", description="Original Description")
        created_task = self.repository.create_task(original_task)

        # Update the task
        updated_task = Task(
            id=created_task.id,
            title="Updated Task",
            description="Updated Description",
            completed=True
        )
        result = self.repository.update_task(created_task.id, updated_task)

        self.assertIsNotNone(result)
        self.assertEqual(result.id, created_task.id)
        self.assertEqual(result.title, "Updated Task")
        self.assertEqual(result.description, "Updated Description")
        self.assertTrue(result.completed)

    def test_update_task_not_exists(self):
        """Test updating a task that doesn't exist."""
        task = Task(id=999, title="Non-existent Task")
        result = self.repository.update_task(999, task)
        self.assertIsNone(result)

    def test_delete_task_exists(self):
        """Test deleting a task that exists."""
        task = Task(id=0, title="Test Task")
        created_task = self.repository.create_task(task)

        result = self.repository.delete_task(created_task.id)
        self.assertTrue(result)
        self.assertNotIn(created_task.id, self.repository._tasks)

        # Verify task is gone
        retrieved_task = self.repository.get_task_by_id(created_task.id)
        self.assertIsNone(retrieved_task)

    def test_delete_task_not_exists(self):
        """Test deleting a task that doesn't exist."""
        result = self.repository.delete_task(999)
        self.assertFalse(result)

    def test_toggle_task_completion_exists(self):
        """Test toggling completion status of a task that exists."""
        task = Task(id=0, title="Test Task")
        created_task = self.repository.create_task(task)

        # Initially not completed
        self.assertFalse(created_task.completed)

        # Toggle to completed
        updated_task = self.repository.toggle_task_completion(created_task.id, True)
        self.assertIsNotNone(updated_task)
        self.assertTrue(updated_task.completed)

        # Toggle back to incomplete
        updated_task = self.repository.toggle_task_completion(created_task.id, False)
        self.assertIsNotNone(updated_task)
        self.assertFalse(updated_task.completed)

    def test_toggle_task_completion_not_exists(self):
        """Test toggling completion status of a task that doesn't exist."""
        result = self.repository.toggle_task_completion(999, True)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()