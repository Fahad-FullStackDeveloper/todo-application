# Todo Application

A command-line todo application with in-memory storage built using Python 3.13+.

## Version
**Version 2.0.0** - Enhanced version with advanced features

## Features

### Basic Level (Core Essentials)
- Add, list, update, delete, and mark tasks as complete/incomplete
- Interactive command-line interface
- In-memory storage for tasks
- Task completion tracking
- Comprehensive unit and integration tests

### Intermediate Level (Organization & Usability)
- **Priorities & Tags/Categories** – Assign levels (high/medium/low/urgent) or labels to tasks
- **Search & Filter** – Search by keyword; filter by status, priority, or tag
- **Sort Tasks** – Reorder by due date, priority, or alphabetically

### Advanced Level (Intelligent Features)
- **Due Dates & Time Management** – Set deadlines with date/time for tasks
- **Future Enhancements Ready** – Framework for recurring tasks and reminders

## Project Structure

- `/src/models` - Contains data models (Task entity)
- `/src/repositories` - Contains data access layer (TaskRepository)
- `/src/services` - Contains business logic (TaskService)
- `/src/interfaces` - Contains user interface components (ConsoleInterface)
- `/src/parsers` - Contains command parsing logic (CommandParser)
- `/tests/unit` - Contains unit tests
- `/tests/integration` - Contains integration tests

## Getting Started

### Prerequisites

- Python 3.13+

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

### Usage

The application supports the following commands:

#### Basic Commands
- `add <title> [description]` - Add a new task
- `list` - List all tasks
- `update <id> <title> [description]` - Update a task
- `delete <id>` - Delete a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete

#### Intermediate Commands
- `search <query>` - Search tasks by title, description, or tags
- `filter <criterion>` - Filter tasks (completed, pending, priority, tag)
- `sort <field> [asc|desc]` - Sort tasks by field (id, title, priority, created_at, due_date)
- `tag <id> <tag>` - Add a tag to a task
- `tagremove <id> <tag>` - Remove a tag from a task
- `priority <id> <level>` - Set task priority (low, medium, high, urgent)

#### Advanced Commands
- `due <id> <date>` - Set due date for a task

#### System Commands
- `version` - Show application version
- `help` - Show help message
- `exit/quit/q` - Exit the application

### Examples

```bash
# Basic operations
python src/main.py "add Complete project documentation"
python src/main.py list
python src/main.py "complete 1"
python src/main.py "update 1 Updated task title Updated description"
python src/main.py "delete 1"

# Intermediate features
python src/main.py "priority 1 high"          # Set task priority
python src/main.py "tag 1 work"              # Add tag to task
python src/main.py "search project"          # Search for tasks
python src/main.py "filter high"             # Filter by priority
python src/main.py "sort priority"           # Sort by priority

# Advanced features
python src/main.py "due 1 2026-12-31"       # Set due date
```

## Version Control System

This project follows semantic versioning (SemVer) with the following versioning scheme:

### Version Format
`MAJOR.MINOR.PATCH` where:
- `MAJOR` version: Incremented for incompatible API changes
- `MINOR` version: Incremented for new functionality in a backward-compatible manner
- `PATCH` version: Incremented for backward-compatible bug fixes

### Current Version: 2.0.0

#### Version History
- **2.0.0** - Enhanced release with intermediate and advanced features
  - Added priority management (low, medium, high, urgent)
  - Added tag management (add, remove, filter by tags)
  - Added search functionality (search by title, description, tags)
  - Added filter functionality (by status, priority, tags)
  - Added sort functionality (by id, title, priority, date)
  - Added due date management
  - Enhanced task display with all new fields
  - Updated user interface to show all task details
  - Comprehensive testing for all new features

- **1.0.0** - Initial release
  - Core functionality: add, list, update, delete, complete, incomplete tasks
  - In-memory storage implementation
  - Command-line interface
  - Unit and integration tests
  - MVC architecture implementation

### Git Workflow
This project uses the following Git workflow:
- `main` branch: Stable, production-ready code
- Feature branches: Development of new features (`feature/feature-name`)
- Hotfix branches: Urgent bug fixes (`hotfix/issue-description`)
- Release branches: Preparation for new releases (`release/vX.Y.Z`)

### Tagging Convention
Git tags follow the format `vX.Y.Z` (e.g., `v2.0.0`)

## Running Tests

```bash
# Run unit tests
PYTHONPATH=src python -m unittest discover tests/unit/ -v

# Run integration tests
PYTHONPATH=src python -m unittest discover tests/integration/ -v

# Run all tests
PYTHONPATH=src python -m unittest discover tests/ -v
```

## Running the Demo

```bash
python demo.py
```

## Architecture

### Component Responsibilities

#### Task Model
- Defines the Task data structure with id, title, description, completion status, priority, tags, due date
- Includes validation for required fields
- Handles data representation with all new fields

#### TaskRepository
- Manages in-memory storage of tasks
- Provides CRUD operations for tasks
- Handles data persistence (in-memory)
- Implements search, filter, and sort functionality
- Manages tag and priority operations

#### TaskService
- Implements business logic for task operations
- Validates inputs before data operations
- Coordinates between repository and interface
- Provides enhanced functionality for priorities, tags, search, filter, sort

#### ConsoleInterface
- Handles user input and output
- Formats display of tasks with all new fields (priority, tags, due dates)
- Provides user feedback

#### CommandParser
- Parses command-line input
- Routes commands to appropriate service methods
- Handles command validation for all new commands
- Manages argument extraction for complex operations

## Development Workflow

1. Follow the tasks outlined in `specs/todo-app/tasks.md`
2. Implement components in the order specified
3. Write tests as you implement functionality
4. Validate functionality after each component
5. Follow the MVC architecture pattern