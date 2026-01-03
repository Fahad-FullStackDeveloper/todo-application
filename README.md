# Todo Application

A command-line todo application with in-memory storage built using Python 3.13+.

## Version
**Version 1.0.0** - Initial release with core functionality

## Features

- Add, list, update, delete, and mark tasks as complete/incomplete
- Interactive command-line interface
- In-memory storage for tasks
- Task completion tracking
- Comprehensive unit and integration tests

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

- `add <title> [description]` - Add a new task
- `list` - List all tasks
- `update <id> <title> [description]` - Update a task
- `delete <id>` - Delete a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `help` - Show help message
- `exit/quit/q` - Exit the application

### Examples

```bash
# Add a task
python src/main.py "add Complete project documentation"

# List all tasks
python src/main.py list

# Mark task with ID 1 as complete
python src/main.py "complete 1"

# Update task with ID 1
python src/main.py "update 1 Updated task title Updated description"

# Delete task with ID 1
python src/main.py "delete 1"
```

## Version Control System

This project follows semantic versioning (SemVer) with the following versioning scheme:

### Version Format
`MAJOR.MINOR.PATCH` where:
- `MAJOR` version: Incremented for incompatible API changes
- `MINOR` version: Incremented for new functionality in a backward-compatible manner
- `PATCH` version: Incremented for backward-compatible bug fixes

### Current Version: 1.0.0

#### Version History
- **1.0.0** - Initial release
  - Core functionality: add, list, update, delete, complete, incomplete tasks
  - In-memory storage implementation
  - Command-line interface
  - Unit and integration tests
  - MVC architecture implementation

### Git Workflow
This project uses the following Git workflow:
- `master` branch: Stable, production-ready code
- Feature branches: Development of new features (`feature/feature-name`)
- Hotfix branches: Urgent bug fixes (`hotfix/issue-description`)
- Release branches: Preparation for new releases (`release/vX.Y.Z`)

### Tagging Convention
Git tags follow the format `vX.Y.Z` (e.g., `v1.0.0`)

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
- Defines the Task data structure
- Includes validation for required fields
- Handles data representation

#### TaskRepository
- Manages in-memory storage of tasks
- Provides CRUD operations for tasks
- Handles data persistence (in-memory)

#### TaskService
- Implements business logic for task operations
- Validates inputs before data operations
- Coordinates between repository and interface

#### ConsoleInterface
- Handles user input and output
- Formats display of tasks
- Provides user feedback

#### CommandParser
- Parses command-line input
- Routes commands to appropriate service methods
- Handles command validation

## Development Workflow

1. Follow the tasks outlined in `specs/todo-app/tasks.md`
2. Implement components in the order specified
3. Write tests as you implement functionality
4. Validate functionality after each component
5. Follow the MVC architecture pattern