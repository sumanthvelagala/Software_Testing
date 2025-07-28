from playwright.sync_api import Page
from pathlib import Path
import urllib.parse


base_path = Path("/Users/Sumanth/Documentss/ASU/SVVP/GUI Testing/version-2").resolve()
def file_url(filename):
    return urllib.parse.urljoin("file:", base_path.joinpath(filename).as_uri())



def test_index_size(page: Page):
    page.goto(file_url("index.html"))
    image = page.locator("img")
    width = image.bounding_box()["width"]
    assert width == 300

def test_index_location(page: Page):
    page.goto(file_url("index.html"))

    form = page.locator(".form-elements")
    box = form.bounding_box()

    x = box["x"]
    y = box["y"]

    expected_x = 440
    expected_y = 317.984375

    assert x == expected_x
    assert y == expected_y



def test_index_orientation(page: Page):
    page.goto(file_url("index.html"))

    button_group = page.locator(".button-group")
    direction = button_group.evaluate("el => getComputedStyle(el).flexDirection")
    assert direction == "row"

def test_add_size(page: Page):
    page.goto(file_url("add.html"))

    img = page.locator("img")
    width = img.evaluate("el => el.offsetWidth")
    assert width == 300

def test_add_width(page: Page):
    page.goto(file_url("add.html"))
    
    form_container = page.locator('.form-container')
    form_container_width = form_container.evaluate("el => getComputedStyle(el).width")
    
    assert form_container_width == "400px"

def test_add_orientation(page: Page):
    page.goto(file_url("add.html"))
    button_group = page.locator(".button-group")
    direction = button_group.evaluate("el => getComputedStyle(el).flexDirection")
    assert direction == "row"


def test_summary_location(page: Page):
    page.goto(file_url("summary.html"))

    top_nav = page.locator(".top-nav")
    box = top_nav.bounding_box()
    
    x = box["x"]
    y = box["y"]

    expected_x = 20
    expected_y = 20

    assert x == expected_x
    assert y == expected_y


def test_summary_orientation(page: Page):
    page.goto(file_url("summary.html"))
    
    flex_container = page.locator(".filter-container")

    direction = flex_container.evaluate("el => getComputedStyle(el).flexDirection")
    assert direction == "row"

def test_summary_size(page: Page):
    page.goto(file_url("summary.html"))
    
    scrollbox = page.locator(".scrollbox")
    scrollbox_height = scrollbox.evaluate("el => getComputedStyle(el).height")
    
    expected_height = "200px" 

    assert scrollbox_height == expected_height



def test_full_navigation_flow(page: Page):

    page.goto(file_url("index.html"))
    assert "index.html" in page.url

    add_button = page.locator("button:has-text('Add Grocery')")
    assert add_button.count() > 0
    add_button.first.click()
    
    assert "add.html" in page.url

    summary_button = page.locator("button:has-text('Summary')")
    assert summary_button.count() > 0
    summary_button.first.click()

    assert "summary.html" in page.url

def test_index_elements_exist(page: Page):
    page.goto(file_url("index.html"))
    
    assert page.locator("h1").is_visible()
    assert page.locator("img").is_visible()
    assert page.locator("input[type='text']").is_visible()
    assert page.locator("#remember").is_visible()
    assert page.locator("#budget").is_visible()
    assert page.locator("button", has_text="Add Grocery").is_visible()
    assert page.locator("button", has_text="View Summary").is_visible()
def test_add_page_elements_exist(page: Page):
    page.goto(file_url("add.html"))
    
    assert page.locator("h2").is_visible()
    assert page.locator("img").is_visible()
    assert page.locator("#itemName").is_visible()
    assert page.locator("#itemQuantity").is_visible()
    assert page.locator("#itemDepartment").is_visible()
    assert page.locator("#itemDate").is_visible()
    assert page.locator("button", has_text="Submit").is_visible()
    assert page.locator("button", has_text="Clear").is_visible()
def test_summary_page_elements_exist(page: Page):
    page.goto(file_url("summary.html"))

    assert page.locator("h2").is_visible()
    assert page.locator("img").is_visible()
    assert page.locator("#dateFilter").is_visible()
    assert page.locator("#fruits").is_visible()
    assert page.locator("#veggies").is_visible()
    assert page.locator(".scrollbox").is_visible()
    assert page.locator("button", has_text="Apply Filters").is_visible()
    assert page.locator("button", has_text="Clear Filters").is_visible()
    assert page.locator("button", has_text="Clear All Items").is_visible()







