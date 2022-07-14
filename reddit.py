from selenium import webdriver
from selenium.webdriver.common.by import By

container = "rpBJOHq2PR60pnwJlUyP0" # Container name for all the memes and stuff

driver = webdriver.Chrome("C:\\Users\\take2\\Desktop\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://reddit.com/r/wholesomememes")

# Create a collection
i = 1
# Get first level child elements
for element in driver.find_element(By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0").find_elements(By.XPATH, "./*"): # No, I don't know what XPATH is either
    text = element.text
    # Sanitize the collection
    if text != "" and "PINNED BY MODERATORS" not in text and "u/Broclen" not in text and element.tag_name == "div" and "Gif" not in text and "Promoted" not in text:
        i += 1

        # hehe
        for h3 in element.find_elements(By.TAG_NAME, "h3"):
            h3h3 = h3.text

        # Extract the items from the collection
        for elmnt in element.find_elements(By.TAG_NAME, "img"):
            # Being short was never a bad thing, until now
            if elmnt.size["height"] > 99 and elmnt.size["width"] > 99:
                elmnt.screenshot(f"{h3h3}.png") # This method, it puts a smile on my face

driver.close()
print("\n\nHeist Complete")