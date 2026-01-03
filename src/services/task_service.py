"""
Task Service for the Todo application.

This module provides business logic for task operations.
"""
from typing import List, Optional
from models.task import Task
from repositories.task_repository import TaskRepository
from datetime import datetime


class TaskService:
    """
    Service class for managing task business logic.
    """
    def __init__(self, repository: TaskRepository):
        """
        Initialize the service with a repository.

        Args:
            repository: The task repository to use
        """
        self.repository = repository

    def create_task(self, title: str, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None) -> Optional[Task]:
        """
        Create a new task with validation.

        Args:
            title: The title of the task
            description: The description of the task (optional)
            priority: The priority level of the task (optional)
            tags: List of tags for the task (optional)

        Returns:
            The created task if successful, None otherwise
        """
        # Validate inputs
        if not title or not title.strip():
            return None

        # Create task object with new fields
        task = Task(
            id=0,
            title=title.strip(),
            description=description,
            priority=priority,
            tags=tags if tags is not None else []
        )

        # Validate the task
        if not task.validate():
            return None

        # Save to repository
        return self.repository.create_task(task)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List of all tasks
        """
        return self.repository.get_all_tasks()

    def update_task(self, task_id: int, title: str, description: Optional[str] = None, priority: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task with validation.

        Args:
            task_id: The ID of the task to update
            title: The new title of the task
            description: The new description of the task (optional)
            priority: The new priority of the task (optional)

        Returns:
            The updated task if successful, None otherwise
        """
        # Validate inputs
        if not title or not title.strip():
            return None

        # Check if task exists
        existing_task = self.repository.get_task_by_id(task_id)
        if not existing_task:
            return None

        # Create updated task object with new fields
        updated_task = Task(
            id=task_id,
            title=title.strip(),
            description=description,
            completed=existing_task.completed,
            created_at=existing_task.created_at,
            priority=priority if priority is not None else existing_task.priority,
            tags=existing_task.tags,  # Keep existing tags unless specifically updated
            due_date=existing_task.due_date,  # Keep existing due date
            recurring=existing_task.recurring  # Keep existing recurrence
        )

        # Validate the task
        if not updated_task.validate():
            return None

        # Update in repository
        return self.repository.update_task(task_id, updated_task)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False otherwise
        """
        return self.repository.delete_task(task_id)

    def toggle_task_completion(self, task_id: int, completed: bool) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to update
            completed: The new completion status

        Returns:
            The updated task if successful, None otherwise
        """
        return self.repository.toggle_task_completion(task_id, completed)

    def search_tasks(self, query: str) -> List[Task]:
        """
        Search tasks by title, description, or tags.

        Args:
            query: The search query string

        Returns:
            List of tasks matching the query
        """
        return self.repository.search_tasks(query)

    def filter_tasks(self, completed: Optional[bool] = None, priority: Optional[str] = None, tag: Optional[str] = None, due_before: Optional[datetime] = None, due_after: Optional[datetime] = None) -> List[Task]:
        """
        Filter tasks based on various criteria.

        Args:
            completed: Filter by completion status
            priority: Filter by priority level
            tag: Filter by tag
            due_before: Filter by due date (before this date)
            due_after: Filter by due date (after this date)

        Returns:
            List of tasks matching the criteria
        """
        return self.repository.filter_tasks(completed=completed, priority=priority, tag=tag, due_before=due_before, due_after=due_after)

    def sort_tasks(self, by: str = 'id', ascending: bool = True, completed_first: bool = False) -> List[Task]:
        """
        Sort tasks by various criteria.

        Args:
            by: Field to sort by ('id', 'title', 'priority', 'created_at', 'due_date')
            ascending: Sort order (True for ascending, False for descending)
            completed_first: Whether to put completed tasks first (regardless of other sorting)

        Returns:
            List of tasks sorted by the specified criteria
        """
        return self.repository.sort_tasks(by=by, ascending=ascending, completed_first=completed_first)

    def add_tag_to_task(self, task_id: int, tag: str) -> bool:
        """
        Add a tag to a task.

        Args:
            task_id: The ID of the task
            tag: The tag to add

        Returns:
            True if successful, False if task doesn't exist
        """
        return self.repository.add_tag_to_task(task_id, tag)

    def remove_tag_from_task(self, task_id: int, tag: str) -> bool:
        """
        Remove a tag from a task.

        Args:
            task_id: The ID of the task
            tag: The tag to remove

        Returns:
            True if successful, False if task doesn't exist or tag not found
        """
        return self.repository.remove_tag_from_task(task_id, tag)

    def set_task_priority(self, task_id: int, priority: str) -> bool:
        """
        Set the priority of a task.

        Args:
            task_id: The ID of the task
            priority: The priority level ('low', 'medium', 'high', 'urgent')

        Returns:
            True if successful, False if task doesn't exist
        """
        return self.repository.set_task_priority(task_id, priority)

    def set_task_due_date(self, task_id: int, due_date: datetime) -> bool:
        """
        Set the due date of a task.

        Args:
            task_id: The ID of the task
            due_date: The due date to set

        Returns:
            True if successful, False if task doesn't exist
        """
        return self.repository.set_task_due_date(task_id, due_date)