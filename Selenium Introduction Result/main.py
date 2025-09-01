import time
import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SeleniumWebDriverContextManager:  # 1 Context Manager for Selenium WebDriver
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            self.driver.quit()


def extract_table(driver: WebDriver):
    """Extract table content and save it to a CSV file."""
    try:
        # Locate the table
        table = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "table"))
        )
        columns = table.find_elements(By.CLASS_NAME, "y-column")
        table_dict = {}
        # Extract table headers and content
        for column in columns:
            header = column.find_element(By.ID, "header").text.strip()
            cells = [
                cell.text.strip()
                for cell in column.find_elements(By.CLASS_NAME, "cell-text")
                if cell.text.strip() != header
            ]
            table_dict[header] = cells
        # Save table content to CSV
        df = pd.DataFrame(table_dict)
        df.to_csv("table.csv", index=False)
        print("Table content saved to table.csv")
    except TimeoutException:
        print("Error: Table not found within the timeout period.")
    except NoSuchElementException as e:
        print(f"Error: Missing element in table extraction - {e}")


def extract_doughnut_chart(driver: WebDriver):
    """Iterate through doughnut chart filters, take screenshots, and save data to CSV files."""
    try:
        # Locate the scrollbox containing doughnut chart filters
        doughnut_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scrollbox"))
        )
        filter_elements = doughnut_filter.find_elements(By.CLASS_NAME, "traces")
        for index, filter_element in enumerate(filter_elements):
            if index == 0:
                # Screenshot of the initial unfiltered state
                driver.save_screenshot(f"screenshot{index}.png")
                print(f"Screenshot saved: screenshot{index}.png")
                save_doughnut_data(driver, index)
            # Click on the filter and wait for the chart to update
            filter_element.click()
            time.sleep(1)  # Use WebDriverWait if possible for better reliability
            driver.save_screenshot(f"screenshot{index + 1}.png")
            print(f"Screenshot saved: screenshot{index + 1}.png")
            save_doughnut_data(driver, index + 1)
    except TimeoutException:
        print("Error: Doughnut chart filters not found within the timeout period.")
    except NoSuchElementException as e:
        print(f"Error: Missing element in doughnut chart extraction - {e}")


def save_doughnut_data(driver: WebDriver, index: int):
    """Extract doughnut chart data and save it to a CSV file with schema: Facility Type, Min Average Time Spent."""
    try:
        doughnut = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pielayer"))
        )
        # Extract the slices of the doughnut chart
        doughnut_elements = doughnut.find_elements(By.CSS_SELECTOR, "text.slicetext[data-notex='1']")
        # Extract data from the doughnut chart
        doughnut_data = []
        for doughnut_element in doughnut_elements:
            # Try locating <tspan> elements using find_elements(By.TAG_NAME, "tspan")
            tspans = doughnut_element.find_elements(By.TAG_NAME, "tspan")
            # First <tspan> contains Facility Type
            facility_type = tspans[0].text.strip()
            # Second <tspan> contains Min Average Time Spent
            min_average_time_spent = tspans[1].text.strip()
            # Append the data to the list
            doughnut_data.append({
                "Facility Type": facility_type,
                "Min Average Time Spent": min_average_time_spent
            })
        # Save data to a CSV file
        df = pd.DataFrame(doughnut_data)
        df.to_csv(f"doughnut{index}.csv", index=False)
        print(f"Doughnut chart data saved to doughnut{index}.csv")
    except TimeoutException:
        print(f"Error: Doughnut chart not found for filter index {index}.")
    except NoSuchElementException as e:
        print(f"Error: Missing element in doughnut chart data extraction - {e}")


if __name__ == "__main__":
    with SeleniumWebDriverContextManager() as driver:  # 1 Context Manager for Selenium WebDriver
        # Open the HTML report file
        html_file_path = os.path.abspath("report.html")
        driver.get(f"file://{html_file_path}")
        # Zoom for screenshots
        driver.execute_script("document.body.style.zoom='75%'")
        time.sleep(0.5)
        # 2 Extract table content
        extract_table(driver)
        # 3 Extract doughnut chart data
        extract_doughnut_chart(driver)
