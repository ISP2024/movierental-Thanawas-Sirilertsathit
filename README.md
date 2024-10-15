## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.

## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

2.1. The code symptom is Feature Envy. Some fields moved to another class so it should also move to another class as well.
2.2. Single Responsibility Principle because Movie handle only movie detail stuff but Rental handle only price and point logic.
