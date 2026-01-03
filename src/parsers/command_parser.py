"""
Command Parser for the Todo application.

This module parses command-line input and routes to appropriate service methods.
"""
from typing import Dict, List, Optional, Tuple


class CommandParser:
    """
    Parser class for handling command-line input.
    """
    def __init__(self):
        """Initialize the command parser."""
        self.valid_commands = {
            'add', 'list', 'update', 'delete', 'complete', 'incomplete', 'help', 'version',
            'search', 'filter', 'sort', 'tag', 'priority', 'due', 'tagadd', 'tagremove'
        }

    def parse_command(self, user_input: str) -> Tuple[str, List[str]]:
        """
        Parse user input into command and arguments.

        Args:
            user_input: The raw user input

        Returns:
            A tuple containing the command and a list of arguments
        """
        if not user_input.strip():
            return 'help', []

        parts = user_input.strip().split()
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Validate command
        if command not in self.valid_commands:
            return 'invalid', [user_input]

        return command, args

    def validate_add_command(self, args: List[str]) -> bool:
        """
        Validate the 'add' command arguments.

        Args:
            args: List of arguments for the add command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 1  # At least a title is required

    def validate_update_command(self, args: List[str]) -> bool:
        """
        Validate the 'update' command arguments.

        Args:
            args: List of arguments for the update command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 2  # At least an ID and a title are required

    def validate_delete_command(self, args: List[str]) -> bool:
        """
        Validate the 'delete' command arguments.

        Args:
            args: List of arguments for the delete command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) == 1  # Exactly an ID is required

    def validate_complete_command(self, args: List[str]) -> bool:
        """
        Validate the 'complete' command arguments.

        Args:
            args: List of arguments for the complete command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) == 1  # Exactly an ID is required

    def validate_incomplete_command(self, args: List[str]) -> bool:
        """
        Validate the 'incomplete' command arguments.

        Args:
            args: List of arguments for the incomplete command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) == 1  # Exactly an ID is required

    def extract_task_details(self, args: List[str]) -> Tuple[str, Optional[str]]:
        """
        Extract title and description from command arguments.

        Args:
            args: List of arguments containing title and optional description

        Returns:
            A tuple containing the title and optional description
        """
        if len(args) == 0:
            return "", None

        # For update command, first argument is ID, so title is the second argument
        # For add command, first argument is title
        # We need to handle this more intelligently
        title = args[0]
        description = ' '.join(args[1:]) if len(args) > 1 else None
        return title, description

    def extract_task_details_for_add(self, args: List[str]) -> Tuple[str, Optional[str]]:
        """
        Extract title and description from command arguments for add command.
        For add command: add <title> [description]
        We'll use the first argument as title and the rest as description.

        Args:
            args: List of arguments containing title and optional description

        Returns:
            A tuple containing the title and optional description
        """
        if len(args) == 0:
            return "", None
        elif len(args) == 1:
            return args[0], None  # Just title
        else:
            # Use first argument as title, rest as description
            title = args[0]
            description = ' '.join(args[1:])
            return title, description

    def extract_task_details_for_update(self, args: List[str]) -> Tuple[str, Optional[str]]:
        """
        Extract title and description from command arguments for update command.
        Args should be [id, title, ...description_parts]

        Args:
            args: List of arguments containing id, title and optional description

        Returns:
            A tuple containing the title and optional description
        """
        if len(args) < 2:  # Need at least id and title
            return "", None
        elif len(args) == 2:
            return args[1], None  # [id, title]
        else:
            # [id, title, ...description_parts]
            title = args[1]
            description = ' '.join(args[2:])
            return title, description

    def extract_task_id(self, args: List[str]) -> Optional[int]:
        """
        Extract task ID from command arguments.

        Args:
            args: List of arguments containing the task ID

        Returns:
            The task ID as an integer, or None if invalid
        """
        try:
            return int(args[0])
        except (ValueError, IndexError):
            return None

    def validate_search_command(self, args: List[str]) -> bool:
        """
        Validate the 'search' command arguments.

        Args:
            args: List of arguments for the search command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 1  # At least a search query is required

    def validate_filter_command(self, args: List[str]) -> bool:
        """
        Validate the 'filter' command arguments.

        Args:
            args: List of arguments for the filter command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 1  # At least a filter criterion is required

    def validate_sort_command(self, args: List[str]) -> bool:
        """
        Validate the 'sort' command arguments.

        Args:
            args: List of arguments for the sort command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 1  # At least a sort field is required

    def validate_tag_command(self, args: List[str]) -> bool:
        """
        Validate the 'tag' command arguments (for adding tags).

        Args:
            args: List of arguments for the tag command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 2  # At least an ID and a tag are required

    def validate_priority_command(self, args: List[str]) -> bool:
        """
        Validate the 'priority' command arguments.

        Args:
            args: List of arguments for the priority command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 2  # At least an ID and a priority level are required

    def validate_due_command(self, args: List[str]) -> bool:
        """
        Validate the 'due' command arguments.

        Args:
            args: List of arguments for the due date command

        Returns:
            True if arguments are valid, False otherwise
        """
        return len(args) >= 2  # At least an ID and a date are required

    def extract_search_query(self, args: List[str]) -> str:
        """
        Extract search query from command arguments.

        Args:
            args: List of arguments containing the search query

        Returns:
            The search query string
        """
        return ' '.join(args)

    def extract_filter_criteria(self, args: List[str]) -> Dict[str, str]:
        """
        Extract filter criteria from command arguments.

        Args:
            args: List of arguments containing the filter criteria

        Returns:
            A dictionary of filter criteria
        """
        # For now, we'll just return the first argument as a simple filter
        # In a more complex implementation, this could parse more sophisticated filters
        if len(args) >= 1:
            return {'criterion': args[0]}
        return {}

    def extract_sort_criteria(self, args: List[str]) -> Dict[str, str]:
        """
        Extract sort criteria from command arguments.

        Args:
            args: List of arguments containing the sort criteria

        Returns:
            A dictionary of sort criteria
        """
        # Format: sort field [asc|desc]
        field = args[0] if len(args) > 0 else 'id'
        ascending = True
        if len(args) > 1:
            ascending = args[1].lower() in ['asc', 'ascending', 'a']
        return {'by': field, 'ascending': ascending}

    def extract_tag_info(self, args: List[str]) -> Tuple[Optional[int], str]:
        """
        Extract task ID and tag from command arguments.

        Args:
            args: List of arguments containing the task ID and tag

        Returns:
            A tuple containing the task ID and tag
        """
        if len(args) < 2:
            return None, ""
        try:
            task_id = int(args[0])
            tag = args[1]
            return task_id, tag
        except ValueError:
            return None, ""

    def extract_priority_info(self, args: List[str]) -> Tuple[Optional[int], str]:
        """
        Extract task ID and priority from command arguments.

        Args:
            args: List of arguments containing the task ID and priority

        Returns:
            A tuple containing the task ID and priority
        """
        if len(args) < 2:
            return None, ""
        try:
            task_id = int(args[0])
            priority = args[1]
            return task_id, priority
        except ValueError:
            return None, ""

    def extract_due_info(self, args: List[str]) -> Tuple[Optional[int], str]:
        """
        Extract task ID and due date from command arguments.

        Args:
            args: List of arguments containing the task ID and due date

        Returns:
            A tuple containing the task ID and due date string
        """
        if len(args) < 2:
            return None, ""
        try:
            task_id = int(args[0])
            due_date_str = ' '.join(args[1:])  # Join remaining arguments as date string
            return task_id, due_date_str
        except ValueError:
            return None, ""