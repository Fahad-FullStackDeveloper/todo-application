"""
Console Interface for the Todo application.

This module handles user input and output in the console.
"""
from typing import List
from models.task import Task


class ConsoleInterface:
    """
    Interface class for handling console input and output.
    """
    def display_tasks(self, tasks: List[Task]) -> None:
        """
        Display all tasks in a formatted way.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            print(self.format_task(task))
        print("-" * 50)

    def display_task(self, task: Task) -> None:
        """
        Display a single task.

        Args:
            task: The task to display
        """
        print(self.format_task(task))

    def format_task(self, task: Task) -> str:
        """
        Format a task for display.

        Args:
            task: The task to format

        Returns:
            Formatted string representation of the task
        """
        # Use the Task's __str__ method which includes all new fields
        return str(task)

    def display_error(self, message: str) -> None:
        """
        Display an error message.

        Args:
            message: The error message to display
        """
        print(f"Error: {message}")

    def display_success(self, message: str) -> None:
        """
        Display a success message.

        Args:
            message: The success message to display
        """
        print(f"Success: {message}")

    def get_user_input(self, prompt: str = "") -> str:
        """
        Get input from the user.

        Args:
            prompt: The prompt to display to the user

        Returns:
            The user's input
        """
        return input(prompt)