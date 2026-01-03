"""
Main Application for the Todo application.

This module orchestrates the components of the application.
"""
import os
from typing import List, Optional
from services.task_service import TaskService
from interfaces.console_interface import ConsoleInterface
from parsers.command_parser import CommandParser


class TodoApp:
    """
    Main application class that orchestrates all components.
    """
    def __init__(self, task_service: TaskService, console_interface: ConsoleInterface, command_parser: CommandParser):
        """
        Initialize the application with required components.

        Args:
            task_service: The task service to use
            console_interface: The console interface to use
            command_parser: The command parser to use
        """
        self.task_service = task_service
        self.console_interface = console_interface
        self.command_parser = command_parser

    def run(self, initial_command: Optional[str] = None) -> None:
        """
        Run the main application loop.

        Args:
            initial_command: Optional initial command to execute
        """
        if initial_command:
            self.execute_command(initial_command)
        else:
            self.display_welcome_message()

        # Main application loop
        while True:
            try:
                user_input = self.console_interface.get_user_input("\nEnter command: ")
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("Goodbye!")
                    break

                self.execute_command(user_input)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                self.console_interface.display_error(f"An unexpected error occurred: {str(e)}")

    def execute_command(self, user_input: str) -> None:
        """
        Execute a command based on user input.

        Args:
            user_input: The raw user input to process
        """
        command, args = self.command_parser.parse_command(user_input)

        if command == 'add':
            self.handle_add_command(args)
        elif command == 'list':
            self.handle_list_command()
        elif command == 'update':
            self.handle_update_command(args)
        elif command == 'delete':
            self.handle_delete_command(args)
        elif command == 'complete':
            self.handle_complete_command(args)
        elif command == 'incomplete':
            self.handle_incomplete_command(args)
        elif command == 'search':
            self.handle_search_command(args)
        elif command == 'filter':
            self.handle_filter_command(args)
        elif command == 'sort':
            self.handle_sort_command(args)
        elif command in ['tag', 'tagadd']:
            self.handle_tag_add_command(args)
        elif command == 'tagremove':
            self.handle_tag_remove_command(args)
        elif command == 'priority':
            self.handle_priority_command(args)
        elif command == 'due':
            self.handle_due_command(args)
        elif command == 'help':
            self.handle_help_command()
        elif command == 'version':
            self.handle_version_command()
        elif command == 'invalid':
            self.console_interface.display_error(f"Invalid command: {user_input}")
            self.handle_help_command()
        else:
            self.console_interface.display_error(f"Unknown command: {command}")
            self.handle_help_command()

    def handle_add_command(self, args: List[str]) -> None:
        """Handle the 'add' command."""
        if not self.command_parser.validate_add_command(args):
            self.console_interface.display_error("Usage: add <title> [description]")
            return

        title, description = self.command_parser.extract_task_details_for_add(args)
        # For now, create task with default priority and no tags
        task = self.task_service.create_task(title, description)

        if task:
            self.console_interface.display_success(f"Task added with ID: {task.id}")
        else:
            self.console_interface.display_error("Failed to add task. Title cannot be empty.")

    def handle_list_command(self) -> None:
        """Handle the 'list' command."""
        tasks = self.task_service.get_all_tasks()
        self.console_interface.display_tasks(tasks)

    def handle_update_command(self, args: List[str]) -> None:
        """Handle the 'update' command."""
        if not self.command_parser.validate_update_command(args):
            self.console_interface.display_error("Usage: update <id> <title> [description]")
            return

        task_id = self.command_parser.extract_task_id(args[:1])
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        title, description = self.command_parser.extract_task_details_for_update(args)
        task = self.task_service.update_task(task_id, title, description)

        if task:
            self.console_interface.display_success(f"Task {task_id} updated successfully.")
        else:
            self.console_interface.display_error(f"Failed to update task {task_id}. Task may not exist.")

    def handle_delete_command(self, args: List[str]) -> None:
        """Handle the 'delete' command."""
        if not self.command_parser.validate_delete_command(args):
            self.console_interface.display_error("Usage: delete <id>")
            return

        task_id = self.command_parser.extract_task_id(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        success = self.task_service.delete_task(task_id)
        if success:
            self.console_interface.display_success(f"Task {task_id} deleted successfully.")
        else:
            self.console_interface.display_error(f"Failed to delete task {task_id}. Task may not exist.")

    def handle_complete_command(self, args: List[str]) -> None:
        """Handle the 'complete' command."""
        if not self.command_parser.validate_complete_command(args):
            self.console_interface.display_error("Usage: complete <id>")
            return

        task_id = self.command_parser.extract_task_id(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        task = self.task_service.toggle_task_completion(task_id, True)
        if task:
            self.console_interface.display_success(f"Task {task_id} marked as complete.")
        else:
            self.console_interface.display_error(f"Failed to mark task {task_id} as complete. Task may not exist.")

    def handle_incomplete_command(self, args: List[str]) -> None:
        """Handle the 'incomplete' command."""
        if not self.command_parser.validate_incomplete_command(args):
            self.console_interface.display_error("Usage: incomplete <id>")
            return

        task_id = self.command_parser.extract_task_id(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        task = self.task_service.toggle_task_completion(task_id, False)
        if task:
            self.console_interface.display_success(f"Task {task_id} marked as incomplete.")
        else:
            self.console_interface.display_error(f"Failed to mark task {task_id} as incomplete. Task may not exist.")

    def handle_search_command(self, args: List[str]) -> None:
        """Handle the 'search' command."""
        if not self.command_parser.validate_search_command(args):
            self.console_interface.display_error("Usage: search <query>")
            return

        query = self.command_parser.extract_search_query(args)
        tasks = self.task_service.search_tasks(query)
        self.console_interface.display_tasks(tasks)

    def handle_filter_command(self, args: List[str]) -> None:
        """Handle the 'filter' command."""
        if not self.command_parser.validate_filter_command(args):
            self.console_interface.display_error("Usage: filter <criterion>")
            return

        # For now, we'll implement a simple filter by status
        criterion = args[0].lower()

        # Parse filter criteria
        completed = None
        priority = None
        tag = None

        if criterion in ['completed', 'done', 'finished']:
            completed = True
        elif criterion in ['pending', 'incomplete', 'todo']:
            completed = False
        elif criterion in ['high', 'medium', 'low', 'urgent']:
            priority = criterion
        else:
            # Assume it's a tag filter
            tag = criterion

        tasks = self.task_service.filter_tasks(completed=completed, priority=priority, tag=tag)
        self.console_interface.display_tasks(tasks)

    def handle_sort_command(self, args: List[str]) -> None:
        """Handle the 'sort' command."""
        if not self.command_parser.validate_sort_command(args):
            self.console_interface.display_error("Usage: sort <field> [asc|desc]")
            return

        sort_criteria = self.command_parser.extract_sort_criteria(args)
        by = sort_criteria['by']
        ascending = sort_criteria['ascending']

        # Validate sort field
        valid_fields = ['id', 'title', 'priority', 'created_at', 'due_date']
        if by not in valid_fields:
            self.console_interface.display_error(f"Invalid sort field. Valid fields: {', '.join(valid_fields)}")
            return

        tasks = self.task_service.sort_tasks(by=by, ascending=ascending)
        self.console_interface.display_tasks(tasks)

    def handle_tag_add_command(self, args: List[str]) -> None:
        """Handle the 'tag' or 'tagadd' command."""
        if not self.command_parser.validate_tag_command(args):
            self.console_interface.display_error("Usage: tag <id> <tag>")
            return

        task_id, tag = self.command_parser.extract_tag_info(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        success = self.task_service.add_tag_to_task(task_id, tag)
        if success:
            self.console_interface.display_success(f"Tag '{tag}' added to task {task_id}.")
        else:
            self.console_interface.display_error(f"Failed to add tag to task {task_id}. Task may not exist.")

    def handle_tag_remove_command(self, args: List[str]) -> None:
        """Handle the 'tagremove' command."""
        if not self.command_parser.validate_tag_command(args):
            self.console_interface.display_error("Usage: tagremove <id> <tag>")
            return

        task_id, tag = self.command_parser.extract_tag_info(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        success = self.task_service.remove_tag_from_task(task_id, tag)
        if success:
            self.console_interface.display_success(f"Tag '{tag}' removed from task {task_id}.")
        else:
            self.console_interface.display_error(f"Failed to remove tag from task {task_id}. Task or tag may not exist.")

    def handle_priority_command(self, args: List[str]) -> None:
        """Handle the 'priority' command."""
        if not self.command_parser.validate_priority_command(args):
            self.console_interface.display_error("Usage: priority <id> <level>")
            return

        task_id, priority = self.command_parser.extract_priority_info(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        # Validate priority level
        valid_priorities = ['low', 'medium', 'high', 'urgent']
        if priority not in valid_priorities:
            self.console_interface.display_error(f"Invalid priority level. Valid levels: {', '.join(valid_priorities)}")
            return

        success = self.task_service.set_task_priority(task_id, priority)
        if success:
            self.console_interface.display_success(f"Priority set to '{priority}' for task {task_id}.")
        else:
            self.console_interface.display_error(f"Failed to set priority for task {task_id}. Task may not exist.")

    def handle_due_command(self, args: List[str]) -> None:
        """Handle the 'due' command."""
        if not self.command_parser.validate_due_command(args):
            self.console_interface.display_error("Usage: due <id> <date>")
            return

        task_id, due_date_str = self.command_parser.extract_due_info(args)
        if task_id is None:
            self.console_interface.display_error("Invalid task ID.")
            return

        # For simplicity, we'll just store the date string for now
        # In a real implementation, you would parse the date string properly
        from datetime import datetime
        try:
            # Try to parse the date - for now, just accept any string and create a datetime object
            # In a real implementation, you'd want to parse various date formats
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if len(due_date_str) == 10 else datetime.now()
        except ValueError:
            # If the date can't be parsed, just create a default datetime
            due_date = datetime.now()
            self.console_interface.display_error(f"Could not parse date '{due_date_str}', using current time instead.")

        success = self.task_service.set_task_due_date(task_id, due_date)
        if success:
            self.console_interface.display_success(f"Due date set to '{due_date_str}' for task {task_id}.")
        else:
            self.console_interface.display_error(f"Failed to set due date for task {task_id}. Task may not exist.")

    def handle_help_command(self) -> None:
        """Handle the 'help' command."""
        help_text = """
Available commands:
  add <title> [description]    - Add a new task
  list                        - List all tasks
  update <id> <title> [description] - Update a task
  delete <id>                 - Delete a task
  complete <id>               - Mark task as complete
  incomplete <id>             - Mark task as incomplete
  search <query>              - Search tasks by title, description, or tags
  filter <criterion>          - Filter tasks (completed, pending, priority, tag)
  sort <field> [asc|desc]     - Sort tasks by field (id, title, priority, created_at, due_date)
  tag <id> <tag>              - Add a tag to a task
  tagremove <id> <tag>        - Remove a tag from a task
  priority <id> <level>       - Set task priority (low, medium, high, urgent)
  due <id> <date>             - Set due date for a task
  version                     - Show application version
  help                        - Show this help message
  exit/quit/q                 - Exit the application
        """
        print(help_text)

    def handle_version_command(self) -> None:
        """Handle the 'version' command."""
        # Try to read version from VERSION file
        # __file__ is the path to this file (src/app.py)
        # We need to go up one level from src directory to project root
        version_file_path = os.path.join(os.path.dirname(__file__), '..', 'VERSION')
        try:
            with open(version_file_path, 'r') as f:
                version = f.read().strip()
        except FileNotFoundError:
            version = "1.0.0"  # Default version if file not found

        version_text = f"Todo Application Version {version}"
        print(version_text)

    def display_welcome_message(self) -> None:
        """Display the welcome message."""
        welcome_text = """
Welcome to the Todo Application!
This is a simple console-based todo app.
Type 'help' to see available commands.
        """
        print(welcome_text)