"""
Task Repository for the Todo application.

This module provides in-memory storage and retrieval of Task objects.
"""
from typing import Dict, List, Optional
from models.task import Task, Priority
from datetime import datetime


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

    def search_tasks(self, query: str) -> List[Task]:
        """
        Search tasks by title, description, or tags.

        Args:
            query: The search query string

        Returns:
            List of tasks matching the query
        """
        query_lower = query.lower()
        matching_tasks = []

        for task in self._tasks.values():
            # Search in title
            if query_lower in task.title.lower():
                matching_tasks.append(task)
            # Search in description
            elif task.description and query_lower in task.description.lower():
                matching_tasks.append(task)
            # Search in tags
            elif task.tags:
                for tag in task.tags:
                    if query_lower in tag.lower():
                        matching_tasks.append(task)
                        break  # Avoid adding the same task multiple times

        return matching_tasks

    def filter_tasks(self,
                    completed: Optional[bool] = None,
                    priority: Optional[str] = None,
                    tag: Optional[str] = None,
                    due_before: Optional[datetime] = None,
                    due_after: Optional[datetime] = None) -> List[Task]:
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
        filtered_tasks = []

        for task in self._tasks.values():
            # Check completion status
            if completed is not None and task.completed != completed:
                continue

            # Check priority
            if priority is not None and task.priority != priority:
                continue

            # Check tag
            if tag is not None and tag not in task.tags:
                continue

            # Check due date before
            if due_before is not None and task.due_date and task.due_date > due_before:
                continue

            # Check due date after
            if due_after is not None and task.due_date and task.due_date < due_after:
                continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self,
                  by: str = 'id',
                  ascending: bool = True,
                  completed_first: bool = False) -> List[Task]:
        """
        Sort tasks by various criteria.

        Args:
            by: Field to sort by ('id', 'title', 'priority', 'created_at', 'due_date')
            ascending: Sort order (True for ascending, False for descending)
            completed_first: Whether to put completed tasks first (regardless of other sorting)

        Returns:
            List of tasks sorted by the specified criteria
        """
        def sort_key(task):
            # Primary sort: completed status if requested
            if completed_first:
                completed_val = 0 if task.completed else 1
            else:
                completed_val = 0  # Don't affect sorting if not requested

            # Secondary sort: based on the 'by' field
            if by == 'title':
                sort_val = task.title.lower()
            elif by == 'priority':
                # Map priority to numeric value for sorting (urgent > high > medium > low)
                priority_order = {
                    'urgent': 0,
                    'high': 1,
                    'medium': 2,
                    'low': 3
                }
                sort_val = priority_order.get(task.priority, 4)  # Default to lowest priority
            elif by == 'created_at':
                sort_val = task.created_at
            elif by == 'due_date':
                # Use due date, with None values treated as far in the future
                sort_val = task.due_date if task.due_date is not None else datetime.max
            else:  # Default to id
                sort_val = task.id

            return (completed_val, sort_val)

        sorted_tasks = sorted(self._tasks.values(), key=sort_key, reverse=not ascending)
        return sorted_tasks

    def add_tag_to_task(self, task_id: int, tag: str) -> bool:
        """
        Add a tag to a task.

        Args:
            task_id: The ID of the task
            tag: The tag to add

        Returns:
            True if successful, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.add_tag(tag)
            return True
        return False

    def remove_tag_from_task(self, task_id: int, tag: str) -> bool:
        """
        Remove a tag from a task.

        Args:
            task_id: The ID of the task
            tag: The tag to remove

        Returns:
            True if successful, False if task doesn't exist or tag not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            return task.remove_tag(tag)
        return False

    def set_task_priority(self, task_id: int, priority: str) -> bool:
        """
        Set the priority of a task.

        Args:
            task_id: The ID of the task
            priority: The priority level ('low', 'medium', 'high', 'urgent')

        Returns:
            True if successful, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
            return True
        return False

    def set_task_due_date(self, task_id: int, due_date: datetime) -> bool:
        """
        Set the due date of a task.

        Args:
            task_id: The ID of the task
            due_date: The due date to set

        Returns:
            True if successful, False if task doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.due_date = due_date
            return True
        return False