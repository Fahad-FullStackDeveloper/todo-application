"""
Entry point for the Todo application.

This module initializes and runs the main application.
"""
import sys
from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from interfaces.console_interface import ConsoleInterface
from parsers.command_parser import CommandParser
from app import TodoApp


def main():
    """
    Main entry point for the application.
    """
    # Initialize components
    repository = TaskRepository()
    service = TaskService(repository)
    interface = ConsoleInterface()
    parser = CommandParser()

    # Create and run the application
    app = TodoApp(service, interface, parser)

    # Process command-line arguments if provided
    if len(sys.argv) > 1:
        initial_command = ' '.join(sys.argv[1:])
        # Run with initial command but don't enter interactive mode
        app.execute_command(initial_command)
    else:
        app.run()


if __name__ == "__main__":
    main()