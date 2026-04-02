## Tablet Automation Test – TinyKola App (Appium + Python)

This script automates a complete end-to-end workflow for the TinyKola Tablet application using Appium with Python. It simulates real user interactions including login, printer setup, category configuration, and order processing.

---

### Overview

The automation validates a full business flow in the tablet application, including:

* Handling app and system permissions
* Logging into the application
* Configuring printer settings
* Selecting paper type and print format
* Managing categories
* Performing test print
* Navigating to Orders module
* Searching and selecting items
* Printing KOT (Kitchen Order Ticket)

This ensures both functional and operational workflows of the application are working correctly.

---

### Code Reference

Main script:


---

### Technologies Used

* Python
* Appium (UiAutomator2 Driver)
* Selenium WebDriver
* Pytest

---

### Key Components

#### 1. Safe Interaction Methods

Custom utility functions are used:

* `safe_tap()` → handles element clicking
* `safe_type()` → uses mobile-specific typing method

These improve interaction reliability on tablet devices.

---

#### 2. Permission Handling

The script dynamically handles:

* App-level permissions (Allow / Not Now)
* Android system permission dialogs

This ensures smooth execution without manual interruption.

---

#### 3. Locator Strategy

Multiple locator strategies are used:

* **Accessibility ID** → primary and most stable
* **UIAutomator (scrollIntoView)** → for off-screen elements
* **XPath** → used only when necessary
* **Class Name / ID** → for input fields

---

### Test Flow Breakdown

#### 1. App Launch

* Initialize driver with capabilities
* Start Appium session
* Wait for login screen

---

#### 2. Login Flow

* Enter email using mobile typing
* Hide keyboard to avoid UI blocking
* Click Continue
* Select Password option
* Enter password
* Click Sign In

---

#### 3. Validation

* Verify successful login by checking presence of Settings

---

#### 4. Printer Configuration

* Navigate to Settings
* Open Printer section
* Discover available printers
* Select printer

---

#### 5. Print Setup

* Choose paper type (58mm thermal paper)
* Select print type (Print All)
* Scroll to locate options dynamically

---

#### 6. Category Configuration

* Select categories
* Save category configuration

---

#### 7. Test Print

* Execute test print to validate setup

---

#### 8. Order Flow

* Navigate to Orders
* Search for item (Biryani)
* Select item from results

---

#### 9. Order Processing

* Print KOT
* Confirm selection

---

### Wait Strategy

* Explicit waits (`WebDriverWait`) for reliable synchronization
* `time.sleep()` used for UI transitions where required
* Scroll handling using `UiScrollable` for dynamic content

---

### Challenges Faced

#### 1. Element Interaction Issues

* Some elements were not directly clickable
* Required fallback strategies like coordinate tapping

#### 2. Keyboard Interference

* On-screen keyboard blocked elements
* Resolved using `hide_keyboard()`

#### 3. Dynamic Content Loading

* Elements not visible initially
* Handled using scroll-based locators

---

### Best Practices Followed

* Preferred Accessibility ID for stability and speed
* Avoided deep XPath hierarchies
* Used reusable utility functions for actions
* Handled edge cases like keyboard blocking
* Ensured modular and readable structure

---

### How to Run

1. Start Appium server:

   ```
   appium
   ```

2. Connect tablet device or emulator

3. Run test:

   ```
   pytest mobile_automation.py -v
   ```

---

### Outcome

This automation script validates:

* End-to-end business workflow
* Printer configuration and printing functionality
* Order management process

It ensures the application is ready for real-world usage in a tablet-based environment.

---

### Future Improvements

* Replace static waits with dynamic synchronization
* Add assertions for validation checkpoints
* Implement Page Object Model (POM)
* Add logging and reporting
* Integrate with CI/CD pipelines

---

This project demonstrates practical expertise in mobile/tablet automation, handling real-world challenges such as dynamic UI elements, permission handling, and device-specific issues.
