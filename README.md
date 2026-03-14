# smart-parking-agent
## DCIT 403 – Intelligent Agent Project

### Project Overview

The **Smart Parking Agent System** is an intelligent multi-agent system designed to efficiently manage parking spaces in a parking lot. The system automatically assigns available parking spaces to vehicles when they arrive and updates the parking status when vehicles leave.

The system demonstrates the **Perceive → Decide → Act** cycle commonly used in intelligent agent design.

This project was developed as part of the **DCIT 403 Intelligent Agents course**.

---

# Problem Statement

In busy environments such as shopping malls, campuses, and office complexes, drivers often spend a lot of time searching for available parking spaces. This leads to traffic congestion, wasted fuel, and frustration.

The Smart Parking Agent solves this problem by automatically:

* Detecting available parking spaces
* Assigning parking spaces to incoming vehicles
* Updating the parking system when vehicles leave

---

# System Architecture

The system is composed of three main components:

### 1. Parking Management Agent

This is the **main intelligent agent** responsible for decision-making.

Responsibilities:

* Receive parking requests from vehicles
* Check available parking spaces
* Assign parking spaces
* Update the parking system

---

### 2. Sensor Agent

The **Sensor Agent perceives the environment** by detecting available parking spaces.

Responsibilities:

* Monitor parking space availability
* Send space status information to the Parking Management Agent

---

### 3. Parking Lot (Environment)

The **environment** where the agents operate.

It contains:

* Parking spaces
* Status of each parking space (Free or Occupied)

---

# Agent Behaviour

The Smart Parking Agent follows the **Perceive → Decide → Act** model:

### Perceive

The Sensor Agent detects the status of parking spaces.

### Decide

The Parking Management Agent determines whether a parking space is available.

### Act

The agent assigns a parking space to the vehicle or notifies the driver if the parking lot is full.

---

# System Interaction

Vehicle → Parking Management Agent → Sensor Agent → Parking Lot

Example interaction:

1. A vehicle requests parking.
2. The Parking Agent checks the Sensor Agent.
3. The Sensor Agent detects available spaces.
4. The Parking Agent assigns a space.
5. The parking system updates the environment.

---

# Project Structure

```
Smart-Parking-Agent
│
├── README.md
├── parking_lot.py
├── sensor_agent.py
├── parking_agent.py
├── main.py
```

### File Descriptions

**parking_lot.py**
Defines the parking environment and parking space status.

**sensor_agent.py**
Implements the Sensor Agent responsible for detecting available parking spaces.

**parking_agent.py**
Implements the Parking Management Agent responsible for assigning parking spaces.

**main.py**
Runs the simulation of the Smart Parking Agent system.

---

# Installation and Setup

### Step 1 – Clone the repository

```bash
git clone https://github.com/BenKhemical/smart-parking-agent.git
```

### Step 2 – Navigate to the project folder

```bash
cd Smart-Parking-Agent
```

### Step 3 – Run the program

```bash
python main.py
```

---

# Example Output

```
Parking Lot Status
P1 : Free
P2 : Free
P3 : Free
P4 : Free
P5 : Free

Car1 requesting parking...
Car1 assigned to P1

Car2 requesting parking...
Car2 assigned to P2

Car3 requesting parking...
Car3 assigned to P3

Car leaving P2
P2 is now available

Car4 requesting parking...
Car4 assigned to P2
```

---

# Technologies Used

* Python
* Git
* GitHub

---

# Learning Objectives

This project demonstrates:

* Intelligent Agent Design
* Multi-Agent System Interaction
* Environment Perception
* Decision Making in Agents
* Version Control with Git

