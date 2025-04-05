WAIT_TIMEOUT = 10

PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

FIRST_NAME_FIELD = ("xpath", "//input[@ng-model='fName']")
LAST_NAME_FIELD = ("xpath", "//input[@ng-model='lName']")
POST_CODE_FIELD = ("xpath", "//input[@ng-model='postCd']")
ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//button[@type='submit']")

TABLE_DATA_ROWS_LIST = ("xpath", "(//table//tbody//tr)")
FIRST_NAME_TITLE = ("xpath", "//a[contains(text(),'First Name')]")

FIRST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[1])")
LAST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[2])")
POST_CODE_LIST = ("xpath", "(//tr[@class='ng-scope']//td[3])")
DELETE_BTN_LIST = ("xpath", "(//button[@ng-click='deleteCust(cust)'])")

BTN_MENU_LIST = ("xpath", "(//div[@class='center']//button)")