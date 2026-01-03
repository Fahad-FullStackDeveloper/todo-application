# ADR-002: In-Memory Storage Architecture

## Status
Proposed

## Date
2026-01-03

## Context
The Todo application Phase I requires a storage solution for task data. The decision impacts data persistence, application complexity, and alignment with Phase I requirements. The application needs to store tasks during runtime but doesn't require persistence between application runs for this phase.

## Decision
We will implement in-memory storage using Python data structures (lists, dictionaries) instead of persistent storage solutions like databases or file systems. Task objects will be stored in memory during the application lifecycle and will be lost when the application exits.

## Alternatives Considered
- File-based storage (JSON, CSV): Would provide persistence but adds complexity for Phase I
- Database (SQLite, PostgreSQL): Overkill for Phase I requirements
- No storage: Would make the application non-functional
- Cloud storage: Inappropriate for a local CLI application

## Consequences
### Positive
- Simple implementation that matches Phase I MVP requirements
- No external dependencies required
- Fast read/write operations
- Minimal complexity for educational purposes
- Aligns with the "in-memory Python console app" requirement

### Negative
- Data is lost when the application exits
- Not suitable for production use
- May require significant refactoring in later phases when persistence is needed
- Limited scalability for large numbers of tasks

## References
- specs/todo-app/plan.md
- Project requirements for Phase I