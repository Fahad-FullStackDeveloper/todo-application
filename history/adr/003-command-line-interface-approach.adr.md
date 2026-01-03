# ADR-003: Command-Line Interface Approach

## Status
Proposed

## Date
2026-01-03

## Context
The Todo application Phase I requires selecting an appropriate user interface approach. The decision impacts user experience, development complexity, and alignment with Phase I requirements for a console application.

## Decision
We will implement a command-line interface (CLI) instead of a graphical user interface (GUI) or web interface. The application will accept commands through the terminal and provide text-based feedback to the user.

## Alternatives Considered
- Web interface: More user-friendly but adds complexity with web frameworks and server setup
- Desktop GUI: More intuitive for users but requires additional UI frameworks
- Mobile app: Inappropriate for Phase I requirements
- API-only: Would require separate client interface

## Consequences
### Positive
- Simple to implement and aligns with console app requirements
- Minimal dependencies and setup required
- Appropriate for educational purposes
- Follows Unix philosophy of simple, focused tools
- Easier to test and automate

### Negative
- Less user-friendly than GUI applications
- Requires users to learn command syntax
- More challenging for non-technical users
- Limited visual feedback compared to GUI applications

## References
- specs/todo-app/plan.md
- Project requirements for Phase I