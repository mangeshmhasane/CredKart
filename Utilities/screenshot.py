def take_screenshot(driver, request, status, path):
    test_name = request.node.name   # <-- auto test name
    file_name = f"{test_name}_{status}.png"
    driver.save_screenshot(f"{path}/{file_name}")
