from selenium import webdriver
import varibles
import time

driver = webdriver.Firefox()

username = input("Your Student Number: ")
password = input("Your Student Password: ")


def main():
    driver.get(varibles.mainURL)
    print("Loading Page...")
    time.sleep(varibles.loadingTime)

    driver.find_element_by_xpath(varibles.classlinkLoginButtonXPATH).click()
    print("Pressing Button")
    time.sleep(varibles.loadingTime)

    driver.find_element_by_xpath(varibles.StudentNumberInputXpath).send_keys(username + "@brevardschools.org")
    print("Entering Username...")
    time.sleep(1)
    driver.find_element_by_xpath(varibles.StudentPasswordInputXpath).send_keys(password)
    print("Entering Password...")
    time.sleep(1)
    driver.find_element_by_xpath(varibles.SigninButtonXpath).click()
    print("Signing in...")
    time.sleep(varibles.focusLoadingTime)
    driver.find_element_by_xpath(varibles.FocusBtnXPath).click()
    print("Loading Focus...")
    time.sleep(varibles.focusLoadingTime)

    btn = driver.find_element_by_xpath(varibles.ImPresentButtonXPath)

    btn.click()
    print("Your Marked For Attendance")


main()
