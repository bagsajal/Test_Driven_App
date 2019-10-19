from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'C:\Users\Dell\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
