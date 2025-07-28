# GUI Testing Assignment – CSE 565

This project was developed as part of the CSE 565 course to explore graphical user interface (GUI) testing tools. The goal was to design and test a small GUI-based application using an automated GUI testing framework and evaluate its effectiveness.

# Project Overview

A grocery list management application was developed in two versions:

- **Version 1**: Original layout with a structured flow between pages.
- **Version 2**: Contains three visual changes per page and a modified navigation flow between the pages.

Each version includes three main pages:

1. **Index Page** – Entry page to input basic grocery settings.
2. **Add Page** – Allows adding new grocery items.
3. **Summary Page** – Displays and filters the summary of added items.

All pages include core GUI elements such as images, text boxes, buttons, labels, and at least two secondary elements like checkboxes, scrollbars, or sliders.

# Project Structure
gui-testing/
├── version-1/
│ ├── index.html
│ ├── add.html
│ ├── summary.html
│ └── 1.webp
│
├── version-2/
│ ├── index.html
│ ├── add.html
│ ├── summary.html
│ └── 1.webp
│
├── conftest.py # Playwright test fixture
├── test_gui.py # GUI test cases
│
├── report.pdf
├── requirements.pdf
├── report.html # Summary of passed/failed cases
│
└── README.md
# Technologies Used

- **Programming Language**: Python
- **Testing Framework**: Playwright (with `pytest`)


# Test Coverage

The following aspects were tested for both versions of the application:

- **Element existence**: Verifies visibility of all expected GUI elements.
- **Size and location**: Confirms element dimensions and placement.
- **Orientation**: Checks layout direction using CSS flex properties.
- **Navigation flow**: Validates button clicks and transitions between pages.

# Sample Test Scenarios

- Confirm index image width is 300px.
- Validate location of `.form-elements` block on the index page.
- Ensure button group orientation is horizontal (`flex-direction: row`).
- Test full navigation from index → add → summary page.
- Check visibility of buttons, inputs, images, and filters across all pages.

# To Run
pytest test_gui.py --html=report.html

