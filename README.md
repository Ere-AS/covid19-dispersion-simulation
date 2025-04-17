# 🦠 COVID-19 Dispersion Simulation using Cellular Automata

This project simulates the spread of COVID-19 in a simplified virtual population using cellular automata and probabilistic modeling. The goal is to illustrate how the virus propagates and how mitigation strategies—like mask usage—can affect the infection curve.

---

## 📌 Features

- Real-time simulation of population behavior
- States: Healthy, Infected, Recovered, Deceased
- Random mask usage per individual
- Adjustable infection probability before simulation starts
- Color-coded indicators for visual tracking
- Automatic restart of the simulation
- Interactive dashboard to analyze results

---

## 🎥 Simulation Previews

**Infection probability = 0.3**  
![Simulation demo](prob3.gif)

**Infection probability = 0.8**  
![Simulation demo](prob8.gif)

---

## 🌍 Live Dashboard

Explore the interactive dashboard built with Streamlit to analyze the simulation results:

👉 [Open Dashboard on Streamlit](https://covid19-dispersion-simulation.streamlit.app/)

---

## 🗂️ Dashboard Preview

![Dashboard demo](dashboard.gif)

---

## ▶️ Run the Dashboard Locally

If you prefer to run it on your machine:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch the dashboard:
   ```bash
   streamlit run dashboard_covid_streamlit.py
   ```

3. Once it opens in your browser, upload the generated `resultado_simulacion.csv` file to visualize the results.

---

## 🧠 How It Works

- Each individual is represented as a dot on a 2D grid.
- Individuals move randomly unless they are deceased.
- When an infected person is near a healthy one, there is a configurable chance of transmission.
- Infected individuals may either recover or die over time, based on defined probabilities.

---

## 🛠️ Technologies Used

- Python 3
- Matplotlib (`pyplot`, `animation`, `widgets`)
- Pandas (for exporting simulation data)
- Streamlit (for interactive dashboard)

---

## ▶️ How to Run the Simulation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ere-AS/covid19-dispersion-simulation
   cd covid19-dispersion-simulation
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ```bash
   python covidSimul.py
   ```

4. The simulation window will display the spread day by day. After it finishes, a CSV file will be saved and a chart will be displayed.

---

   
## 👩‍💻 Author
Developed by [Ere AS](https://github.com/Ere-AS)
Erendira Lizet Aguilar Salamanca
