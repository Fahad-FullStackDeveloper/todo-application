"""
Task Service for the Todo application.

This module provides business logic for task operations.
"""
from typing import List, Optional
from models.task import Task
from repositories.task_repository import TaskRepository


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

    def create_task(self, title: str, description: Optional[str] = None) -> Optional[Task]:
        """
        Create a new task with validation.

        Args:
            title: The title of the task
            description: The description of the task (optional)

        Returns:
            The created task if successful, None otherwise
        """
        # Validate inputs
        if not title or not title.strip():
            return None

        # Create task object
        task = Task(id=0, title=title.strip(), description=description)

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

    def update_task(self, task_id: int, title: str, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task with validation.

        Args:
            task_id: The ID of the task to update
            title: The new title of the task
            description: The new description of the task (optional)

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

        # Create updated task object
        updated_task = Task(
            id=task_id,
            title=title.strip(),
            description=description,
            completed=existing_task.completed,
            created_at=existing_task.created_at
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