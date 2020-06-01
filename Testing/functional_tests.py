from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/Users/Matt/bridge/Testing/geckodriver.exe')
browser.get('http://127.0.0.1:8000/')

assert 'blog' in browser.title

browser.quit()