"""
Task Repository for the Todo application.

This module provides in-memory storage and retrieval of Task objects.
"""
from typing import Dict, List, Optional
from models.task import Task


class TaskRepository:
    """
    Repository class for managing Task objects in memory.
    """
    def __init__(self):
        """Initialize the repository with an empty storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def create_task(self, task: Task) -> Task:
        """
        Create a new task in the repository.

        Args:
            task: The task to create

        Returns:
            The created task with assigned ID
        """
        if task.id is None or task.id == 0:
            task.id = self._next_id
            self._next_id += 1
        self._tasks[task.id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks from the repository.

        Returns:
            List of all tasks
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, updated_task: Task) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            updated_task: The updated task object

        Returns:
            The updated task if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        # Preserve the original ID
        updated_task.id = task_id
        self._tasks[task_id] = updated_task
        return updated_task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if it didn't exist
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_task_completion(self, task_id: int, completed: bool) -> Optional[Task]:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to update
            completed: The new completion status

        Returns:
            The updated task if successful, None if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = completed
            return task
        return None