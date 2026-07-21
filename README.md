# 🔐 Enterprise Random Password Generator

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Security](https://img.shields.io/badge/security-cryptographically%20secure-brightgreen.svg)
![NIST](https://img.shields.io/badge/NIST-SP%20800--63--4%20compliant-blueviolet.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A cryptographically secure password generator following NIST SP 800-63-4 guidelines**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Security](#security) • [Documentation](#documentation)

</div>

---

## 📋 Overview

The **Enterprise Random Password Generator** is a production-ready Python tool that generates cryptographically secure passwords using the `secrets` module instead of the predictable `random` module. Built following NIST SP 800-63-4 guidelines, this tool emphasizes **length over complexity** for superior security.

### Why This Matters

- ❌ **Legacy Approach**: `random.choice()` uses Mersenne Twister (predictable)
- ✅ **Enterprise Standard**: `secrets.choice()` uses OS entropy (unpredictable)
- 📊 **NIST Compliant**: 15+ character minimum recommendation
- ⚡ **Memory Efficient**: O(n) join() operation, no wasteful concatenation

---

## ✨ Features

### Core Capabilities
- 🔐 **Cryptographically Secure**: Uses Python's `secrets` module for hardware-level entropy
- 📏 **NIST Compliant**: Enforces 15+ character minimum (SP 800-63-4)
- 🎯 **Character Variety**: Includes uppercase, lowercase, digits, and special characters
- 🧮 **Entropy Calculation**: Displays password strength in bits
- ⏱️ **Crack Time Estimation**: Shows theoretical time to brute-force
- ⚡ **Memory Efficient**: Uses `.join()` for O(n) linear time complexity

### Security Metrics
| Metric | Description |
|--------|-------------|
| **Entropy** | Mathematical measure of password strength (bits) |
| **Character Set Size** | 94 possible characters |
| **Crack Time** | Estimated time at 1 billion attempts/second |
| **NIST Status** | Compliance check with 15-character guideline |

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses standard library only)

### Clone and Run
```bash
# Clone the repository
git clone https://github.com/yourusername/enterprise-password-generator.git

# Navigate to the directory
cd enterprise-password-generator

# Run the generator
python password_generator.py
