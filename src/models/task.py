"""
Task model for the Todo application.

This module defines the Task data class with validation and string representation.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo task with id, title, description, completion status, and creation timestamp.
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """String representation of the task."""
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.title} - {self.description or 'No description'}"

    def validate(self) -> bool:
        """
        Validate the task data.

        Returns:
            bool: True if the task is valid, False otherwise
        """
        if not self.title or not self.title.strip():
            return False
        return True