#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time
import os
import json

def create_demo_forms():
    """Create realistic form automation demonstrations with screenshots."""
    screenshots_dir = "/tmp/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    results = {}

    # Create local HTML forms to demonstrate automation
    create_local_forms()

    with sync_playwright() as p:
        print("🚀 Starting Browser Form Automation Demo")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1400, 'height': 900})
        page = context.new_page()

        # Demo 1: Local Contact Form
        print("\n=== DEMO 1: Contact Form Automation ===")
        try:
            page.goto(f"file:///tmp/contact_form.html")
            page.screenshot(path=f"{screenshots_dir}/01_contact_form.png")
            print("📸 Screenshot: Contact form loaded")

            # Fill out the contact form
            page.fill('#name', 'John Doe')
            page.fill('#email', 'john.doe@example.com')
            page.fill('#phone', '(555) 123-4567')
            page.select_option('#subject', 'Technical Support')
            page.fill('#message', 'I need help with automating forms using browser automation tools. This is a demonstration of real-world form filling capabilities.')

            page.screenshot(path=f"{screenshots_dir}/02_contact_filled.png")
            print("📸 Screenshot: Contact form filled")

            page.click('#submit')
            page.wait_for_timeout(1000)
            page.screenshot(path=f"{screenshots_dir}/03_contact_submitted.png")
            print("✅ Contact form submitted successfully")

            results["contact_form"] = "Successfully filled and submitted contact form with personal details"

        except Exception as e:
            print(f"❌ Contact form error: {e}")
            results["contact_form"] = f"Error: {e}"

        # Demo 2: E-commerce Product Search
        print("\n=== DEMO 2: E-commerce Search Form ===")
        try:
            page.goto(f"file:///tmp/ecommerce_search.html")
            page.screenshot(path=f"{screenshots_dir}/04_ecommerce_landing.png")
            print("📸 Screenshot: E-commerce page loaded")

            # Search for products
            page.fill('#search-input', 'wireless headphones')
            page.select_option('#category', 'electronics')
            page.select_option('#price-range', '100-500')
            page.check('#free-shipping')

            page.screenshot(path=f"{screenshots_dir}/05_ecommerce_search_filled.png")
            print("📸 Screenshot: Search criteria filled")

            page.click('#search-btn')
            page.wait_for_timeout(1000)
            page.screenshot(path=f"{screenshots_dir}/06_ecommerce_results.png")
            print("✅ Product search executed successfully")

            results["ecommerce_search"] = "Successfully searched for wireless headphones in electronics category with price filter"

        except Exception as e:
            print(f"❌ E-commerce error: {e}")
            results["ecommerce_search"] = f"Error: {e}"

        # Demo 3: Registration Form
        print("\n=== DEMO 3: User Registration Form ===")
        try:
            page.goto(f"file:///tmp/registration_form.html")
            page.screenshot(path=f"{screenshots_dir}/07_registration_form.png")
            print("📸 Screenshot: Registration form loaded")

            # Fill registration form
            page.fill('#reg-username', 'automation_user_2024')
            page.fill('#reg-email', 'automation.user@testdomain.com')
            page.fill('#reg-password', 'SecurePassword123!')
            page.fill('#reg-confirm-password', 'SecurePassword123!')
            page.fill('#reg-first-name', 'Automation')
            page.fill('#reg-last-name', 'User')
            page.select_option('#reg-country', 'US')
            page.check('#terms-checkbox')
            page.check('#newsletter-checkbox')

            page.screenshot(path=f"{screenshots_dir}/08_registration_filled.png")
            print("📸 Screenshot: Registration form filled")

            page.click('#register-btn')
            page.wait_for_timeout(1000)
            page.screenshot(path=f"{screenshots_dir}/09_registration_submitted.png")
            print("✅ Registration form submitted successfully")

            results["registration"] = "Successfully created user account with secure credentials and preferences"

        except Exception as e:
            print(f"❌ Registration error: {e}")
            results["registration"] = f"Error: {e}"

        # Demo 4: Survey Form
        print("\n=== DEMO 4: Customer Survey Form ===")
        try:
            page.goto(f"file:///tmp/survey_form.html")
            page.screenshot(path=f"{screenshots_dir}/10_survey_form.png")
            print("📸 Screenshot: Survey form loaded")

            # Fill survey
            page.check('input[name="satisfaction"][value="very-satisfied"]')
            page.check('input[name="features"][value="ease-of-use"]')
            page.check('input[name="features"][value="performance"]')
            page.fill('#suggestions', 'The automation capabilities are excellent. Would like to see more integration options.')
            page.select_option('#recommendation', '9')
            page.check('#follow-up-yes')

            page.screenshot(path=f"{screenshots_dir}/11_survey_filled.png")
            print("📸 Screenshot: Survey form filled")

            page.click('#submit-survey')
            page.wait_for_timeout(1000)
            page.screenshot(path=f"{screenshots_dir}/12_survey_submitted.png")
            print("✅ Survey submitted successfully")

            results["survey"] = "Successfully completed customer satisfaction survey with detailed feedback"

        except Exception as e:
            print(f"❌ Survey error: {e}")
            results["survey"] = f"Error: {e}"

        print("\n🎉 All form automation demos completed successfully!")
        browser.close()

        # Save results
        with open("/tmp/form_results.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n📊 Results saved to /tmp/form_results.json")

        return screenshots_dir, results

def create_local_forms():
    """Create local HTML forms for demonstration."""

    # Contact Form
    contact_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Browser Automation Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
        .form-container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; color: #555; }
        input, select, textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; }
        textarea { height: 120px; resize: vertical; }
        button { background: #007bff; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .success { background: #d4edda; color: #155724; padding: 15px; border-radius: 4px; margin-top: 20px; display: none; }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>📧 Contact Us - Browser Automation Demo</h1>
        <form id="contact-form">
            <div class="form-group">
                <label for="name">Full Name *</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address *</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="subject">Subject</label>
                <select id="subject" name="subject">
                    <option value="">Select a subject...</option>
                    <option value="General Inquiry">General Inquiry</option>
                    <option value="Technical Support">Technical Support</option>
                    <option value="Billing Question">Billing Question</option>
                    <option value="Feature Request">Feature Request</option>
                </select>
            </div>
            <div class="form-group">
                <label for="message">Message *</label>
                <textarea id="message" name="message" required placeholder="Please describe your inquiry in detail..."></textarea>
            </div>
            <button type="submit" id="submit">Send Message</button>
        </form>
        <div class="success" id="success">✅ Thank you! Your message has been sent successfully.</div>
    </div>
    <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
            e.preventDefault();
            document.getElementById('success').style.display = 'block';
            this.style.display = 'none';
        });
    </script>
</body>
</html>"""

    # E-commerce Search Form
    ecommerce_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Search - E-commerce Demo</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f8f9fa; }
        .header { background: #343a40; color: white; padding: 20px; text-align: center; margin: -20px -20px 30px; }
        .search-container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .search-row { display: flex; gap: 20px; margin-bottom: 20px; align-items: end; }
        .search-group { flex: 1; }
        .search-group label { display: block; margin-bottom: 5px; font-weight: bold; color: #555; }
        .search-group input, .search-group select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
        .filters { display: flex; gap: 30px; margin: 20px 0; }
        .filter-group label { display: flex; align-items: center; gap: 8px; }
        .search-btn { background: #28a745; color: white; padding: 12px 30px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        .results { margin-top: 30px; padding: 20px; background: #e9ecef; border-radius: 4px; }
        .product { background: white; padding: 15px; margin: 10px 0; border-radius: 4px; border-left: 4px solid #28a745; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🛍️ Product Search - E-commerce Automation Demo</h1>
    </div>
    <div class="search-container">
        <form id="search-form">
            <div class="search-row">
                <div class="search-group">
                    <label for="search-input">Search Products</label>
                    <input type="text" id="search-input" name="search" placeholder="Enter product name or keywords...">
                </div>
                <div class="search-group">
                    <label for="category">Category</label>
                    <select id="category" name="category">
                        <option value="">All Categories</option>
                        <option value="electronics">Electronics</option>
                        <option value="clothing">Clothing</option>
                        <option value="home">Home & Garden</option>
                        <option value="sports">Sports & Outdoors</option>
                        <option value="books">Books</option>
                    </select>
                </div>
                <div class="search-group">
                    <label for="price-range">Price Range</label>
                    <select id="price-range" name="price">
                        <option value="">Any Price</option>
                        <option value="0-50">$0 - $50</option>
                        <option value="50-100">$50 - $100</option>
                        <option value="100-500">$100 - $500</option>
                        <option value="500+">$500+</option>
                    </select>
                </div>
            </div>
            <div class="filters">
                <div class="filter-group">
                    <label><input type="checkbox" id="free-shipping" name="shipping"> Free Shipping</label>
                </div>
                <div class="filter-group">
                    <label><input type="checkbox" name="prime"> Prime Eligible</label>
                </div>
                <div class="filter-group">
                    <label><input type="checkbox" name="sale"> On Sale</label>
                </div>
            </div>
            <button type="submit" id="search-btn" class="search-btn">🔍 Search Products</button>
        </form>
        <div id="results" class="results" style="display:none;">
            <h3>Search Results:</h3>
            <div class="product">
                <strong>Premium Wireless Headphones</strong><br>
                Price: $249.99 | Rating: ⭐⭐⭐⭐⭐ | Free Shipping ✅
            </div>
            <div class="product">
                <strong>Noise-Canceling Bluetooth Headphones</strong><br>
                Price: $179.99 | Rating: ⭐⭐⭐⭐ | Free Shipping ✅
            </div>
            <div class="product">
                <strong>Professional Studio Headphones</strong><br>
                Price: $399.99 | Rating: ⭐⭐⭐⭐⭐ | Free Shipping ✅
            </div>
        </div>
    </div>
    <script>
        document.getElementById('search-form').addEventListener('submit', function(e) {
            e.preventDefault();
            document.getElementById('results').style.display = 'block';
        });
    </script>
</body>
</html>"""

    # Registration Form
    registration_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration - Automation Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 30px auto; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .form-container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        h1 { color: #333; text-align: center; margin-bottom: 30px; }
        .form-row { display: flex; gap: 15px; }
        .form-group { margin-bottom: 20px; flex: 1; }
        label { display: block; margin-bottom: 5px; font-weight: bold; color: #555; }
        input, select { width: 100%; padding: 12px; border: 2px solid #e1e5e9; border-radius: 6px; font-size: 14px; transition: border-color 0.3s; }
        input:focus, select:focus { outline: none; border-color: #667eea; }
        .checkbox-group { display: flex; align-items: center; gap: 10px; margin-top: 15px; }
        .checkbox-group input { width: auto; }
        button { width: 100%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; margin-top: 20px; }
        button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .success { background: #d4edda; color: #155724; padding: 20px; border-radius: 6px; text-align: center; display: none; }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>👤 Create Your Account</h1>
        <form id="registration-form">
            <div class="form-group">
                <label for="reg-username">Username *</label>
                <input type="text" id="reg-username" name="username" required>
            </div>
            <div class="form-group">
                <label for="reg-email">Email Address *</label>
                <input type="email" id="reg-email" name="email" required>
            </div>
            <div class="form-group">
                <label for="reg-password">Password *</label>
                <input type="password" id="reg-password" name="password" required>
            </div>
            <div class="form-group">
                <label for="reg-confirm-password">Confirm Password *</label>
                <input type="password" id="reg-confirm-password" name="confirm-password" required>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label for="reg-first-name">First Name *</label>
                    <input type="text" id="reg-first-name" name="first-name" required>
                </div>
                <div class="form-group">
                    <label for="reg-last-name">Last Name *</label>
                    <input type="text" id="reg-last-name" name="last-name" required>
                </div>
            </div>
            <div class="form-group">
                <label for="reg-country">Country</label>
                <select id="reg-country" name="country">
                    <option value="">Select your country...</option>
                    <option value="US">United States</option>
                    <option value="CA">Canada</option>
                    <option value="UK">United Kingdom</option>
                    <option value="AU">Australia</option>
                    <option value="DE">Germany</option>
                    <option value="FR">France</option>
                </select>
            </div>
            <div class="checkbox-group">
                <input type="checkbox" id="terms-checkbox" name="terms" required>
                <label for="terms-checkbox">I agree to the Terms of Service and Privacy Policy *</label>
            </div>
            <div class="checkbox-group">
                <input type="checkbox" id="newsletter-checkbox" name="newsletter">
                <label for="newsletter-checkbox">Subscribe to our newsletter for updates</label>
            </div>
            <button type="submit" id="register-btn">Create Account</button>
        </form>
        <div class="success" id="reg-success">🎉 Account created successfully! Welcome aboard!</div>
    </div>
    <script>
        document.getElementById('registration-form').addEventListener('submit', function(e) {
            e.preventDefault();
            document.getElementById('reg-success').style.display = 'block';
            this.style.display = 'none';
        });
    </script>
</body>
</html>"""

    # Survey Form
    survey_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Survey - Feedback Demo</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 700px; margin: 40px auto; padding: 20px; background: #f0f2f5; }
        .survey-container { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; text-align: center; margin-bottom: 10px; }
        .subtitle { text-align: center; color: #666; margin-bottom: 30px; }
        .question-group { margin-bottom: 25px; padding: 20px; background: #fafbfc; border-radius: 8px; border-left: 4px solid #1a73e8; }
        .question { font-weight: bold; color: #333; margin-bottom: 15px; }
        .radio-group, .checkbox-group { display: flex; flex-direction: column; gap: 10px; }
        .radio-option, .checkbox-option { display: flex; align-items: center; gap: 10px; padding: 8px; }
        input[type="radio"], input[type="checkbox"] { margin: 0; }
        textarea { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; resize: vertical; height: 80px; }
        select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; }
        .submit-btn { width: 100%; background: #1a73e8; color: white; padding: 15px; border: none; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 20px; }
        .submit-btn:hover { background: #1557b0; }
        .thank-you { background: #e8f5e8; color: #2d5a2d; padding: 30px; text-align: center; border-radius: 8px; display: none; }
    </style>
</head>
<body>
    <div class="survey-container">
        <h1>📋 Customer Feedback Survey</h1>
        <p class="subtitle">Help us improve our browser automation services</p>

        <form id="survey-form">
            <div class="question-group">
                <div class="question">How satisfied are you with our automation platform?</div>
                <div class="radio-group">
                    <label class="radio-option">
                        <input type="radio" name="satisfaction" value="very-satisfied">
                        Very Satisfied
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="satisfaction" value="satisfied">
                        Satisfied
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="satisfaction" value="neutral">
                        Neutral
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="satisfaction" value="dissatisfied">
                        Dissatisfied
                    </label>
                </div>
            </div>

            <div class="question-group">
                <div class="question">Which features do you find most valuable? (Select all that apply)</div>
                <div class="checkbox-group">
                    <label class="checkbox-option">
                        <input type="checkbox" name="features" value="ease-of-use">
                        Ease of use
                    </label>
                    <label class="checkbox-option">
                        <input type="checkbox" name="features" value="performance">
                        Performance
                    </label>
                    <label class="checkbox-option">
                        <input type="checkbox" name="features" value="reliability">
                        Reliability
                    </label>
                    <label class="checkbox-option">
                        <input type="checkbox" name="features" value="documentation">
                        Documentation
                    </label>
                    <label class="checkbox-option">
                        <input type="checkbox" name="features" value="support">
                        Customer Support
                    </label>
                </div>
            </div>

            <div class="question-group">
                <div class="question">Additional comments or suggestions:</div>
                <textarea id="suggestions" name="suggestions" placeholder="Share your thoughts on how we can improve..."></textarea>
            </div>

            <div class="question-group">
                <div class="question">How likely are you to recommend our service? (0-10)</div>
                <select id="recommendation" name="recommendation">
                    <option value="">Select a rating...</option>
                    <option value="10">10 - Extremely likely</option>
                    <option value="9">9 - Very likely</option>
                    <option value="8">8 - Likely</option>
                    <option value="7">7 - Somewhat likely</option>
                    <option value="6">6 - Neutral</option>
                    <option value="5">5 - Somewhat unlikely</option>
                    <option value="4">4 - Unlikely</option>
                    <option value="3">3 - Very unlikely</option>
                    <option value="2">2 - Extremely unlikely</option>
                    <option value="1">1 - Would not recommend</option>
                    <option value="0">0 - Definitely would not recommend</option>
                </select>
            </div>

            <div class="question-group">
                <div class="question">May we contact you for follow-up questions?</div>
                <div class="radio-group">
                    <label class="radio-option">
                        <input type="radio" name="follow-up" value="yes" id="follow-up-yes">
                        Yes, you may contact me
                    </label>
                    <label class="radio-option">
                        <input type="radio" name="follow-up" value="no">
                        No, please don't contact me
                    </label>
                </div>
            </div>

            <button type="submit" id="submit-survey" class="submit-btn">Submit Survey</button>
        </form>

        <div class="thank-you" id="survey-thanks">
            <h2>🎉 Thank You!</h2>
            <p>Your feedback has been submitted successfully. We appreciate your time and input!</p>
        </div>
    </div>

    <script>
        document.getElementById('survey-form').addEventListener('submit', function(e) {
            e.preventDefault();
            document.getElementById('survey-thanks').style.display = 'block';
            this.style.display = 'none';
        });
    </script>
</body>
</html>"""

    # Write the HTML files
    with open("/tmp/contact_form.html", "w") as f:
        f.write(contact_html)
    with open("/tmp/ecommerce_search.html", "w") as f:
        f.write(ecommerce_html)
    with open("/tmp/registration_form.html", "w") as f:
        f.write(registration_html)
    with open("/tmp/survey_form.html", "w") as f:
        f.write(survey_html)

if __name__ == "__main__":
    screenshots_dir, results = create_demo_forms()
    print(f"\n📁 Screenshots saved to: {screenshots_dir}")
    print(f"\n📊 Results Summary:")
    for key, value in results.items():
        print(f"  • {key}: {str(value)[:80]}...")
    print(f"\n🎯 Form automation demonstration completed successfully!")