from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xlsxwriter

import pandas as pd

driver = webdriver.Chrome()
url = "https://www.nba.com/stats/teams/traditional/"

driver.get(url)

# Determine the number of seasons to collect

# season_val = "2020-21"
season_vals = []
for each in range(4):
    season_vals.append(f"202{each}-2{each+1}")

# print(season_vals)

season_drpdwn = Select(driver.find_element(By.CLASS_NAME,"DropDown_select__4pIg9"))
season_drpdwn.select_by_visible_text(season_vals[0])

# installed xlsx writer to open and write in excel workbook

# workbook = xlsxwriter.Workbook("nba_stats.xlsx")
# worksheet = workbook.add_worksheet(name=season_val)

#Console log info expected to receive from online nba stats chart

# installed lxml to print output of the table catupured

xpath_table = '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table'
table = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, xpath_table))).get_attribute("outerHTML")
# table = driver.find_element(By.TAG_NAME, "tr")
df = pd.read_html(table)[0]
df.dropna(how='all', axis=1, inplace=True)
print(df)

df.to_excel("nba_stats.xlsx",sheet_name=season_val)
# rows = len(driver.find_element)
# rows = 30
# cols = 27

# for row in range(rows):
#     for col in range(cols):
#         print(0)

# workbook.close()