# Save as /tmp/excalidraw_automation.py
from playwright.sync_api import sync_playwright
import time
import os

def draw_rectangle(page, x, y, width, height):
    """Draw a rectangle at the specified position."""
    # Select rectangle tool
    page.keyboard.press("r")
    time.sleep(0.3)

    # Click and drag to create rectangle
    page.mouse.move(x, y)
    page.mouse.down()
    page.mouse.move(x + width, y + height)
    page.mouse.up()
    time.sleep(0.3)

def draw_arrow(page, x1, y1, x2, y2):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    page.keyboard.press("a")
    time.sleep(0.3)

    page.mouse.move(x1, y1)
    page.mouse.down()
    page.mouse.move(x2, y2)
    page.mouse.up()
    time.sleep(0.3)

def add_text(page, x, y, text):
    """Add text at the specified position."""
    page.keyboard.press("t")
    time.sleep(0.3)

    page.mouse.click(x, y)
    time.sleep(0.2)
    page.keyboard.type(text, delay=30)
    time.sleep(0.2)

    # Click elsewhere to finish text
    page.keyboard.press("Escape")
    time.sleep(0.2)

def automate_excalidraw():
    """Create a simple architecture diagram in Excalidraw."""
    screenshots_dir = "/tmp/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
            proxy={'server': 'http://127.0.0.1:8888'}
        )
        context = browser.new_context(
            viewport={'width': 1400, 'height': 900},
            ignore_https_errors=True
        )
        page = context.new_page()

        print("Step 1: Navigate to Excalidraw")
        page.goto("https://excalidraw.com/")
        time.sleep(4)  # Wait for canvas to load
        page.screenshot(path=f"{screenshots_dir}/01_excalidraw_loaded.png")
        print("Screenshot: 01_excalidraw_loaded.png")

        print("Step 2: Close any welcome dialogs")
        # Try to close the welcome screen by clicking outside the menu area
        # The welcome screen appears to be centered, so click in an empty area
        page.mouse.click(200, 200)  # Click in top-left empty area
        time.sleep(1)

        # Press Escape multiple times to ensure any dialogs are closed
        page.keyboard.press("Escape")
        time.sleep(0.5)
        page.keyboard.press("Escape")
        time.sleep(0.5)

        # Try clicking on the canvas background area
        page.mouse.click(700, 450)
        time.sleep(1)

        page.screenshot(path=f"{screenshots_dir}/02_canvas_ready.png")
        print("Screenshot: 02_canvas_ready.png")

        # === Create a simple 3-tier architecture diagram ===
        # Layout:
        #   [Client]
        #      |
        #      v
        #   [Server]
        #      |
        #      v
        #   [Database]

        print("Step 3: Draw Client box")
        draw_rectangle(page, 550, 100, 200, 80)
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/03_client_box.png")
        print("Screenshot: 03_client_box.png")

        print("Step 4: Add 'Client' label")
        add_text(page, 610, 130, "Client")
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/04_client_label.png")
        print("Screenshot: 04_client_label.png")

        print("Step 5: Draw Server box")
        draw_rectangle(page, 550, 280, 200, 80)
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/05_server_box.png")
        print("Screenshot: 05_server_box.png")

        print("Step 6: Add 'Server' label")
        add_text(page, 610, 310, "API Server")
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/06_server_label.png")
        print("Screenshot: 06_server_label.png")

        print("Step 7: Draw Database box")
        draw_rectangle(page, 550, 460, 200, 80)
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/07_database_box.png")
        print("Screenshot: 07_database_box.png")

        print("Step 8: Add 'Database' label")
        add_text(page, 600, 490, "Database")
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/08_database_label.png")
        print("Screenshot: 08_database_label.png")

        print("Step 9: Draw arrow from Client to Server")
        draw_arrow(page, 650, 180, 650, 280)
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/09_arrow1.png")
        print("Screenshot: 09_arrow1.png")

        print("Step 10: Draw arrow from Server to Database")
        draw_arrow(page, 650, 360, 650, 460)
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/10_arrow2.png")
        print("Screenshot: 10_arrow2.png")

        print("Step 11: Take final screenshot")
        # Press V to switch to selection tool and click away
        page.keyboard.press("v")
        time.sleep(0.3)
        page.mouse.click(100, 100)  # Click away from objects
        time.sleep(0.5)
        page.screenshot(path=f"{screenshots_dir}/11_final_diagram.png")
        print("Screenshot: 11_final_diagram.png")

        print("Step 12: Export the diagram")
        # Try to export using menu
        # Ctrl+Shift+E opens export dialog in Excalidraw
        page.keyboard.press("Control+Shift+e")
        time.sleep(1)
        page.screenshot(path=f"{screenshots_dir}/12_export_dialog.png")
        print("Screenshot: 12_export_dialog.png")

        # Try clicking "Export image" button if visible
        export_btn = page.locator('button:has-text("Export"), [aria-label*="Export"]')
        if export_btn.count() > 0:
            export_btn.first.click()
            time.sleep(1)
            page.screenshot(path=f"{screenshots_dir}/13_export_options.png")

        print("Done!")
        browser.close()
        return screenshots_dir

if __name__ == "__main__":
    dir = automate_excalidraw()
    print(f"\nScreenshots saved to: {dir}")