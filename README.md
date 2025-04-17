# 🦠 COVID-19 Dispersion Simulation using Cellular Automata
This project simulates the spread of COVID-19 in a simplified virtual population using cellular automata and probabilistic modeling. The goal is to illustrate how the virus propagates and how mitigation strategies like mask usage can affect the infection curve.

## 📌 Features
- Real-time simulation of population behavior
- States: Healthy, Infected, Recovered, Deceased
- Random mask usage per individual
- Adjustable infection probability before starting the simulation
- Visual indicators and color-coded statuses
- Automatic restart of simulation with updated parameters

## 🎥 Preview

Prob = 0.3
![Simulation demo](prob3.gif)

Prob = 0.8
![Simulation demo](prob8.gif)


## 🧠 How It Works
- Each person is represented as a dot in a grid.
- People move randomly unless deceased.
- When an infected individual is close to a healthy one, the virus may spread depending on the probability.
- Over time, infected individuals either recover or die, based on defined probabilities.

## 🛠️ Technologies Used
- Python 3
- Matplotlib (`pyplot`, `animation`, `widgets`)

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ere-AS/covid19-dispersion-simulation
   cd covid19-dispersion-simulation
