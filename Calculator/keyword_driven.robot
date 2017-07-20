*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``CalculatorLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           CalculatorLibrary.py

*** Test Cases ***
Push button
    Push button    1
    Result should be    1

Push multiple buttons
    #Test if you can enter 2 digit number e.g. 12

Simple calculation
    #Test if you can enter whole calculation by pushing individual buttons

Longer calculation
    #Test calculation using push buttons keyword

Clear
    #Test if input is cleared using the 'C' button
