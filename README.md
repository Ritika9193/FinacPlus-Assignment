# Coding Challenge Solutions

## Question 1: Special Cipher
> Write a special cipher that is a combination of Caesar’s cipher followed by a simple RLE. The function should receive a string and the rotation number as parameters.

**Input:** `specialCipher("AABCCC", 3)`
**Output:** `D2EF3`

### Solution and Explanation
The solution is implemented in Python.

-   **Code:** `Q1/special_cipher.py`
-   **Tests:** `Q1/test_special_cipher.py`

### How to Run
To run the tests for this solution, navigate to the root directory of this project and execute the following command:
```bash
python Q1/test_special_cipher.py
```

---

## Question 2: Denomination Optimizer
> Write a program that finds the most optimized set of 6 units to shop with for values fewer than 100.

**Example:**
-   Units used are 1, 2, 5, 10, 20, 50
-   1: 1 (1 unit used)
-   2: 2 (1 unit used)
-   3: 1+2 (2 units used)
-   ...
-   98: 1+2+5+20+20+50 (6 units used)
-   99: 2+2+5+20+20+50 (6 units used)
-   AVG of units = 3.4

### Solution and Explanation
The solution is implemented in Python.

-   **Code:** `Q2/denomination_optimizer.py`
-   **Tests:** `Q2/test_denomination_optimizer.py`

### How to Run
To run the tests for this solution, navigate to the root directory and execute the following command:
```bash
python Q2/test_denomination_optimizer.py
```

---

## Question 3: Amazon Product Metadata
> Imagine you work for Amazon. What is the metadata information you will store for an item in your Database? For e.g. the item is a a shirt. Once you have stored the metadata, how will you use the information?

### Solution and Explanation
The detailed answer, including a proposed database schema and how the metadata would be utilized, is provided in the markdown file below.

-   **Location:** `Q3/amazonProductMetaData.md`

---

## Question 4: High-Level System Design
> Represent the following problem in a high-level design diagram:
> - Have a set of 250 users.
> - Each user has at least one account with assets (stocks or mutual funds).
> - Each user will see his portfolio in real-time at any time of the day.
> - Prices come from different sources.
> - Design a platform to create, calculate, and maintain the portfolios of these users.
> - It should be reliable and scalable.
> - The portfolios should be updated as soon as the source provides data.
> - The data gets refreshed every 10 mins.

### Solution and Explanation
A high-level design diagram, key components, and design considerations for this system are documented in the markdown file below.

-   **Location:** `Q4/AssetViewProductHld.md`


## Created Demo Project Also

A demo implementation of this architecture has been created:

- **GitHub Repository:** [https://github.com/Ritika9193/WealthWatch](https://github.com/Ritika9193/WealthWatch)
- **Live Project:** [https://wealth-watch-three.vercel.app/dashboard](https://wealth-watch-three.vercel.app/dashboard)

You can explore the live dashboard and review the codebase.            
Note - The asset and trading services work only on localhost, as they use local storage with mock data for simulation.

---

### Submitted by:
- **Name:** Ritika
- **Contact:** 8979716127
- **Email:** ritika22022003@gmail.com
- **Portfolio:** https://terminal-portfolio-phi-topaz.vercel.app/
