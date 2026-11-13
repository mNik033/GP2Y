# Google AI Pro (5 TB) Zero-Cost Two-Year Automation Console

A console for automating the activation and management of Google AI Pro (5 TB) benefits, built with FastAPI + Playwright + CDP. It provides a local visual web UI, batch account scheduling, tax-free-region card binding, and the full flow of cancelling auto-renewal.

---

## 📌 Features

- **Visual console**: A modern web UI that monitors each account's execution status, current step, expiry date, and returned screenshots in real time.
- **Multi-format bulk account import**: Quickly enter accounts with plain passwords, recovery-email verification, or 2FA/TOTP secrets.
- **Fully automated flow**:
  - Handles Google sign-in and multi-factor verification automatically
  - Fills in a billing address in a tax-free region (e.g. Oregon, a no-sales-tax state) and binds the card
  - Stacks offers step by step: 12 months + 6 months + 6 months (up to 24 months of benefits)
  - Goes to Google Play to cancel auto-renewal and lock in the expiry date
- **Safeguard and US$0.00 check**: The script confirms the amount is `US$0.00`; any non-zero subscription is blocked and reported as an error.

---

## 💻 Requirements

1. **Operating system**: Windows 10 / 11
2. **Browser**: Google Chrome (installed in the default system path)
3. **Python**: Python 3.10 or later (check `Add Python to PATH` during installation)
4. **Network**: A system-wide US proxy (recommended), or a supported proxy address/template configured in the console panel

---

## 🚀 Quick Start

### Option 1: Launch scripts (recommended)

1. On first use, double-click: `1_首次运行_安装依赖并启动.bat` (First run: install dependencies and start)
2. For daily use afterwards, double-click: `2_启动控制台.bat` (Start console)
3. Once the console service starts, the browser opens automatically at `http://127.0.0.1:8765`

### Option 2: Manual command line

```bash
# 1. Install project dependencies
pip install -r requirements.txt

# 2. Start the service
python app.py
```

After startup, open the local port: [http://127.0.0.1:8765](http://127.0.0.1:8765)

---

## 📖 Usage Guide

### 1. Global configuration and payment card settings
1. Open the **Global Config & Inline Tax-Free Card Binding** section on the left of the console.
2. Enter the foreign-currency card (Visa / Mastercard) number, expiry date, CVC, and cardholder name used for verification.
3. The tax-free address is preset to a US Oregon ZIP code (`97201`); leave it unchanged unless you have a specific need.
4. Click **💾 Save Config**.

### 2. Bulk account import
In the **Bulk Account Import** area on the right of the page, paste account information (one per line). These common formats are supported:
```text
email----password----recovery_email
email----password----recovery_email----2FA_secret
email----password----2FA_secret
```
After pasting, click **➕ Import Account List** to add them to the execution queue.

### 3. Running tasks and monitoring progress
- **Single account**: Click **▶ Run** to the right of the target account.
- **Batch queue**: Click **▶ Run Batch Automatically** at the top of the list; the system runs the accounts one after another.
- **Execution steps**:
  - **Step 1**: Launch the browser, sign in to the Google account automatically, and complete security verification.
  - **Step 2**: Fill in the billing address, bind the card, and activate the first offer layer.
  - **Step 3**: Automatically stack the second free period.
  - **Step 4**: Stack the third offer period (capped at 24 months).
  - **Step 5**: Go to the Google Play subscription management page, cancel future auto-charges, lock in the two-year validity, and keep a verification screenshot.

---

## 📂 Directory Structure

```text
├── 1_首次运行_安装依赖并启动.bat    # First run: install dependencies and start
├── 2_启动控制台.bat              # Everyday start script
├── app.py                       # FastAPI backend service and route dispatch
├── automation_engine.py         # Core Playwright/CDP automation engine
├── templates/index.html         # Web console front-end page
├── requirements.txt             # Python dependency list
├── config.json                  # Local runtime configuration file
└── README.md                    # Project documentation
```

---

## ⚠️ Disclaimer

This project is intended only for automation testing and personal technical learning and research. It does not encourage or assist any behavior that violates the terms of service of the relevant platforms. Users bear full legal responsibility for all operations and consequences arising from the use of this tool; the author accepts no liability for any direct or indirect loss.
</Content>
