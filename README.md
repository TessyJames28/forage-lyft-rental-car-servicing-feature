# Clean Design, Refactoring, Unit Testing, and Test-Driven Development

## Clean Design for Existing Unfinished Component

1. Separate Concerns
2. Single Responsibility Principle (SRP)
3. Dependency Injection
4. Interface Segregation Principle (ISP)
5. Use Design Patterns
6. Remove Code Smells
7. Consistent Naming and Formatting

## Refactoring the Messy Codebase

1. Understand the Code
2. Break Down Large Functions
3. Remove Duplicate Code
4. Improve Naming and Documentation
5. Simplify Complex Logic
6. Remove Unused Code
7. Test as You Refactor
8. Refactor Gradually

## Writing Unit Tests for the Refactored System

1. Identify Testable Units
2. Write Test Cases
3. Use Appropriate Testing Framework
4. Arrange, Act, and Assert
5. Test for Correctness, Not Implementation Details
6. Mock Dependencies
7. Run Tests Regularly
8. Test Coverage

## Adding New Functionality using Test-Driven Development (TDD)

1. Write a Failing Test
2. Implement the Functionality
3. Refactor
4. Write Additional Tests
5. Repeat the Process


# UML DESIGN

## Serviceable

- `needs_service(): bool`

## Car

- `engine: Engine`
- `battery: Battery`
- `needs_service(): bool`

## Engine

- `needs_service(): bool`

### CapuletEngine

- `last_service_mileage: int`
- `current_milage: int`
- `needs_service(): bool`

### SternmanEngine

- `warning_light_on: bool`
- `needs_service(): bool`

### WilloughbyEngine

- `last_service_mileage: int`
- `current_milage: int`
- `needs_service(): bool`

## Battery

- `needs_service(): bool`

### SpindlerBattery

- `last_service_date: date`
- `current_date: date`
- `needs_service(): bool`

### NubbinBattery

- `last_service_date: date`
- `current_date: date`
- `needs_service(): bool`

## CarFactory

- `create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car`
- `create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car`
- `create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): Car`
- `create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car`
- `create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car`

Cars are accessed through the `Serviceable` interface. Rather than using a convoluted inheritance hierarchy, each car is composed of different parts. When `needs_service()` is called, the `Car` object calls `needs_service()` on each of its parts and returns `true` if any of them return `true`. Modifying the behavior of a part for all cars that contain that part can be accomplished by modifying a single piece of code. Adding a new part is as simple as creating a new class that implements the given interface. Adding additional types of parts to the service criteria can be accomplished by following the pattern set forth by `Engine` and `Battery`. Consult the strategy design pattern for additional context.

Cars are created by calling the corresponding `create` method on `CarFactory`. Changing the parts a car is composed of can be accomplished by modifying the corresponding `create` method.

