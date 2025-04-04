Here’s a **properly structured** and **well-formatted** `README.md` file with direct download links.  

---

# 🛒 Flipkart E-commerce Automation

## 📌 Project Overview  
This project automates the process of **searching for a mobile phone on Flipkart**, applying a price filter **(₹15,000 - ₹20,000)**, adding the product to the cart, and verifying that the correct product appears in the cart.

---

## **📂 Project Structure**
```
ecommerce-automation/
│── drivers/                   # Contains WebDriver (chromedriver.exe)
│── tests/                     # Test scripts
│   ├── test_add_to_cart.py    # Main test script
│── pages/                     # Page Object Model (POM) classes
│   ├── home_page.py           # Homepage actions
│   ├── product_listing_page.py # Product listing page actions
│   ├── product_page.py        # Product page actions
│── config.py                  # Configuration settings (URL, driver path)
│── README.md                  # Documentation
│── requirements.txt           # Python dependencies
```

---

## 🔧 **Setup & Installation**
### **1️⃣ Prerequisites**
Ensure you have the following installed:

| 🔗 Required Software       | 🔽 Direct Download Link |
|----------------------------|------------------------|
| **Python 3.10+**           | [Download Here](https://www.python.org/downloads/) |
| **Google Chrome (Latest Version)** | [Download Here](https://www.google.com/chrome/) |
| **Chrome WebDriver** (Same version as Chrome) | [Download Here](https://sites.google.com/chromium.org/driver/) |

> **⚠️ Note:**  
> - Place `chromedriver.exe` inside the `drivers/` folder.
> - Ensure the WebDriver version matches your **Chrome browser version**.

---

### **2️⃣ Install Dependencies**
Navigate to the project folder and install required Python packages:
```sh
pip install -r requirements.txt
```

---

### **3️⃣ Running the Test**
To execute the automation test, run:
```sh
python tests/test_add_to_cart.py
```

---

## 🚀 **How It Works**
1. **Opens Flipkart.**  
2. **Closes the login popup** (if present).  
3. **Searches for Mobiles.**  
4. **Applies a price filter ₹15,000 - ₹20,000.**  
5. **Selects the first product** from the results.  
6. **Switches to the product details page.**  
7. Clicks **"Add to Cart".**  
8. Opens the **Cart Page.**  
9. **Validates that the selected mobile is present in the cart.**  
10. **Passes/Fails** based on cart validation.  

---

## 🛠 **Troubleshooting**
### **❌ Issue: ModuleNotFoundError: No module named 'config'**
✅ **Solution:** Ensure `config.py` is in the root folder (not inside any subfolder).

### **❌ Issue: selenium.common.exceptions.NoSuchElementException**
✅ **Solution:** Flipkart might have changed its UI. Update **XPath** in `pages/*.py`.

### **❌ Issue: ChromeDriver Version Mismatch**
✅ **Solution:** Ensure **Chrome and ChromeDriver** versions are the same. Update ChromeDriver if needed.

---

## 📌 **Dependencies (`requirements.txt`)**
This file lists all the dependencies needed for the project.

```txt
selenium==4.10.0
webdriver-manager==4.0.1
unittest2==1.1.0
```

To install these dependencies, run:
```sh
pip install -r requirements.txt
```

---

## 👨‍💻 **Author**
**📌 Created by:** Aditya Singh  
📧 **Contact:** [singhaditya5298@gmail.com](mailto:singhaditya5298@gmail.com)  

---

This README is **clean, structured, and includes direct download links** for easy setup. 🚀 Let me know if you need modifications! 😊
