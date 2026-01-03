# Claude Code Instructions for Todo Application

This file contains specific instructions for using Claude Code with the Todo Application project.

## Project Overview

The Todo Application Phase I is a command-line todo application with in-memory storage built using Python 3.13+, UV package manager, Claude Code, and Spec-Kit Plus.

## Code Standards

- Follow PEP 8 Python style guide
- Use type hints for all function parameters and return values
- Include docstrings for all classes and functions
- Use meaningful variable and function names
- Follow clean code principles
- Separate concerns with clear component boundaries

## Project Structure

- `/src/models` - Contains data models (Task entity)
- `/src/repositories` - Contains data access layer (TaskRepository)
- `/src/services` - Contains business logic (TaskService)
- `/src/interfaces` - Contains user interface components (ConsoleInterface)
- `/src/parsers` - Contains command parsing logic (CommandParser)
- `/tests/unit` - Contains unit tests
- `/tests/integration` - Contains integration tests

## Component Responsibilities

### Task Model
- Defines the Task data structure
- Includes validation for required fields
- Handles data representation

### TaskRepository
- Manages in-memory storage of tasks
- Provides CRUD operations for tasks
- Handles data persistence (in-memory)

### TaskService
- Implements business logic for task operations
- Validates inputs before data operations
- Coordinates between repository and interface

### ConsoleInterface
- Handles user input and output
- Formats display of tasks
- Provides user feedback

### CommandParser
- Parses command-line input
- Routes commands to appropriate service methods
- Handles command validation

## Development Workflow

1. Follow the tasks outlined in `specs/todo-app/tasks.md`
2. Implement components in the order specified
3. Write tests as you implement functionality
4. Validate functionality after each component
5. Follow the MVC architecture pattern