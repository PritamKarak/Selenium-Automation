<h2>Group Details</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Group No.</th>
    <th>Name</th>
    <th>Enrollment No.</th>
    <th>Section</th>
    <th>Roll</th>
    <th>Stream</th>
  </tr>
  <tr>
    <td>15</td>
    <td>Pranabesh Basu</td>
    <td>12023002028154</td>
    <td>C</td>
    <td>19</td>
    <td>CSE(AI & ML)</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Nilanjan Saha</td>
    <td>12023002028144</td>
    <td>C</td>
    <td>09</td>
    <td>CSE(AI & ML)</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Pritam Karak</td>
    <td>12023002028157</td>
    <td>C</td>
    <td>22</td>
    <td>CSE(AI & ML)</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Purba Chakraborty</td>
    <td>12023002028162</td>
    <td>C</td>
    <td>27</td>
    <td>CSE(AI & ML)</td>
  </tr>
</table>

# Description:

## Assignment 1: Web Element Identification

### Objective

To understand and implement fundamental Selenium locators to efficiently identify and interact with different types of web elements on a webpage.

### Description

This assignment focuses on locating web elements using standard Selenium WebDriver locators in Python. The solution demonstrates how to interact with various UI components on the given practice website, including finding a text box by ID, a checkbox by Name, a radio button by Class Name, a static dropdown by Tag Name, and a hyperlink using Link Text and Partial Link Text.

### Website

**Rahul Shetty Academy – Automation Practice**

https://rahulshettyacademy.com/AutomationPractice/

### Technologies Used

- Python
- Selenium WebDriver
- Google Chrome (or preferred browser)
- Basic DOM Locators

### Key Concepts

- Web Element Locators
- `By.ID` — Locating highly unique elements
- `By.NAME` — Locating form data elements
- `By.CLASS_NAME` — Locating elements by styling class
- `By.TAG_NAME` — Locating elements by HTML structure (e.g., `<select>`)
- `By.LINK_TEXT` & `By.PARTIAL_LINK_TEXT` — Locating anchor tags by visible text
- The Selenium `Select` Class (for static dropdown menus)
- Element Interactions (`.click()`, `.send_keys()`)
- `find_element()`
- Browser Automation

## Assignment 2: Multiple Element Identification Challenge

### Objective

To identify multiple elements of the same type on a webpage and use Selenium to find and work with the list of elements.

### Description

This assignment focuses on locating and interacting with collections of web elements using Selenium WebDriver in Python. The solution demonstrates how to retrieve multiple matching elements such as checkboxes and radio buttons using find_elements(), iterate through the resulting list, extract element attributes dynamically, and perform iterative actions like clicking and verifying the selection state.

### Website

Rahul Shetty Academy – Automation Practice
https://rahulshettyacademy.com/AutomationPractice/

### Technologies Used

- Python
- Selenium WebDriver
- WebDriver Manager
- Google Chrome
- Mozilla Firefox
- XPath
- CSS Selectors

### Key Concepts

- find_elements() vs find_element()
- List Iteration (For loops)
- Element State Verification (is_selected())
- Extracting Element Values (get_attribute())
- XPath Attribute Selectors
- CSS Attribute Selectors
- Browser Automation
- Checkbox and Radio Button Interaction

## Assignment 3: CSS Selector Challenge

###  Objective

To understand and implement **CSS wildcard selectors** in Selenium for locating web elements efficiently, especially when some parts of an element's attributes may change dynamically.

###  Description

This assignment focuses on locating web elements using **CSS Selectors in Selenium with Python**, including wildcard selectors for elements with fixed and dynamic attribute values. The solution demonstrates `^=`, `*=`, and `$=` selectors using the radio buttons on the given website.

### Website

Rahul Shetty Academy – Automation Practice
https://rahulshettyacademy.com/AutomationPractice/

###  Technologies Used

- Python
- Selenium WebDriver
- WebDriver Manager
- Google Chrome
- Mozilla Firefox
- CSS Selectors

###  Key Concepts

- CSS Attribute Selectors
- `^=` — Starts With
- `*=` — Contains
- `$=` — Ends With
- Dynamic Attribute Handling
- `find_element()`
- `find_elements()`
- Browser Automation
- Selenium WebDriver

## Assignment 4: Child Nodes Using CSS

### Objective
To identify and locate child or nested web elements using CSS child selectors and interact with the required elements.

### Description
In this assignment, Selenium is used with Python to demonstrate how CSS selectors can be used to locate nested web elements on the Rahul Shetty Academy Automation Practice website. The program demonstrates the use of the CSS child selector (`>`) to navigate through a parent-child relationship and locate the required radio button. It also demonstrates the CSS adjacent sibling selector (`+`) to locate an element based on its immediate sibling relationship. Finally, Selenium interacts with the located Radio2 element using the `click()` method.

### Website Used
Rahul Shetty Academy – Automation Practice

https://rahulshettyacademy.com/AutomationPractice/

### Key Concepts
- CSS Child Selector (`>`)
- CSS Adjacent Sibling Selector (`+`)
- Nested Web Element Identification
- Selenium `find_element()`
- Selenium `click()`

# Demo:
https://drive.google.com/drive/folders/16M-HYGTABzH6iExp5sYAtml8asAewDKS?usp=drive_link
