"""
Task model for the Todo application.

This module defines the Task data class with validation and string representation.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum


class Priority(Enum):
    """Priority levels for tasks."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


@dataclass
class Task:
    """
    Represents a todo task with id, title, description, completion status, and additional features.
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None
    priority: Optional[str] = None  # Can be 'low', 'medium', 'high', 'urgent'
    tags: Optional[List[str]] = None  # List of tags for the task
    due_date: Optional[datetime] = None  # Due date for the task
    recurring: Optional[Dict[str, Any]] = None  # Recurrence pattern for recurring tasks

    def __post_init__(self):
        """Initialize default values if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.tags is None:
            self.tags = []
        if self.priority is None:
            self.priority = Priority.MEDIUM.value

    def __str__(self) -> str:
        """String representation of the task."""
        status = "X" if self.completed else "O"
        priority_str = f" [{self.priority}]" if self.priority else ""
        tags_str = f" Tags: {', '.join(self.tags)}" if self.tags else ""
        due_str = f" Due: {self.due_date.strftime('%Y-%m-%d %H:%M') if self.due_date else ''}" if self.due_date else ""
        recurring_str = f" Recurring: {self.recurring}" if self.recurring else ""

        result = f"[{status}]{priority_str} {self.id}: {self.title} - {self.description or 'No description'}"
        if tags_str:
            result += f"\n    {tags_str}"
        if due_str:
            result += f"\n    {due_str}"
        if recurring_str:
            result += f"\n    {recurring_str}"
        return result

    def validate(self) -> bool:
        """
        Validate the task data.

        Returns:
            bool: True if the task is valid, False otherwise
        """
        if not self.title or not self.title.strip():
            return False
        if self.priority and self.priority not in [p.value for p in Priority]:
            return False
        return True

    def add_tag(self, tag: str) -> None:
        """Add a tag to the task if it doesn't already exist."""
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> bool:
        """Remove a tag from the task if it exists."""
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False