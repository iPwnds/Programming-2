# Exercise logger app

Consider the starter code (in `starter_code.py`). It is part of an implementation of a new exercise logging app we're developing.

In this application, we will be able to log three types of exercises: `Run`'s, `Ride`'s and `Swim`'s. These three classes have several things in common:

- fields:
  - `date`
  - `distance`
  - `duration`
- methods/properties
  - `is_valid_date`
  - `calories`

Nonetheless, these three classes also have their differences:

- Run and Ride also keep track of an elevation factor, Swim (obviously) does not.
- though the `calories` property is the same for all classes, the property `calories_factor` is computed differently.

## Important: Avoid code duplication
Throughout these questions, we expect you to implement solutions in a way that avoids unnecessary code duplication using the principles you've learned throughout the semester.

## Copy the code
Create a copy of the starter code in `student.py`. Implement all following questions in this file.

## Question 1: Refactor the code
As we've seen, though the `Run`, `Swim` and `Ride` classes have their differences, they also share code. In a new file `student.py`, Create an appropriate abstract class `Exercise` and reimplement `Run`, `Swim` and `Ride` such that they inherit from this `Exercise` class and minimizing code duplication. Where appropriate, use abstract methods or properties to enforce that each subclass provides its own implementation for behavior that differs.

> Tip: At the bottom of the file you can find some example usage. Use this example usage to make sure changes you make don't break the application.

## Question 2: Operator overloading

After we have created exercises, we would also like to compare the effectivity of each exercise. Make sure exercise sessions are compared by calories spent, like shown in the example below.

```
>>> morning_run = Run("2023-10-02", 5, 21, 12)
>>> morning_run.calories
800
>>> evening_bike_ride = Ride("2023-10-01", 20, 60, 0)
>>> evening_bike_ride.calories
800
>>> morning_run == evening_bike_ride
True
>>> morning_run < evening_bike_ride
False
>>> morning_run > evening_bike_ride
False
```

## Question 3: static method

For one of the methods in the code it would be more appropriate to convert this method into a static method. Convert this method into a static method and change all of the other code to reflect this change (make sure the code still works).

## Question 4: `is_valid_date`
The current implementation of `is_valid_date` can also be improved upon. Use a single regex string to reduce this method in size.

## Question 5: Comprehensions

Using comprehensions, implement following methods:

- a method `filter(self,condition)` for the class `ExerciseLog` which returns a list of the Exercise items, filtered on a certain condition.
- a method `filter_by_date(self, date)` which returns a list of the Exercise items, where the Exercise's date must match the given `date`.
- a method `filter_by_distance(self, min_distance)` which returns a list of the Exercise items, where the exercise's distance must be at least the length of the given parameter `min_distance`.

## Question 6: testing

Write tests for the Swim class.

- For the constructor include the following:
  - at least one succesful creation of a Swim object
  - test that exceptions are raised in the appropriate cases
- Write a parameterized test for the `calories` property

