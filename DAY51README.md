# D A Y F I F T Y O N E

## Project Goal
### Automagically test internet speed on speedtest.net, and tweet at your ISP

## driver.navigate vs driver.get ?

`<div class="result-label">Finding optimal server...</div>`

### Finding optimal server XPATH = `/div`
### server_box = `//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[3]/div/div`

## HOW TO TELL WHEN PAGE IS FINISHED LOADING:


## SETTING WINDOW POSITION:
`self.driver.set_window_position(500, 0, window_handle="current")`

## SNEAKY SELENIUM
```python
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
```

## SELENIUM VIRTUAL AUTHENTICATOR?!?!