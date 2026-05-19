# Smart Parking Lot System 

A Smart Parking Lot System built using Flask, HTML, CSS, and Bootstrap that demonstrates the use of Greedy Algorithms, Hashing, Queue, and O(1) optimized operations for efficient parking management.

---

# Features

- Greedy-based parking slot allocation
- O(1) optimized slot allocation using deque
- Hashing for fast vehicle search and deallocation
- Queue handling when parking becomes full
- Dynamic parking pricing based on occupancy
- Visual slot status (Free / Occupied)
- Vehicle search functionality
- Automatic queue allocation after vehicle exit
- Responsive modern UI using Bootstrap

---

# Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap
- Jinja Template Engine

---

# DSA Concepts Used

## Greedy Algorithm
Used for optimal parking slot allocation by assigning the first available slot.

## Hashing
Used for:
- Fast vehicle lookup
- Vehicle deallocation
- Vehicle-slot mapping

## Queue
Used to manage waiting vehicles when parking is full.

## Deque
Used for O(1) parking slot allocation and insertion.

---

# Project Structure

```text
parking-system/
│
├── app.py
│
├── parking/
│   ├── allocation.py
│   ├── pricing.py
│   └── queue_handler.py
│
├── templates/
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── README.md
