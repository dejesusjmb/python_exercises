*** Settings ***
Library           CalculatorLibrary

*** Test Cases ***
Addition
    Given calculator has been cleared
    When user types "1 + 1"
    and user pushes equals
    Then result is "2"

*** Keywords ***
calculator has been cleared
    Push button    C
user types "${input}"
    Push buttons  ${input}
user pushes equals
    Push button    =
result is "${result}"
    Result should be    ${result}
