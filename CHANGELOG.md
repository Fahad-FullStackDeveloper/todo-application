# Changelog

All notable changes to the Todo Application will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-01-04

### Added
- Priority management: assign priority levels (low, medium, high, urgent) to tasks
- Tag management: add, remove, and filter tasks by tags
- Search functionality: search tasks by title, description, or tags
- Filter functionality: filter tasks by status, priority, or tag
- Sort functionality: sort tasks by various fields (id, title, priority, creation date, due date)
- Due date management: set and track due dates for tasks
- Enhanced task display: show priority, tags, due dates in task listings
- New commands: search, filter, sort, tag, tagremove, priority, due
- Updated user interface to display all new task attributes
- Comprehensive testing for all new features
- Enhanced Task model with priority, tags, due date, and recurring fields
- Enhanced repository with search, filter, and sort methods
- Enhanced service layer with business logic for new features
- Updated command parser to handle new commands and arguments
- Updated documentation with new features and usage examples

### Changed
- Task model now includes priority (default: medium), tags, due date, and recurring fields
- Console interface now displays all task attributes including priority, tags, and due dates
- README updated with comprehensive documentation of all new features
- Version updated from 1.0.0 to 2.0.0 to reflect major feature enhancements

## [1.0.0] - 2026-01-03

### Added
- Core functionality: add, list, update, delete, complete, incomplete tasks
- In-memory storage implementation
- Command-line interface with interactive mode
- Task model with validation and completion tracking
- Repository layer for data access operations
- Service layer for business logic
- Interface layer for console input/output
- Command parser for processing user commands
- Unit tests for all components (35 tests)
- Integration tests for full workflow validation (4 tests)
- MVC architecture implementation
- Comprehensive documentation
- Demo script for functionality demonstration
- Version control system documentation