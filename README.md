# Playwright UI Automation Demo

This is a demonstration of the usage of the Playwright library for UI automation.  
As an example was taken **[instagram.com](https://www.instagram.com)** web version of the application. 

## Features
* Framework is build on Paje Object Model pattern. It is accepted that main use case is a single usage of  
the page during test actions and usage of the same page duplicated several times across one test is considered  
rare, but ability to create several similar pages is provided.
* By default, page objects are created under the hood and are available inside test cases via ```self.*page_name*```.
* **TODO:** Page objects are decomposed into smaller Page Elements blocks.  
* `@cashed_property` is used to provide lazy loading of the page object.  
* Test cases grouped in test suites using class-as-test-suite approach.  
* Preconditions for the test cases provided via specialized intermediate classes from which test suite  
inherits.
* Snapshot testing feature is present (currently only as visual, doesn't work).

* **TODO:** for a specific type of testing (smoke, regression, etc.) pytest markers are used.

## Stack
- Python 3.13+
- Playwright
- Pytest
- Faker