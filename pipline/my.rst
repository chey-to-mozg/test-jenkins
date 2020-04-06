=====================================
  Robot Framework Quick Start Guide
=====================================

.. code:: robotframework

    *** Test Cases ***
    Compress positive number
        Compare number   5
        Status Should Be    GREATER

    Compress negative number
        Compare number   -5
        Status Should Be    LOWER

    Compress zero number
        Compare number   0
        Status Should Be    ZERO
.. code:: robotframework

    *** Settings ***
    Library           lib.py

    *** Keywords ***

    Compare number
        [Arguments]    ${number}
        Compare        ${number}
