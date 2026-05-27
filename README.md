# Smart Parking Lot System
A Smart Parking Lot System built using Flask, HTML, CSS, and Bootstrap that demonstrates
the use of Greedy Algorithms, Hashing, Queue, and Dynamic Pricing for efficient parking management.

---

# Features
- Greedy-based parking slot allocation (always picks first available slot)
- Hashing for O(1) vehicle search, insertion, and deallocation
- Queue handling when parking is full
- Automatic queue allocation after vehicle exit
- Dynamic parking pricing based on occupancy percentage
- Algorithm visualization popup on slot allocation (shows greedy steps live)
- Visual slot status (Free / Occupied)
- Vehicle search functionality
- Responsive modern dark UI using Bootstrap 5

---

# Technologies Used
- Python 3
- Flask
- HTML / CSS
- Bootstrap 5
- Jinja2 Template Engine

---

# DSA Concepts Used

## Greedy Algorithm
Used for parking slot allocation. Always picks the first available slot from
`available_slots[0]` without evaluating other options. After a vehicle is removed,
`available_slots.sort()` restores greedy order so the next allocation is always consistent.

## Hashing
`parked_vehicles` is a Python dictionary used as a hash map.
- Vehicle number is the key, slot is the value
- Park, search, and remove are all O(1) operations
- No iteration needed — direct memory access

## Queue (FIFO)
`waiting_queue` is a list that acts as a FIFO queue.
- When parking is full, vehicles are added to the rear
- When a slot frees up, the front vehicle is auto-allocated immediately
- Duplicate entries are prevented in `add_to_queue()`

## Dynamic Pricing
Threshold-based pricing recalculated on every request:
- 0–49% occupancy → Rs. 50
- 50–79% occupancy → Rs. 100
- 80%+ occupancy   → Rs. 150

---

# Algorithm Visualization
When a vehicle is successfully parked, a popup appears showing:
- All slots color-coded (free / occupied / chosen)
- The chosen slot highlighted with a pulse animation
- Step-by-step breakdown of how greedy picked the slot

---

# Project Structure
```text
parking-system/
│
├── app.py                  # Flask routes (park, remove, search, home)
│
├── parking/
│   ├── allocation.py       # Greedy allocation, hash map, slot management
│   ├── pricing.py          # Dynamic pricing logic
│   └── queue_handler.py    # Waiting queue management
│
├── templates/
│   └── dashboard.html      # Main UI with Jinja2 templating + viz popup
│
├── static/
│   └── style.css           # Dark theme styling
│
└── README.md
```

---

# How to Run
```bash
pip install flask
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

---
