"""
Simple test script to demonstrate the Todo application functionality.
"""
import sys
import os

# Add src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from interfaces.console_interface import ConsoleInterface
from parsers.command_parser import CommandParser
from app import TodoApp


def demo():
    """Demonstrate the Todo application functionality."""
    # Initialize components
    repository = TaskRepository()
    service = TaskService(repository)
    interface = ConsoleInterface()
    parser = CommandParser()

    # Create and run the application
    app = TodoApp(service, interface, parser)

    print("=== Todo Application Demo ===\n")

    # Add a task - in this format: add title description
    # So "add Sample Task This is a sample task" means:
    # - Command: add
    # - Args: ["Sample", "Task", "This", "is", "a", "sample", "task"]
    # - Title: "Sample" (first arg)
    # - Description: "Task This is a sample task" (remaining args)
    print("1. Adding a task:")
    app.execute_command("add Sample 'Task This is a sample task'")

    # Add another task
    print("\n2. Adding another task:")
    app.execute_command("add Another 'Task Another task for testing'")

    # List tasks
    print("\n3. Listing all tasks:")
    app.execute_command("list")

    # Update a task - format: update id title description
    # So "update 1 Updated Sample Task This is updated" means:
    # - Command: update
    # - Args: ["1", "Updated", "Sample", "Task", "This", "is", "updated"]
    # - ID: "1"
    # - Title: "Sample" (second arg after ID)
    # - Description: "Task This is updated" (remaining args after ID and title)
    print("\n4. Updating the first task:")
    app.execute_command("update 1 Updated 'Sample Task This is updated'")

    # List tasks again
    print("\n5. Listing all tasks after update:")
    app.execute_command("list")

    # Mark a task as complete
    print("\n6. Marking the first task as complete:")
    app.execute_command("complete 1")

    # List tasks to show completion
    print("\n7. Listing all tasks after marking one as complete:")
    app.execute_command("list")

    # Delete a task
    print("\n8. Deleting the second task:")
    app.execute_command("delete 2")

    # Final list
    print("\n9. Final list of tasks:")
    app.execute_command("list")


if __name__ == "__main__":
    demo()