"""
Unit tests for the ConsoleInterface.
"""
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from src.models.task import Task
from src.interfaces.console_interface import ConsoleInterface


class TestConsoleInterface(unittest.TestCase):
    """
    Test cases for the ConsoleInterface.
    """
    def setUp(self):
        """Set up a console interface for testing."""
        self.interface = ConsoleInterface()

    def test_format_task(self):
        """Test formatting a single task."""
        task = Task(id=1, title="Test Task", description="Test Description")

        # Test incomplete task with priority
        formatted = self.interface.format_task(task)
        expected = "[O] [medium] 1: Test Task - Test Description"
        self.assertEqual(formatted, expected)

        # Test completed task with priority
        task.completed = True
        formatted = self.interface.format_task(task)
        expected = "[X] [medium] 1: Test Task - Test Description"
        self.assertEqual(formatted, expected)

        # Test task with no description
        task = Task(id=2, title="No Description Task")
        formatted = self.interface.format_task(task)
        expected = "[O] [medium] 2: No Description Task - No description"
        self.assertEqual(formatted, expected)

    def test_display_task(self):
        """Test displaying a single task."""
        task = Task(id=1, title="Test Task", description="Test Description")

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.interface.display_task(task)

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected = "[O] [medium] 1: Test Task - Test Description"
        self.assertEqual(output, expected)

    def test_display_tasks_empty(self):
        """Test displaying an empty task list."""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.interface.display_tasks([])

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, "No tasks found.")

    def test_display_tasks_multiple(self):
        """Test displaying multiple tasks."""
        task1 = Task(id=1, title="Task 1", description="Description 1")
        task2 = Task(id=2, title="Task 2", description="Description 2")
        task2.completed = True

        captured_output = StringIO()
        sys.stdout = captured_output

        self.interface.display_tasks([task1, task2])

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        # Check that the output contains the expected elements
        self.assertIn("Your Tasks:", output)
        self.assertIn("[O] [medium] 1: Task 1 - Description 1", output)
        self.assertIn("[X] [medium] 2: Task 2 - Description 2", output)
        self.assertIn("-" * 50, output)

    def test_display_error(self):
        """Test displaying an error message."""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.interface.display_error("Something went wrong")

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected = "Error: Something went wrong"
        self.assertEqual(output, expected)

    def test_display_success(self):
        """Test displaying a success message."""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.interface.display_success("Operation completed")

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected = "Success: Operation completed"
        self.assertEqual(output, expected)

    @patch('builtins.input', return_value='test input')
    def test_get_user_input(self, mock_input):
        """Test getting user input."""
        result = self.interface.get_user_input("Enter something: ")
        self.assertEqual(result, 'test input')
        mock_input.assert_called_once_with("Enter something: ")


if __name__ == '__main__':
    unittest.main()