"""
Integration tests for the Todo application components.
"""
import unittest
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.interfaces.console_interface import ConsoleInterface
from src.parsers.command_parser import CommandParser
from src.app import TodoApp


class TestTodoAppIntegration(unittest.TestCase):
    """
    Integration tests for the Todo application components.
    """
    def setUp(self):
        """Set up components for integration testing."""
        self.repository = TaskRepository()
        self.service = TaskService(self.repository)
        self.interface = ConsoleInterface()
        self.parser = CommandParser()
        self.app = TodoApp(self.service, self.interface, self.parser)

    def test_full_task_lifecycle(self):
        """Test the complete lifecycle of a task: create, read, update, complete, delete."""
        # 1. Create a task
        task = self.service.create_task("Integration Test Task", "Test description for integration")
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Integration Test Task")
        self.assertEqual(task.description, "Test description for integration")
        self.assertFalse(task.completed)

        # 2. Read all tasks (should have 1)
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Integration Test Task")

        # 3. Update the task
        updated_task = self.service.update_task(task.id, "Updated Integration Test Task", "Updated description")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Updated Integration Test Task")
        self.assertEqual(updated_task.description, "Updated description")

        # 4. Mark as complete
        completed_task = self.service.toggle_task_completion(task.id, True)
        self.assertIsNotNone(completed_task)
        self.assertTrue(completed_task.completed)

        # 5. Mark as incomplete again
        incomplete_task = self.service.toggle_task_completion(task.id, False)
        self.assertIsNotNone(incomplete_task)
        self.assertFalse(incomplete_task.completed)

        # 6. Delete the task
        delete_result = self.service.delete_task(task.id)
        self.assertTrue(delete_result)

        # 7. Verify task is gone
        final_tasks = self.service.get_all_tasks()
        self.assertEqual(len(final_tasks), 0)

    def test_multiple_tasks_operations(self):
        """Test operations with multiple tasks."""
        # Create multiple tasks
        task1 = self.service.create_task("Task 1", "Description 1")
        task2 = self.service.create_task("Task 2", "Description 2")
        task3 = self.service.create_task("Task 3", "Description 3")

        self.assertIsNotNone(task1)
        self.assertIsNotNone(task2)
        self.assertIsNotNone(task3)

        # Check all tasks exist
        all_tasks = self.service.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)

        # Update one task
        updated_task = self.service.update_task(task2.id, "Updated Task 2", "Updated Description 2")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Updated Task 2")

        # Mark one as complete
        completed_task = self.service.toggle_task_completion(task1.id, True)
        self.assertIsNotNone(completed_task)
        self.assertTrue(completed_task.completed)

        # Delete one task
        delete_result = self.service.delete_task(task3.id)
        self.assertTrue(delete_result)

        # Verify we have 2 tasks left
        remaining_tasks = self.service.get_all_tasks()
        self.assertEqual(len(remaining_tasks), 2)

        # Verify the correct tasks remain
        titles = [task.title for task in remaining_tasks]
        self.assertIn("Task 1", titles)  # Updated Task 1
        self.assertIn("Updated Task 2", titles)  # Updated Task 2 (was Task 2)

    def test_command_parsing_integration(self):
        """Test command parsing with service operations."""
        # Test add command parsing
        command, args = self.parser.parse_command("add Test Title Test Description")
        self.assertEqual(command, "add")
        self.assertEqual(len(args), 4)  # ["Test", "Title", "Test", "Description"] split by spaces

        # Test list command parsing
        command, args = self.parser.parse_command("list")
        self.assertEqual(command, "list")
        self.assertEqual(len(args), 0)

        # Test update command parsing
        command, args = self.parser.parse_command("update 1 New Title New Description")
        self.assertEqual(command, "update")
        self.assertEqual(len(args), 5)  # ["1", "New", "Title", "New", "Description"] split by spaces

        # Test delete command parsing
        command, args = self.parser.parse_command("delete 1")
        self.assertEqual(command, "delete")
        self.assertEqual(len(args), 1)

        # Test complete command parsing
        command, args = self.parser.parse_command("complete 1")
        self.assertEqual(command, "complete")
        self.assertEqual(len(args), 1)

        # Test help command parsing
        command, args = self.parser.parse_command("help")
        self.assertEqual(command, "help")
        self.assertEqual(len(args), 0)

    def test_command_validation(self):
        """Test command validation."""
        # Valid add command
        self.assertTrue(self.parser.validate_add_command(["title"]))
        self.assertTrue(self.parser.validate_add_command(["title", "description"]))

        # Invalid add command
        self.assertFalse(self.parser.validate_add_command([]))

        # Valid update command
        self.assertTrue(self.parser.validate_update_command(["1", "title"]))
        self.assertTrue(self.parser.validate_update_command(["1", "title", "description"]))

        # Invalid update command
        self.assertFalse(self.parser.validate_update_command([]))
        self.assertFalse(self.parser.validate_update_command(["1"]))

        # Valid delete command
        self.assertTrue(self.parser.validate_delete_command(["1"]))

        # Invalid delete command
        self.assertFalse(self.parser.validate_delete_command([]))
        self.assertFalse(self.parser.validate_delete_command(["1", "2"]))

        # Valid complete/incomplete commands
        self.assertTrue(self.parser.validate_complete_command(["1"]))
        self.assertTrue(self.parser.validate_incomplete_command(["1"]))

        # Invalid complete/incomplete commands
        self.assertFalse(self.parser.validate_complete_command([]))
        self.assertFalse(self.parser.validate_incomplete_command([]))


if __name__ == '__main__':
    unittest.main()