# Expense Tracker Application

This Python-based application, built with Tkinter and ttkbootstrap, provides a user-friendly interface for tracking personal expenses. It allows users to input, categorize, view, and export their financial transactions.

## Table of Contents

-   Features
-   Getting Started
    -   Prerequisites
    -   Installation
    -   Running the Application
-   Usage
-   File Structure
-   Customization
-   Contributing
-   License

## Features

-   **Expense Input:** Easily record expenses with amount, category, and subcategory details.
-   **Categorization:** Organize expenses using predefined categories and subcategories for better financial overview.
-   **Expense Viewing:** Display expenses in a structured table (Treeview) for easy review.
-   **CSV Export:** Export expense data to a CSV file for external analysis or backup.
-   **Responsive UI:** Designed for usability on various screen sizes, including mobile.
-   **Modern Look:** Utilizes ttkbootstrap for a visually appealing and contemporary interface.
-   **Input Validation:** Ensures that the amount field only accepts numerical inputs.
-   **Dynamic Column Adjustment:** Automatically adjusts column widths in the Treeview to fit content.

## Getting Started

### Prerequisites

-   Python 3.x
-   ttkbootstrap library (install using `pip install ttkbootstrap`)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd expense-tracker-app
    ```

2.  Install the required dependencies:

    ```bash
    pip install ttkbootstrap
    ```

### Running the Application

Execute the Python script:

```bash
python expense_tracker.py
