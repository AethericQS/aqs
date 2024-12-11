import numpy as np
import matplotlib.pyplot as plt
import random

def generate_aetheric_quantum_system(size=100):
    """
    Simulates an aetheric quantum system by generating a grid with random particle states.
    """
    system = np.random.choice(['q', 'g', '-'], size=(size, size), p=[0.3, 0.3, 0.4])
    return system

def display_aetheric_quantum_system(system):
    """
    Displays the aetheric quantum system simulation visually.
    """
    color_map = {'q': 'red', 'g': 'blue', '-': 'white'}
    image = np.zeros((system.shape[0], system.shape[1], 3))
    
    for i in range(system.shape[0]):
        for j in range(system.shape[1]):
            if system[i, j] == 'q':
                image[i, j] = [1, 0, 0]  # Red for quarks
            elif system[i, j] == 'g':
                image[i, j] = [0, 0, 1]  # Blue for gluons
            else:
                image[i, j] = [1, 1, 1]  # White for empty space
    
    plt.imshow(image)
    plt.title("Aetheric Quantum System Simulation")
    plt.axis("off")
    plt.show()

def simulate_neutrino_transport(steps=100):
    """
    Simulates the random walk of a neutrino through a 2D space.
    """
    x, y = [0], [0]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for _ in range(steps):
        dx, dy = random.choice(directions)
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
    
    plt.plot(x, y, marker='o', markersize=2, linestyle='-', color='purple')
    plt.title("Neutrino Transport Simulation")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.show()

def simulate_dark_matter_interactions(particles=50, steps=100):
    """
    Simulates dark matter particle movements and interactions in a 2D space.
    """
    positions = np.random.rand(particles, 2) * 100
    plt.figure(figsize=(6, 6))
    
    for _ in range(steps):
        forces = np.random.randn(particles, 2) * 0.5
        positions += forces
        positions = np.clip(positions, 0, 100)
        
        plt.clf()
        plt.scatter(positions[:, 0], positions[:, 1], c='black', s=10, alpha=0.7)
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.title("Dark Matter Interaction Simulation")
        plt.pause(0.01)
    
    plt.show()

def main():
    """
    Main function to run different quantum physics simulations.
    """
    print("Select a simulation to run:")
    print("1: Aetheric Quantum System Simulation")
    print("2: Neutrino Transport Simulation")
    print("3: Dark Matter Interaction Simulation")
    
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        system = generate_aetheric_quantum_system(size=100)
        display_aetheric_quantum_system(system)
    elif choice == "2":
        steps = int(input("Enter the number of steps for the neutrino transport simulation: "))
        simulate_neutrino_transport(steps=steps)
    elif choice == "3":
        particles = int(input("Enter the number of dark matter particles: "))
        steps = int(input("Enter the number of simulation steps: "))
        simulate_dark_matter_interactions(particles=particles, steps=steps)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
