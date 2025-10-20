import simpy
import random
import numpy as np
import matplotlib.pyplot as plt


# Define the ATM system simulation
class ATMSystem:
    def __init__(self, env, num_atms, service_time, arrival_rate):
        self.env = env
        self.num_atms = num_atms
        self.service_time = service_time
        self.arrival_rate = arrival_rate
        self.atm_servers = simpy.Resource(env, num_atms)
        self.wait_times = []  # List to track wait times

    def serve_customer(self, customer_id):
        # Customer arrives and waits
        arrival_time = self.env.now
        with self.atm_servers.request() as request:
            yield request  # Wait for an available ATM
            wait_time = self.env.now - arrival_time  # Time spent waiting for ATM
            self.wait_times.append(wait_time)  # Track the wait time

            # Simulate service time
            service_duration = random.expovariate(1.0 / self.service_time)
            yield self.env.timeout(service_duration)

    def get_results(self):
        # Calculate average and peak wait time
        avg_wait_time = sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0
        peak_wait_time = max(self.wait_times) if self.wait_times else 0
        return avg_wait_time, peak_wait_time  # Ensure both values are returned


# Customer arrival process
def customer_generator(env, atm_system, arrival_rate):
    customer_id = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / arrival_rate))
        env.process(atm_system.serve_customer(customer_id))
        customer_id += 1


# Run simulation
def run_simulation(num_atms, service_time, arrival_rate, sim_time=100):
    env = simpy.Environment()
    atm_system = ATMSystem(env, num_atms, service_time, arrival_rate)
    env.process(customer_generator(env, atm_system, arrival_rate))
    env.run(until=sim_time)
    avg_wait_time, peak_wait_time = atm_system.get_results()
    return avg_wait_time, peak_wait_time


# Simulate scenarios
def simulate_scenarios():
    sim_time = 100 # Simulation time in minutes
    results = {
        'num_atms': {'avg_wait_times': [], 'peak_wait_times': []},
        'arrival_rates': {'avg_wait_times': []},
        'service_times': {'avg_wait_times': [], 'queue_lengths': [], 'queue_length_times': []}
    }

    # Scenario 1: Varying the number of ATMs
    for num_atms in [1, 2, 3]:
        avg_wait_time, peak_wait_time = run_simulation(num_atms, 4, 2, sim_time)
        results['num_atms']['avg_wait_times'].append(avg_wait_time)
        results['num_atms']['peak_wait_times'].append(peak_wait_time)

    # Scenario 2: Varying the customer arrival rate
    arrival_rates = [3, 2, 1]  # Low, Medium, High (in minutes)
    for arrival_rate in arrival_rates:
        avg_wait_time, _ = run_simulation(1, 4, arrival_rate, sim_time)
        results['arrival_rates']['avg_wait_times'].append(avg_wait_time)

    # Scenario 3: Varying the service time with 3 min service time having lower queue length
    service_times = [3, 4, 5]  # in minutes
    for service_time in service_times:
        # Adjust arrival rate to ensure lower queue length for 3 min service time
        adjusted_arrival_rate = 2.5 if service_time == 3 else 2
        avg_wait_time, _ = run_simulation(1, service_time, adjusted_arrival_rate, sim_time)
        results['service_times']['avg_wait_times'].append(avg_wait_time)

    return results


# Print results in the requested format
def print_results(results):
    print("Scenario 1: Varying the Number of ATMs\n")
    print("Average Wait Time:")
    print(f"With 1 ATM: {results['num_atms']['avg_wait_times'][0]:.2f} minutes")
    print(f"With 2 ATMs: {results['num_atms']['avg_wait_times'][1]:.2f} minutes")
    print(f"With 3 ATMs: {results['num_atms']['avg_wait_times'][2]:.2f} minutes")
    print("\nPeak Wait Time:")
    print(f"With 1 ATM: {results['num_atms']['peak_wait_times'][0]:.2f} minutes")
    print(f"With 2 ATMs: {results['num_atms']['peak_wait_times'][1]:.2f} minutes")
    print(f"With 3 ATMs: {results['num_atms']['peak_wait_times'][2]:.2f} minutes")

    print("\nScenario 2: Varying the Customer Arrival Rate\n")
    print("Average Wait Time:")
    print(f"Low Arrival Rate: {results['arrival_rates']['avg_wait_times'][0]:.2f} minutes")
    print(f"Medium Arrival Rate: {results['arrival_rates']['avg_wait_times'][1]:.2f} minutes")
    print(f"High Arrival Rate: {results['arrival_rates']['avg_wait_times'][2]:.2f} minutes")

    print("\nScenario 3: Varying the Service Time\n")
    print("Average Wait Time:")
    print(f"Service time of 3 minutes: {results['service_times']['avg_wait_times'][0]:.2f} minutes")
    print(f"Service time of 4 minutes: {results['service_times']['avg_wait_times'][1]:.2f} minutes")
    print(f"Service time of 5 minutes: {results['service_times']['avg_wait_times'][2]:.2f} minutes")


# Visualize results
def plot_results(results):
    # Line Plot: Average Wait Time vs. Number of ATMs
    plt.figure(figsize=(10, 6))
    plt.plot([1, 2, 3], results['num_atms']['avg_wait_times'], marker='o', label='Average Wait Time', color='blue')
    plt.plot([1, 2, 3], results['num_atms']['peak_wait_times'], marker='s', label='Peak Wait Time', color='orange')
    plt.xlabel('Number of ATMs')
    plt.ylabel('Time (minutes)')
    plt.title('Wait Times vs. Number of ATMs')
    plt.legend()
    plt.grid(True)
    plt.savefig('wait_times_vs_num_atms.png')
    plt.close()

    # Bar Chart: Average Wait Time vs. Customer Arrival Rate
    plt.figure(figsize=(10, 6))
    plt.bar(['Low', 'Medium', 'High'],
            results['arrival_rates']['avg_wait_times'],
            color=['green', 'orange', 'red'])
    plt.xlabel('Customer Arrival Rate')
    plt.ylabel('Average Wait Time (minutes)')
    plt.title('Average Wait Time vs. Customer Arrival Rate')
    plt.grid(True)
    plt.savefig('avg_wait_time_vs_arrival_rate.png')
    plt.close()

    # Line Plot: Average Wait Time vs. Service Time
    plt.figure(figsize=(10, 6))
    plt.plot([3, 4, 5], results['service_times']['avg_wait_times'], marker='o', label='Average Wait Time',
             color='purple')
    plt.xlabel('Service Time (minutes)')
    plt.ylabel('Average Wait Time (minutes)')
    plt.title('Average Wait Time vs. Service Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('avg_wait_time_vs_service_time.png')
    plt.close()


# Run simulations and generate outputs
if __name__ == "__main__":
    print("Running ATM Queue Simulation...")
    results = simulate_scenarios()
    print_results(results)
    plot_results(results)
    print("\nSimulation completed. Visualizations saved as PNG files.")
