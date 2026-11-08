# LogiMatrix - Warehouse & Supply Chain Management System 📦🚚

LogiMatrix is a robust, fully object-oriented command-line logistics application built in Python. Designed to simulate real-world inventory management and supply chain tracking, this portal features dynamic warehouse storage controls, relational supplier mapping, safety stock triggers, and complete data persistence hooks.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Relational Inventory Ledger:** Add products under distinct tracking segments (Price, Category, Stock) backed by automated sequential ID trackers (`PID-1001`).
*   **Dynamic Supply Chain Dispatch:** Dispatches stock orders in real-time, automatically performing overdraft checks to prevent shipping non-existent inventory assets.
*   **Smart Low Stock Alerts:** Features automated safety threshold triggers that instantly flag warnings if individual product inventories drop **below or equal to 5 units**.
*   **Cross-Referenced Restocking:** Seamlessly updates stock quantities by linking transaction inputs directly with registered `Supplier ID` models (`SUP-5001`).
*   **Dual-Format Persistence Protocols:** 
    *   **CSV Table Exporter:** Generates standardized spreadsheets (`.csv`) for administrative review.
    *   **JSON Inventory Relational Dumper:** Flattens the entire multi-tier system dictionary tree into nested keys (`.json`) containing active product sheets and सप्लायर items arrays.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise supply chain prototype handles isolated logical entities and prevents memory state loss:
*   **Classes & System Architecture:** Structured modularly around independent logical objects: `Product`, `Supplier`, and `WarehouseManager` (the master coordination database).
*   **Composition & Relational Aggregation:** The `Supplier` instance hosts an internal catalog array mapping out stock names, while the `WarehouseManager` utilizes double-nested dictionaries mapping dynamic objects cross-referentially at runtime.
*   **Type Safety & String Sanitization:** Uses explicit `.strip()` data checks and string casing overrides to shield lookup references against unexpected text whitespace errors.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd logimatrix-warehouse-oop
    ```
3.  **Run the interactive logistical framework loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Standard utilities (`csv`, `json` are bundled natively inside default Python runtimes).
