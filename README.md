
# ATM Queue System Simulation 🏧

This project provides a discreet event simulation of an Automated Teller Machine (ATM) queueing system. It is designed to evaluate the performance and efficiency of the system under various operational configurations.

---

## 💡 Overview

The simulation models customer arrivals, queue formation, service times, and departure from a multi-ATM setup. By adjusting parameters like the number of ATMs, customer arrival rates, and service duration, you can quantify how changes affect critical performance metrics.

---

## ✨ Features

* **Configurable ATM Setup:** Easily adjust the number of available ATMs for service.
* **Variable Conditions:** Simulates customer traffic with varying arrival and service time distributions.
* **Metric Tracking:** Monitors and records key performance indicators (KPIs) including:
    * **Average Wait Time**
    * **Peak Wait Time** (Maximum wait time experienced)
    * **Maximum Queue Length**
* **Data Visualization:** Generates visual output, such as line plots and bar charts, using `matplotlib` to analyze results over time or across different scenarios.

---

## 🛠️ Requirements

To run this simulation, you will need:

* **Python 3.80** or above

### Libraries

The following Python libraries are required for the simulation and data analysis/visualization:

* `matplotlib`
* `numpy`
* `pandas`

---

## 📥 Installation

You can clone or download the project files. Once you have the files, install the necessary dependencies using `pip`:

```bash
pip install matplotlib numpy pandas
````

## 🚀 Usage

To run the simulation and view the results, execute the main Python script from your terminal:

1.  **Clone the Repository:**
    ```bash
    git clone [repository_link_here]
    cd atm-queue-simulation
    ```
2.  **Run the Simulation:**
    ```bash
    python atm_queue_simulation.py
    ```

The results (metrics and analysis) will be displayed in the console, and visualization plots will open in a separate window for visual analysis.

---

## 📊 Scenarios and Analysis

The simulation is designed to test the impact of several key factors:

* **Number of ATMs:** Simulate the effect of scaling resources by adding more ATMs on customer wait times and throughput.
* **Customer Arrival Rate:** Analyze how different traffic levels (e.g., low, medium, or high arrival rates) affect queue length and overall system congestion.
* **Service Time:** Evaluate the impact of longer or shorter average service times (e.g., due to system lag or faster processes) on system efficiency and customer satisfaction.

---

## 📈 Potential Improvements 

The following enhancements are planned or suggested for future development:

* **Dynamic ATM Allocation:** Implement logic to bring more ATMs online **during peak hours** and scale down during off-peak times.
* **Service Time Optimization Modeling:** Incorporate variables to model the impact of faster card reading technologies or streamlined automated processes to see the real-world benefit of reduced service time.
* **Dynamic Queue Management:** Implement algorithms for prioritizing urgent or simple transactions (e.g., balance check vs. large withdrawal) to better manage the queue and reduce perceived wait times.
"""


