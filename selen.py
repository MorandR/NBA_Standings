from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xlsxwriter

import pandas as pd

driver = webdriver.Chrome()
url = "https://www.nba.com/stats/teams/traditional?Outcome=&SeasonType=Regular+Season"

driver.get(url)

# Determine the number of seasons to collect

season_val = "2020-21"
# season_vals = []
# for each in range(2):
#     season_vals.append(f"202{each}-2{each+1}")

# print(season_vals)

season_drpdwn = Select(driver.find_element(By.CLASS_NAME,"DropDown_select__4pIg9"))
season_drpdwn.select_by_visible_text(season_val)

# time.sleep(10)



# installed xlsx writer to open and write in excel workbook

# workbook = xlsxwriter.Workbook("nba_stats.xlsx")
# worksheet = workbook.add_worksheet(name=season_val)


# worksheet.write('B5', "RHIZA")


#Console log info expected to receive from online nba stats chart

# installed lxml to print output of the table catupured

table = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table'))).get_attribute("outerHTML")
# table = driver.find_element(By.TAG_NAME, "tr")
print(pd.read_html(table))


# table.to_excel("nba_statss.xlsx")
# rows = len(driver.find_element)
# rows = 30
# cols = 27

# for row in range(rows):
#     for col in range(cols):
#         print(0)

# workbook.close()