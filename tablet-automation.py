from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#safe action
def safe_tap(element):
    element.click()

def safe_type(driver, text):
    driver.execute_script("mobile: type", {"text": text})

#to handle permissions
def handle_permissions(driver):
    for _ in range(10):
        try:
            #to handle app permissions
            allow_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Allow")
            if allow_btn:
                allow_btn[0].click()
                time.sleep(2)
                continue

            not_now_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Not Now")
            if not_now_btn:
                not_now_btn[0].click()
                time.sleep(2)
                continue

            #andriod system permissions
            allow_system = driver.find_elements(
                AppiumBy.XPATH,
                "//android.widget.Button[contains(@text,'Allow') or contains(@text,'While')]"
            )
            if allow_system:
                allow_system[0].click()
                time.sleep(2)
                continue

            break

        except Exception as e:
            print("Permission error:", e)
            break

#main code to test the full flow of the app
def test_full_flow():

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android"
    options.app_package = "com.tinykola.tablet"
    options.app_activity = "com.tinykola.tablet.MainActivity"
    options.automation_name = "UiAutomator2"
    options.no_reset = False
    options.new_command_timeout = 600

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    wait = WebDriverWait(driver, 30)

    #to handle the permissions
    handle_permissions(driver)

    print("Waiting for login screen...")
    wait.until(EC.presence_of_element_located(
        (AppiumBy.CLASS_NAME, "android.widget.EditText")
    ))

    #login flow
    print("Logging in...")

    email = wait.until(EC.presence_of_element_located(
        (AppiumBy.CLASS_NAME, "android.widget.EditText")
    ))
    safe_tap(email)

    safe_type(driver, "abhishek.k@gridsparksolutions.com") # add user name here
    time.sleep(1)

    # hide keyboard
    try:
        driver.hide_keyboard()
    except:
        driver.tap([(100, 100)])

    continue_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "CONTINUE")
    ))

    continue_btn.click()
    time.sleep(3)
    print("After continue screen loaded")

# ---------- CLICK PASSWORD BLOCK ----------
try:
    password_option = wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Password, Sign in with your password")
    ))
    password_option.click()
except:
    print("Normal click failed → trying tap")
    driver.tap([(900, 400)])  # adjust if needed

time.sleep(2)

# ---------- ENTER PASSWORD ----------
    password_field = wait.until(EC.presence_of_element_located(
        (AppiumBy.CLASS_NAME, "android.widget.EditText")    
    ))

    safe_tap(password_field)
    safe_type(driver, "abhi123")

# ---------- SIGN IN ----------
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "SIGN IN")
    )).click()


    # ---------- VALIDATION ----------
    wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Settings")
    ))

    print("Login successful")

    # ---------- SETTINGS ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Settings")
    )))

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "PRINTER")
    )))

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//android.widget.TextView[@text='Discover']")
    )))

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Select'])[1]")
    )))

    print("Printer selected")

    # ---------- PAPER ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID,
         "58mm Paper, Standard thermal paper (32 characters per line)")
    )))

    # ---------- PRINT TYPE ----------
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
        'new UiSelector().descriptionContains("Print All"))'
    )

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID,
         "Print All, KOT + Quick Bill + Finalize Bill (Recommended)")
    )))

    # ---------- CATEGORY ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "All Categories")
    )))

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//android.widget.TextView[@text='Save Categories']")
    )))

    # ---------- TEST PRINT ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Test Print")
    )))

    # ---------- ORDERS ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Orders")
    )))

    search = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ID, "search-bar")
    ))
    safe_tap(search)

    safe_type(driver, "Biryani")

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Biryani')]")
    )))

    print("Item selected")

    # ---------- PRINT KOT ----------
    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Print KOT")
    )))

    safe_tap(wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Select'])[1]")
    )))

    print("Flow completed successfully")

    time.sleep(5)
    driver.quit()